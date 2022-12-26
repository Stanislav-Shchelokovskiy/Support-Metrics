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


WITH ticket_tags AS (
	SELECT
		Tickets AS ticket_id,
		STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), ' ') AS tags
	FROM
		SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags
	GROUP BY
		Tickets
),

enterprise_clients AS (
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
		oi.SubscriptionStart AS subscription_start,
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
),

tickets AS (
	SELECT
		crmCustomer.Id				AS user_crmid,
		u.FriendlyId				AS user_id,
		tribes.Id					AS tribe_id,
		tribes.Name					AS tribe_name,
		ti.Id						AS ticket_id,
		ti.TicketSCID				AS ticket_scid,
		ti.TicketType				AS ticket_type,
		CAST(ti.Created AS DATE)	AS creation_date,
		ug.groups					AS user_groups,
		tt.tags						AS ticket_tags,
		platforms.ids				AS platforms,
		products.ids				AS products,
		CAST(cat.ReplyId	AS UNIQUEIDENTIFIER) AS reply_id,
		CAST(cat.ControlId	AS UNIQUEIDENTIFIER) AS component_id,
		CAST(cat.FeatureId	AS UNIQUEIDENTIFIER) AS feature_id
	FROM 
		(SELECT *
		 FROM 	DXStatisticsV2.dbo.TicketInfos
		 WHERE 	Created BETWEEN @start_date AND @end_date ) AS ti
		OUTER APPLY (
			SELECT
				Ticket_Id,
				[ReplyId] AS [ReplyId],
				[ControlId] AS [ControlId],
				[FeatureId] AS [FeatureId]
			FROM ( SELECT Ticket_Id, Name, Value
					FROM [SupportCenterPaid].[c1f0951c-3885-44cf-accb-1a390f34c342].[TicketProperties]
					WHERE Name IN ('ReplyId', 'ControlId', 'FeatureId') AND Ticket_Id = ti.Id) AS tp
			PIVOT(MIN(Value) FOR Name IN ([ReplyId], [ControlId], [FeatureId])) AS value ) AS cat
		CROSS APPLY (
			SELECT 	FriendlyId
			FROM 	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Users
			WHERE	IsEmployee = 0 AND Id = ti.OwnerGuid AND FriendlyId != 'A2151720'
		)  AS u
		INNER JOIN CRM.dbo.Customers AS crmCustomer ON crmCustomer.FriendlyId = u.FriendlyId
		OUTER APPLY(
			SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') AS groups
			FROM 	CRM.dbo.Customer_UserGroup
			WHERE 	Customer_Id = crmCustomer.Id ) AS ug
		OUTER APPLY(
			SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), CAST(Value AS UNIQUEIDENTIFIER)), ' ') AS ids
			FROM SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
			WHERE Name = 'PlatformedProductId' AND Ticket_Id = ti.Id AND Value NOT LIKE '%:%') AS platforms
		OUTER APPLY(
			SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), CAST(Value AS UNIQUEIDENTIFIER)), ' ') AS ids
			FROM SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
			WHERE Name = 'ProductId' AND Ticket_Id = ti.Id) AS products
		LEFT JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = ISNULL(ti.ProcessingSupportTeam, ti.SupportTeam)
		INNER JOIN CRM.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id
		LEFT JOIN ticket_tags AS tt ON tt.ticket_id = ti.Id
),

