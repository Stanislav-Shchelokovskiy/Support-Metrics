DECLARE @separator CHAR = ';'

DECLARE @licensed		TINYINT = 0
DECLARE @free			TINYINT = 1
DECLARE @trial			TINYINT = 11

DECLARE @converted_paid	TINYINT = 0
DECLARE @converted_free	TINYINT = 1

DECLARE @bug			TINYINT = 2

SELECT
	ti.user_crmid						AS {user_crmid},
	ti.user_id							AS {user_id},
	ti.is_employee						AS {is_employee},
	ti.user_register_date 				AS {user_register_date},
	tribes.tribes_ids					AS {tribes_ids},
	tribes.tribes_names					AS {tribes_names},
	CAST(tent.id AS UNIQUEIDENTIFIER)	AS {tent_id},
	tent.name							AS {tent_name},
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
	conversion_to_bug.happened_on		AS {converted_to_bug_on},
	dups.ticket_type					AS {duplicated_to_ticket_type},
	dups.ticket_scid					AS {duplicated_to_ticket_scid},
	CAST(single_selectors.Assignee		  AS UNIQUEIDENTIFIER) AS {assigned_to},
	CAST(single_selectors.OperatingSystem AS UNIQUEIDENTIFIER) AS {operating_system_id},
	CAST(single_selectors.IDE			  AS UNIQUEIDENTIFIER) AS {ide_id},
	CAST(single_selectors.ReplyId		  AS UNIQUEIDENTIFIER) AS {reply_id},
	CAST(single_selectors.ControlId		  AS UNIQUEIDENTIFIER) AS {component_id},
	CAST(single_selectors.FeatureId		  AS UNIQUEIDENTIFIER) AS {feature_id},
	ti.license_name						AS {license_name},
	ti.parent_license_name				AS {parent_license_name},
	ti.subscription_start				AS {subscription_start},
	ti.expiration_date					AS {expiration_date},
	ti.license_status					AS {license_status},
	CASE
		WHEN ti.license_status IN (@licensed, @free) AND EXISTS(SELECT	TOP 1 twl.user_id FROM #TicketsWithLicenses AS twl WHERE twl.user_id = ti.user_id AND twl.license_status = @trial)
			THEN IIF(ti.license_status = @licensed, @converted_paid, @converted_free)
		WHEN ti.license_status = @trial
			THEN ISNULL((	SELECT TOP 1 @converted_paid
							FROM #TicketsWithLicenses AS twl
							WHERE twl.user_id = ti.user_id AND twl.license_status = @licensed),
						(	SELECT TOP 1 @converted_free
							FROM #TicketsWithLicenses AS twl
							WHERE twl.user_id = ti.user_id AND twl.license_status = @free))
		ELSE NULL
	END 								AS {conversion_status}
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
		FROM (	SELECT 	Ticket_Id, Name, Value
				FROM 	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
				WHERE 	Name IN ('ReplyId', 'ControlId', 'FeatureId', 'OperatingSystem', 'IDE', 'Severity', 'TicketStatus', 'Assignee')
					AND Ticket_Id = ti.ticket_id	) AS tp
		PIVOT(MIN(Value) FOR Name IN ([Assignee], [TicketStatus], [ReplyId], [ControlId], [FeatureId], [OperatingSystem], [IDE], [Severity])) AS value
	) AS single_selectors
	OUTER APPLY (
		SELECT 	
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'PlatformedProductId' AND Value NOT LIKE '%:%', CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) AS platforms_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'ProductId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) AS products_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'SpecificId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), @separator) AS specifics_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'BuildId',		 Value, NULL)), @separator) AS builds_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'FixedInBuild', Value, NULL)), @separator) AS fixed_in_builds_ids
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
		SELECT TOP 1 CAST(Modified AS DATE) AS happened_on
		FROM 	scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets
		WHERE 	ChangedProperties LIKE '%EntityType%'
			AND EntityOid = ti.ticket_id
			AND	EntityType = @bug
	) AS conversion_to_bug
	OUTER APPLY (
		SELECT	STRING_AGG(CONVERT(NVARCHAR(MAX), tribes_inner.id) , @separator)   AS tribes_ids,
				STRING_AGG(CONVERT(NVARCHAR(MAX), tribes_inner.name) , @separator) AS tribes_names	
		FROM	DXStatisticsV2.dbo.get_ticket_tribes(ti.ticket_id, ti.ticket_type, DEFAULT ) AS tribes_inner
	) AS tribes
	OUTER APPLY (
		SELECT	tent_inner.*
		FROM	DXStatisticsV2.dbo.get_ticket_tent(ti.ticket_id) AS tent_inner
	) AS tent
	OUTER APPLY (
		SELECT 	 STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), @separator) AS groups
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
		SELECT	STRING_AGG(CONVERT(NVARCHAR(MAX), CONCAT('(', Tags, ')')), @separator) AS tags
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags
		WHERE	Tickets = ti.ticket_id
	) AS ticket_tags
