SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET ANSI_WARNINGS OFF

DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date   DATE = '{end_date}'

DECLARE @free_license TINYINT = 6
DECLARE @paid		  TINYINT = 5

DECLARE @note			TINYINT = 3
DECLARE @description	TINYINT = 0

DECLARE @actual_lic_origin		TINYINT = 0
DECLARE @historical_lic_origin	TINYINT = 1

DECLARE @bug TINYINT = 2


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
			WHERE Status IN (@paid, @free_license) AND Id = oi.Order_Id) AS o
		CROSS APPLY(
			SELECT Id
			FROM CRM.dbo.SaleItems
			WHERE IsTraining = 0 AND Id=oi.SaleItem_Id) AS si
)


SELECT
		c.user_crmid	 AS user_crmid,
		u.FriendlyId	 AS user_id,
		ti.Id			 AS ticket_id,
		ti.TicketSCID	 AS ticket_scid,
		ti.TicketType	 AS ticket_type,
		ti.creation_date AS creation_date,
		ti.SupportTeam	 AS support_team,
		ti.IsPrivate	 AS is_private,
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
			SELECT	Id, TicketSCID, TicketType, CAST(Created AS DATE) AS creation_date, OwnerGuid, ISNULL(ProcessingSupportTeam, SupportTeam) AS SupportTeam, IsPrivate
			FROM 	DXStatisticsV2.dbo.TicketInfos
			WHERE 	Created BETWEEN @start_date AND @end_date ) AS ti
		CROSS APPLY (
			SELECT 	IsEmployee, FriendlyId
			FROM 	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Users
			WHERE	Id = ti.OwnerGuid AND FriendlyId != 'A2151720'
		)  AS u
		CROSS APPLY (
			SELECT	Id AS user_crmid
			FROM	CRM.dbo.Customers
			WHERE	FriendlyId = u.FriendlyId
		) AS c
WHERE IsEmployee = 0 OR TicketType = @bug

CREATE NONCLUSTERED INDEX idx_user_id ON #TicketsWithLicenses(user_id, license_status);
CREATE NONCLUSTERED INDEX idx_ticket_id ON #TicketsWithLicenses(ticket_id) INCLUDE (ticket_type, ticket_scid);