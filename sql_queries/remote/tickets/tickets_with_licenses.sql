SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET ANSI_WARNINGS OFF

DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date   DATE = '{end_date}'

DECLARE @separator CHAR = ';'

DECLARE @paid		  TINYINT = 5
DECLARE @free_license TINYINT = 6

DECLARE @actual_lic_origin     TINYINT = 0

DECLARE @licensed					TINYINT = 0
DECLARE @free						TINYINT = 1
DECLARE @expired					TINYINT = 2
DECLARE @revoked					TINYINT = 3
DECLARE @assigned_to_someone		TINYINT = 4
DECLARE @no_license					TINYINT = 5
DECLARE @no_license_revoked			TINYINT = 6
DECLARE @no_license_expired			TINYINT = 7
DECLARE @no_license_expired_revoked	TINYINT = 8
DECLARE @no_license_free			TINYINT = 9
DECLARE @no_license_expired_free	TINYINT = 10
DECLARE @trial						TINYINT = 11

DECLARE @converted_paid	TINYINT = 0
DECLARE @converted_free	TINYINT = 1

DECLARE @best_suitable		TINYINT = 0
DECLARE @better_suitable	TINYINT = 1
DECLARE @suitable			TINYINT = 2
DECLARE @least_suitable		TINYINT = 3


DROP TABLE IF EXISTS #TicketsWithLicenses;
WITH enterprise_clients AS (
	SELECT	User_Id AS customer_id
	FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].UserInGroup
	WHERE	UserGroup_Id = '943B96B1-7C80-11E5-BF27-6470020143F0' --Barclays licensed customers
),

licenses AS (
	SELECT	owner_crmid,
			end_user_crmid,
			lic_origin,
			revoked_since,
			oi.subscription_start,
			oi.expiration_date,
			o.free,
			si.license_name,
			si.parent_license_name,
			platforms.licensed_platforms,
			products.licensed_products
	FROM	#LisencesOnly AS lcs 
			CROSS APPLY (
				SELECT	CONVERT(DATE, SubscriptionStart)												AS subscription_start,
						CONVERT(DATE, DATEADD(DAY, ISNULL(HoldingPeriod, 99999), SubscriptionStart))	AS expiration_date,
						SaleItem_Id	AS sale_item_id, 
						Order_Id	AS order_id
				FROM	CRM.dbo.OrderItems
				WHERE	Id = lcs.order_item_id
			) AS oi
			OUTER APPLY ( 
				SELECT	FreeSaleItem_Id	AS sale_item_id
				FROM	CRM.dbo.License_FreeSaleItem
				WHERE	License_Id = lcs.id 
			) AS bundled_skus
			CROSS APPLY(
				SELECT	Status AS free
				FROM	CRM.dbo.Orders
				WHERE	Id = oi.Order_Id AND Status IN (@paid, @free_license) 
			) AS o
			CROSS APPLY(
				SELECT	name													AS license_name,
						IIF(id = oi.sale_item_id,
							NULL,
							(	SELECT TOP 1 name
								FROM   #SaleItemsFlat
								WHERE  id = oi.sale_item_id	))					AS parent_license_name,
						item													AS item
				FROM	#SaleItemsFlat
				WHERE	id IN (oi.sale_item_id, bundled_skus.sale_item_id)
			) AS si
			OUTER APPLY (
				SELECT	STRING_AGG(CONVERT(NVARCHAR(MAX), sip.platform_id), @separator) AS licensed_platforms
				FROM	#SaleItemPlatforms AS sip
				WHERE	sip.sale_item_id = si.item
			) AS platforms
			OUTER APPLY (
				SELECT	STRING_AGG(CONVERT(NVARCHAR(MAX), sip.product_id), @separator) AS licensed_products
				FROM	#SaleItemProducts AS sip
				WHERE	sip.sale_item_id = si.item
			) AS products
)

