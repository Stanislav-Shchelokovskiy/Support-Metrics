SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET ANSI_WARNINGS OFF

DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date   DATE = '{end_date}'

DECLARE @free_license TINYINT = 6
DECLARE @paid		  TINYINT = 0

DECLARE @note			TINYINT = 3
DECLARE @description	TINYINT = 0

DECLARE @actual_lic_origin		TINYINT = 0
DECLARE @historical_lic_origin	TINYINT = 1


DECLARE @licensed		TINYINT = 0
DECLARE @expired		TINYINT = 1
DECLARE @revoked		TINYINT = 2
DECLARE @free			TINYINT = 3
DECLARE @trial			TINYINT = 4
DECLARE @converted_paid	TINYINT = 5
DECLARE @converted_free	TINYINT = 6;


DROP TABLE IF EXISTS #TicketsWithLicenses;
WITH enterprise_clients AS (
	SELECT
		Customer_Id AS customer_id
	FROM 
		DXStatisticsV2.dbo.UserInGroups
	WHERE 
		UserGroup_Id = '943B96B1-7C80-11E5-BF27-6470020143F0' --Barclays licensed customers
),

licenses_only AS (
	SELECT
		Owner_Id AS owner_crmid,
		EndUser_Id AS end_user_crmid,
		OrderItem_Id AS order_item_id,
		@actual_lic_origin AS lic_origin,
		NULL AS revoked_since
	FROM
		CRM.dbo.Licenses
	UNION
	SELECT
		Owner_Id,
		EndUser_Id,
		OrderItem_Id,
		@historical_lic_origin,
		CONVERT(DATE, EntityModified)
	FROM 
		CRMAudit.dxcrm.Licenses
),

licenses AS (
	SELECT
		owner_crmid,
		end_user_crmid,
		lic_origin,
		revoked_since,
		CONVERT(DATE, oi.SubscriptionStart) AS subscription_start,
		DATEADD(DAY, ISNULL(oi.HoldingPeriod, 99999), oi.SubscriptionStart) AS expiration_date,
		IIF(o.Status = @free_license, @free_license, @paid) AS free
	FROM
		licenses_only AS lcs 
		CROSS APPLY (
			SELECT SubscriptionStart, SaleItem_Id, Order_Id, HoldingPeriod
			FROM CRM.dbo.OrderItems
			WHERE Id = lcs.order_item_id) AS oi
		CROSS APPLY(
			SELECT Status
			FROM CRM.dbo.Orders
			WHERE ProcessedDate IS NOT NULL AND Id = oi.Order_Id) AS o
		CROSS APPLY(
			SELECT Id
			FROM CRM.dbo.SaleItems
			WHERE IsTraining = 0 AND Id=oi.SaleItem_Id) AS si
)


SELECT
		c.user_crmid				AS user_crmid,
		u.FriendlyId				AS user_id,
		ti.Id						AS ticket_id,
		ti.TicketSCID				AS ticket_scid,
		ti.TicketType				AS ticket_type,
		ti.creation_date			AS creation_date,
		ti.SupportTeam				AS support_team,
		IIF(EXISTS( SELECT TOP 1 end_user_crmid 
					FROM   licenses 
					WHERE  end_user_crmid = user_crmid AND 
						   creation_date BETWEEN subscription_start AND expiration_date AND
						   free = @paid
						) OR
						user_crmid IN (	SELECT	customer_id 
										FROM	enterprise_clients
						), @licensed,
							IIF(creation_date > (	SELECT IIF(MAX(lic_origin) = @historical_lic_origin, MAX(revoked_since), DATEFROMPARTS(9999,01,01)) 
													FROM   licenses 
													WHERE  end_user_crmid = user_crmid AND
														   free = @paid
								), @revoked,
									IIF(EXISTS( SELECT TOP 1 end_user_crmid 
												FROM   licenses 
												WHERE  end_user_crmid = user_crmid AND 
													   creation_date BETWEEN subscription_start AND expiration_date AND
													   free = @free_license
									), @free,
										IIF(creation_date < (	SELECT	ISNULL(MIN(subscription_start), DATEFROMPARTS(9999,01,01)) 
																FROM	licenses 
																WHERE	end_user_crmid = user_crmid
											), @trial, 
												@expired)))) AS license_status
