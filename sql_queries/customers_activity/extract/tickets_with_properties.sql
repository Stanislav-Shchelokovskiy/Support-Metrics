DECLARE @separator CHAR = ';'

DECLARE @licensed				 TINYINT = 0
DECLARE @free					 TINYINT = 1
DECLARE @trial					 TINYINT = 8
DECLARE @converted_paid			 TINYINT = 9
DECLARE @converted_free			 TINYINT = 10;

SELECT
	ti.user_crmid						AS {user_crmid},
	ti.user_id							AS {user_id},
	tribes.tribes_ids					AS {tribes_ids},
	tribes.tribes_names					AS {tribes_names},
	ti.ticket_id						AS {ticket_id},
	ti.ticket_scid						AS {ticket_scid},
	ti.ticket_type						AS {ticket_type},
	ti.creation_date					AS {creation_date},
	ti.is_private						AS {is_private},
	ug.groups							AS {user_groups},
	ticket_tags.tags					AS {ticket_tags},
	multi_selectors.platforms_ids		AS {platforms},
	multi_selectors.products_ids		AS {products},
	multi_selectors.specifics_ids		AS {frameworks},
	multi_selectors.builds_ids			AS {builds},
	multi_selectors.fixed_in_builds_ids	AS {fixed_in_builds},
	fixed_info.fixed_by					AS {fixed_by},
	fixed_info.fixed_on					AS {fixed_on},
	single_selectors.TicketStatus		AS {ticket_status},
	closed_status_info.closed_by		AS {closed_by},
	closed_status_info.closed_on		AS {closed_on},
	single_selectors.Severity			AS {severity},
	dups.ticket_type					AS {duplicated_to_ticket_type},
	dups.ticket_scid					AS {duplicated_to_ticket_scid},
	CAST(single_selectors.Assignee		  AS UNIQUEIDENTIFIER) AS {assigned_to},
	CAST(single_selectors.OperatingSystem AS UNIQUEIDENTIFIER) AS {operating_system_id},
	CAST(single_selectors.IDE			  AS UNIQUEIDENTIFIER) AS {ide_id},
	CAST(single_selectors.ReplyId		  AS UNIQUEIDENTIFIER) AS {reply_id},
	CAST(single_selectors.ControlId		  AS UNIQUEIDENTIFIER) AS {component_id},
	CAST(single_selectors.FeatureId		  AS UNIQUEIDENTIFIER) AS {feature_id},
	ti.license_name						AS {license_name},
	ti.subscription_start				AS {subscription_start},
	ti.expiration_date					AS {expiration_date},
	ti.license_status					AS {license_status},
	IIF(EXISTS(	SELECT	TOP 1 user_id
				FROM	#TicketsWithLicenses
				WHERE	user_id = ti.user_id AND license_status = @trial), 
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
			NULL)						AS {conversion_status}
FROM #TicketsWithLicenses AS ti
	OUTER APPLY (
		SELECT
			Ticket_Id,
			[Assignee]			AS [Assignee],
			[TicketStatus]		AS [TicketStatus],
			[ReplyId]			AS [ReplyId],
			[ControlId]			AS [ControlId],
			[FeatureId]			AS [FeatureId],
			[OperatingSystem]	AS [OperatingSystem],
			[IDE]				AS [IDE],
			[Severity]			AS [Severity]
		FROM (	SELECT Ticket_Id, Name, Value
				FROM [SupportCenterPaid].[c1f0951c-3885-44cf-accb-1a390f34c342].[TicketProperties]
				WHERE Name IN ('ReplyId', 'ControlId', 'FeatureId', 'OperatingSystem', 'IDE', 'Severity', 'TicketStatus', 'Assignee') AND Ticket_Id = ti.ticket_id) AS tp
		PIVOT(MIN(Value) FOR Name IN ([Assignee], [TicketStatus], [ReplyId], [ControlId], [FeatureId], [OperatingSystem], [IDE], [Severity])) AS value
	) AS single_selectors
	OUTER APPLY (
		SELECT 	
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'PlatformedProductId' AND Value NOT LIKE '%:%', CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) WITHIN GROUP (ORDER BY Value ASC) AS platforms_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'ProductId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) WITHIN GROUP (ORDER BY Value ASC) AS products_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'SpecificId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) WITHIN GROUP (ORDER BY Value ASC) AS specifics_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'BuildId',		 Value, NULL)), @separator) WITHIN GROUP (ORDER BY Value ASC) AS builds_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'FixedInBuild', Value, NULL)), @separator) WITHIN GROUP (ORDER BY Value ASC) AS fixed_in_builds_ids
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
		WHERE	Ticket_Id = ti.ticket_id
	) AS multi_selectors
	OUTER APPLY (
		SELECT	 TOP 1 AuditOwner AS closed_by, CAST(EntityModified AS DATE) AS closed_on
		FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
		WHERE	 Ticket_Id = ti.ticket_id AND Name = 'TicketStatus' AND Value = 'Closed'
		ORDER BY EntityModified DESC
	) AS closed_status_info
	OUTER APPLY (
		SELECT	 TOP 1 AuditOwner AS fixed_by, CAST(EntityModified AS DATE) AS fixed_on
		FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
		WHERE	 Ticket_Id = ti.ticket_id AND Name = 'FixedInBuild'
		ORDER BY EntityModified DESC
	) AS fixed_info
	OUTER APPLY (
		SELECT	STRING_AGG(CONVERT(NVARCHAR(MAX), tribes_inner.id) , ' ') WITHIN GROUP (ORDER BY id ASC) AS tribes_ids,
				STRING_AGG(CONVERT(NVARCHAR(MAX), tribes_inner.name) , ' ') WITHIN GROUP (ORDER BY id ASC) AS tribes_names	
		FROM (	SELECT *, MIN(level) OVER() AS max_level
				FROM (	SELECT TOP 1 Id AS id, Name AS name, 1 AS level
						FROM   CRM.dbo.Tribes
						WHERE  Id = (SELECT TOP 1 value
									 FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
									 WHERE	Ticket_Id = @ticket_id  AND Name = 'ProcessingTribe')
						UNION
						SELECT product_tribe_id, product_tribe_name, 2
						FROM   #PlatformsProductsTribes
						WHERE  product_id IN (	SELECT	value
												FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
												WHERE	Ticket_Id = @ticket_id  AND Name = 'ProductId')
							   AND product_tribe_id IS NOT NULL
						UNION
						SELECT platform_tribe_id, platform_tribe_name, 2
						FROM   #PlatformsProductsTribes
						WHERE  platform_id IN (	SELECT	value
												FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
												WHERE	Ticket_Id = @ticket_id AND Name = 'PlatformedProductId' AND Value NOT LIKE '%:%')) AS ti) AS tribes_inner
		WHERE id IS NOT NULL AND level = max_level
	) AS tribes
	OUTER APPLY (
		SELECT 	 STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), @separator) WITHIN GROUP (ORDER BY UserGroup_Id ASC) AS groups
		FROM 	 CRM.dbo.Customer_UserGroup
		WHERE 	 Customer_Id = ti.user_crmid
	) AS ug
	OUTER APPLY (
		SELECT   ticket_scid, ticket_type 
		FROM     #TicketsWithLicenses AS twl
		WHERE    ticket_id = (SELECT TOP 1 Value
						      FROM	 SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
						      WHERE  Name = 'Duplicate' AND Ticket_Id = ti.ticket_id)
	) AS dups
	OUTER APPLY (
		SELECT	STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), @separator) WITHIN GROUP (ORDER BY Tags ASC) AS tags
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags
		WHERE	Tickets = ti.ticket_id
	) AS ticket_tags