employees AS (
	SELECT 
		u.Id 						  AS id,
		e.Id		 				  AS crmid,
		u.PublicName 				  AS name,
		tribes.Id 					  AS tribe_id,
		tribes.Name 				  AS tribe_name,
		e.EmployeePosition_Id 		  AS position_id,
		ep.Name 					  AS position_name,
		IIF(eer.Id IS NOT NULL, 1, 0) AS has_support_processing_role,
		e.retired					  AS retired,
		IIF(l.Id IS NOT NULL, 1, 0)	  AS is_junior
	FROM (SELECT Id, 
				 Tribe_Id, 
				 EmployeePosition_Id,
				 EmployeeLevel_Id,
				 IIF(RetiredAt IS NOT NULL AND RetirementReason IS NOT NULL, 1, 0) AS retired  
			FROM crm.dbo.Employees ) AS e
			INNER JOIN CRM.dbo.Customers AS c ON c.Id = e.Id
			CROSS APPLY (
			SELECT Id, PublicName, FriendlyId
			FROM   SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Users 
			WHERE  Id != '66CA407C-2E49-4079-ABC1-A7B3BE418668' AND
				   FriendlyId = c.FriendlyId ) AS u
			OUTER APPLY (
			SELECT Id
			FROM   crm.dbo.EmployeeLevels
			WHERE  Id = e.EmployeeLevel_Id AND
				   (Name LIKE '%Junior%' OR Name LIKE '%Trainee%') ) AS l
			LEFT JOIN crm.dbo.Tribes AS tribes ON tribes.Id = e.Tribe_Id
			LEFT JOIN crm.dbo.EmployeePositions AS ep ON ep.Id = e.EmployeePosition_Id
			LEFT JOIN crm.dbo.Employee_EmployeeRole AS eer ON e.Id = eer.Employee_Id AND
															  eer.EmployeeRole_Id = '4D99A826-A414-45F8-A3F9-4F57564E4B24'
),

tickets_with_iterations AS (
	SELECT
		t.user_crmid,
		t.user_id,
		t.tribe_id,
		t.tribe_name,
		t.ticket_scid,
		t.ticket_type,
		t.creation_date,
		t.user_groups,
		t.ticket_tags,
		t.platforms,
		t.products,
		t.reply_id,
		t.component_id,
		t.feature_id,
		p.Id			AS emp_post_id,
		e.crmid			AS emp_crmid,
		e.name			AS emp_name,
		e.position_id	AS emp_pos_id,
		e.position_name AS emp_pos_name,
		e.tribe_id		AS emp_tribe_id,
		e.tribe_name	AS emp_tribe_name
	FROM 
		tickets AS t
		LEFT JOIN DXStatisticsV2.dbo.IterationItems AS ii ON ii.TicketId = t.ticket_id
		CROSS APPLY	(SELECT Id, Owner
					 FROM   DXStatisticsV2.dbo.Posts
					 WHERE  Created BETWEEN @start_date AND @end_date AND 
							Id = ii.PostId AND
							Type NOT IN (@note, @description)) AS p
		INNER JOIN	employees AS e ON e.id = p.Owner
)


INSERT INTO #TicketsWithIterationsAndLicenses
SELECT
	*,
	IIF(EXISTS( SELECT TOP 1 end_user_crmid 
				FROM   licenses 
				WHERE  end_user_crmid = user_crmid AND 
						creation_date BETWEEN subscription_start AND expiration_date AND
						free = @paid
					) OR
					user_crmid IN (	SELECT	customer_id 
									FROM	enterprise_clients
					), @licensed,
						IIF(EXISTS( SELECT TOP 1 end_user_crmid 
									FROM   licenses 
									WHERE  end_user_crmid = user_crmid AND 
											creation_date BETWEEN subscription_start AND expiration_date AND
											free = @free_license
						), @free,
							IIF(creation_date < (	SELECT	ISNULL(MIN(subscription_start), DATEFROMPARTS(9999,01,01)) 
													FROM	licenses 
													WHERE	end_user_crmid = user_crmid
								), 
								@trial, 
									IIF(creation_date > (	SELECT IIF(MAX(lic_origin) = @historical_lic_origin, MAX(revoked_since), DATEFROMPARTS(9999,01,01)) 
															FROM   licenses 
															WHERE  end_user_crmid = user_crmid
										), 
										@revoked, 
											@expired)))) AS license_status
FROM
	tickets_with_iterations