INTO #TicketsWithLicenses
FROM (
			SELECT	Id, TicketSCID, TicketType, CAST(Created AS DATE) AS creation_date, OwnerGuid, ISNULL(ProcessingSupportTeam, SupportTeam) AS SupportTeam
			FROM 	DXStatisticsV2.dbo.TicketInfos
			WHERE 	Created BETWEEN @start_date AND @end_date ) AS ti
		CROSS APPLY (
			SELECT 	FriendlyId
			FROM 	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Users
			WHERE	IsEmployee = 0 AND Id = ti.OwnerGuid AND FriendlyId != 'A2151720'
		)  AS u
		CROSS APPLY (
			SELECT	Id AS user_crmid
			FROM	CRM.dbo.Customers
			WHERE	FriendlyId = u.FriendlyId
		) AS c

CREATE NONCLUSTERED INDEX idx_user_id ON #TicketsWithLicenses(user_id, license_status);


WITH ticket_tags AS (
	SELECT
		Tickets AS ticket_id,
		STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), ' ') AS tags
	FROM
		SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags
	GROUP BY
		Tickets
),

tickets_with_licenses_and_conversion AS (
	SELECT
		*,
		IIF(EXISTS(SELECT TOP 1 user_id
					   FROM #TicketsWithLicenses
					   WHERE user_id = ti.user_id AND license_status = @trial), 
				IIF(license_status = @licensed, @converted_paid, 
					IIF(license_status = @free,  @converted_free,
						IIF(license_status = @trial, 
							IIF(EXISTS(SELECT TOP 1 user_id
									   FROM #TicketsWithLicenses
									   WHERE user_id = ti.user_id AND license_status = @licensed), @converted_paid,
								IIF(EXISTS(SELECT TOP 1 user_id
										   FROM #TicketsWithLicenses
										   WHERE user_id = ti.user_id AND license_status = @free), @converted_free, 
								NULL)
							),
						NULL)
					)
				), 
			NULL) AS conversion_status
	FROM #TicketsWithLicenses AS ti
)

SELECT
	ti.user_crmid				AS {user_crmid},
	ti.user_id					AS {user_id},
	tribes.Id					AS {tribe_id},
	tribes.Name					AS {tribe_name},
	ti.ticket_id				AS {ticket_id},
	ti.ticket_scid				AS {ticket_scid},
	ti.ticket_type				AS {ticket_type},
	ti.creation_date			AS {creation_date},
	ug.groups					AS {user_groups},
	tt.tags						AS {ticket_tags},
	platforms.ids				AS {platforms},
	products.ids				AS {products},
	CAST(cat.ReplyId	AS UNIQUEIDENTIFIER) AS {reply_id},
	CAST(cat.ControlId	AS UNIQUEIDENTIFIER) AS {component_id},
	CAST(cat.FeatureId	AS UNIQUEIDENTIFIER) AS {feature_id},
	ti.license_status			AS {license_status},
	ti.conversion_status		AS {conversion_status}
FROM tickets_with_licenses_and_conversion AS ti
	OUTER APPLY (
		SELECT
			Ticket_Id,
			[ReplyId] AS [ReplyId],
			[ControlId] AS [ControlId],
			[FeatureId] AS [FeatureId]
		FROM (	SELECT Ticket_Id, Name, Value
				FROM [SupportCenterPaid].[c1f0951c-3885-44cf-accb-1a390f34c342].[TicketProperties]
				WHERE Name IN ('ReplyId', 'ControlId', 'FeatureId') AND Ticket_Id = ti.ticket_id) AS tp
		PIVOT(MIN(Value) FOR Name IN ([ReplyId], [ControlId], [FeatureId])) AS value ) AS cat
	OUTER APPLY (
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') AS groups
		FROM 	CRM.dbo.Customer_UserGroup
		WHERE 	Customer_Id = ti.user_crmid ) AS ug
	OUTER APPLY (
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), CAST(Value AS UNIQUEIDENTIFIER)), ' ') AS ids
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
		WHERE	Name = 'PlatformedProductId' AND Ticket_Id = ti.ticket_id AND Value NOT LIKE '%:%') AS platforms
	OUTER APPLY (
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), CAST(Value AS UNIQUEIDENTIFIER)), ' ') AS ids
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
		WHERE	Name = 'ProductId' AND Ticket_Id = ti.ticket_id) AS products
	OUTER APPLY (
		SELECT  TOP 1 t.Id, t.Name
		FROM	DXStatisticsV2.dbo.TribeTeamMapping AS ttm
				INNER JOIN CRM.dbo.Tribes AS t ON t.Id = ttm.Tribe
		WHERE   ttm.SupportTeam = ti.support_team 
		ORDER BY t.Name ) AS tribes
	LEFT JOIN ticket_tags AS tt ON tt.ticket_id = ti.ticket_id