SELECT
		customers.user_crmid				AS user_crmid,
		customers.register_date				AS user_register_date,
		users.FriendlyId					AS user_id,
		users.IsEmployee					AS is_employee,
		tickets.Id							AS ticket_id,
		tickets.FriendlyId					AS ticket_scid,
		tickets.EntityType					AS ticket_type,
		tickets.creation_date				AS creation_date,
		tickets.IsPrivate					AS is_private,
		multi_selectors.specifics_ids		AS specifics,
		multi_selectors.builds_ids			AS builds,
		multi_selectors.fixed_in_builds_ids	AS fixed_in_builds,
		multi_selectors.platforms_ids		AS ticket_platforms,
		multi_selectors.products_ids		AS ticket_products,
		licenses.*,
		CASE
			WHEN suitability IN (@best_suitable, @better_suitable)	THEN IIF(licenses.free = @paid, @licensed, @free)
			WHEN suitability = @suitable							THEN @expired
			WHEN suitability = @least_suitable						THEN IIF(licenses.owner_crmid = customers.user_crmid, @assigned_to_someone, @revoked)
			ELSE ISNULL((	SELECT TOP 1 lic_status
							FROM ( SELECT	CASE
												WHEN tickets.creation_date < MIN(subscription_start) OVER ()
													THEN @trial
												WHEN tickets.creation_date <= expiration_date 
													THEN IIF(free = @free_license, @no_license_free, IIF(revoked_since IS NULL, @no_license, @no_license_revoked))
												WHEN expiration_date IS NOT NULL AND tickets.creation_date > expiration_date 
													THEN IIF(free = @free_license, @no_license_expired_free, IIF(revoked_since IS NULL, @no_license_expired, @no_license_expired_revoked))
												ELSE NULL 
											END AS lic_status,
											expiration_date
									FROM licenses
									WHERE licenses.end_user_crmid = customers.user_crmid ) AS not_matched_licensess
							WHERE lic_status IS NOT NULL
							ORDER BY lic_status ASC, expiration_date DESC), 
					IIF(EXISTS(SELECT TOP 1 customer_id FROM enterprise_clients WHERE customer_id = customers.user_crmid), @licensed, @trial))
		END									AS license_status
INTO #TicketsWithLicenses
FROM (	SELECT	Id, FriendlyId, EntityType, CAST(Created AS DATE) AS creation_date, Owner, IsPrivate
		FROM   	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets
		WHERE 	Created BETWEEN @start_date AND @end_date ) AS tickets
		OUTER APPLY (
			SELECT 	
				STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'PlatformedProductId' AND 
													  Value NOT LIKE '%:%',  CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) AS platforms_ids,
				STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'ProductId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) AS products_ids,
				STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'SpecificId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) AS specifics_ids,
				STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'BuildId',		 Value, NULL)),							  @separator) AS builds_ids,
				STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'FixedInBuild', Value, NULL)),							  @separator) AS fixed_in_builds_ids
			FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
			WHERE	Ticket_Id = tickets.Id
		) AS multi_selectors
		CROSS APPLY (
			SELECT 	IsEmployee, FriendlyId
			FROM 	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Users
			WHERE	Id = tickets.Owner AND FriendlyId != 'A2151720' /* doc.ctor */
		)  AS users
		CROSS APPLY (
			SELECT	Id AS user_crmid, CAST(ISNULL(RegisterDate, '1990-01-01') AS DATE) AS register_date
			FROM	CRM.dbo.Customers
			WHERE	FriendlyId = users.FriendlyId
		) AS customers
		OUTER APPLY (
			SELECT	TOP 1 licenses_inner.*
			FROM	(	SELECT	licenses_most_inner.*,
							CASE 
								WHEN tickets.creation_date BETWEEN licenses_most_inner.subscription_start AND licenses_most_inner.expiration_date AND owner_crmid = end_user_crmid AND lic_origin = @actual_lic_origin
									THEN IIF(parent_license_name IS NULL, @best_suitable, @better_suitable)
								WHEN licenses_most_inner.revoked_since IS NULL AND licenses_most_inner.expiration_date IS NOT NULL AND tickets.creation_date > licenses_most_inner.expiration_date
									THEN @suitable
								WHEN licenses_most_inner.revoked_since IS NOT NULL
									THEN IIF(tickets.creation_date > licenses_most_inner.revoked_since, @least_suitable, @better_suitable)
								ELSE NULL
							END AS suitability
						FROM	licenses AS licenses_most_inner
						WHERE	end_user_crmid = customers.user_crmid 
					) AS licenses_inner
			WHERE	suitability IS NOT NULL AND
					(	EXISTS (	SELECT	*
									FROM	STRING_SPLIT(multi_selectors.products_ids, @separator)   AS tp
											INNER JOIN STRING_SPLIT(licenses_inner.licensed_products, @separator) AS lp ON lp.value = tp.value ) 
						OR
						EXISTS (	SELECT	*
									FROM	STRING_SPLIT(multi_selectors.platforms_ids, @separator)	  AS tp
											INNER JOIN STRING_SPLIT(licenses_inner.licensed_platforms, @separator) AS lp ON lp.value = tp.value))
			ORDER BY suitability, lic_origin, free	
		) AS licenses
WHERE IsEmployee = 0 OR EntityType IN (2 /* Bug Report */, 6 /* Breaking Change */ )

CREATE NONCLUSTERED INDEX idx_userid_ls ON #TicketsWithLicenses(user_id, license_status)
CREATE CLUSTERED INDEX idx_tickettype_ticketscid ON #TicketsWithLicenses(ticket_id)
