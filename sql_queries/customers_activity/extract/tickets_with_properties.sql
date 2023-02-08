DECLARE @licensed		TINYINT = 0
DECLARE @free			TINYINT = 3
DECLARE @trial			TINYINT = 4
DECLARE @converted_paid	TINYINT = 5
DECLARE @converted_free	TINYINT = 6;

WITH ticket_tags AS (
	SELECT
		Tickets AS ticket_id,
		STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), ' ') WITHIN GROUP (ORDER BY Tags ASC) AS tags
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
	ti.user_crmid						AS {user_crmid},
	ti.user_id							AS {user_id},
	tribes.Id							AS {tribe_id},
	tribes.Name							AS {tribe_name},
	ti.ticket_id						AS {ticket_id},
	ti.ticket_scid						AS {ticket_scid},
	ti.ticket_type						AS {ticket_type},
	ti.creation_date					AS {creation_date},
	ti.is_private						AS {is_private},
	ug.groups							AS {user_groups},
	tt.tags								AS {ticket_tags},
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
	ti.license_status					AS {license_status},
	ti.conversion_status				AS {conversion_status},
	dups.ticket_type					AS {duplicated_to_ticket_type},
	dups.ticket_scid					AS {duplicated_to_ticket_scid},
	CAST(single_selectors.OperatingSystem AS UNIQUEIDENTIFIER) AS {operating_system_id},
	CAST(single_selectors.IDE			  AS UNIQUEIDENTIFIER) AS {ide_id},
	CAST(single_selectors.ReplyId		  AS UNIQUEIDENTIFIER) AS {reply_id},
	CAST(single_selectors.ControlId		  AS UNIQUEIDENTIFIER) AS {component_id},
	CAST(single_selectors.FeatureId		  AS UNIQUEIDENTIFIER) AS {feature_id}
FROM tickets_with_licenses_and_conversion AS ti
	OUTER APPLY (
		SELECT
			Ticket_Id,
			[TicketStatus]		AS [TicketStatus],
			[ReplyId]			AS [ReplyId],
			[ControlId]			AS [ControlId],
			[FeatureId]			AS [FeatureId],
			[OperatingSystem]	AS [OperatingSystem],
			[IDE]				AS [IDE],
			[Severity]			AS [Severity]
		FROM (	SELECT Ticket_Id, Name, Value
				FROM [SupportCenterPaid].[c1f0951c-3885-44cf-accb-1a390f34c342].[TicketProperties]
				WHERE Name IN ('ReplyId', 'ControlId', 'FeatureId', 'OperatingSystem', 'IDE', 'Severity', 'TicketStatus') AND Ticket_Id = ti.ticket_id) AS tp
		PIVOT(MIN(Value) FOR Name IN ([TicketStatus], [ReplyId], [ControlId], [FeatureId], [OperatingSystem], [IDE], [Severity])) AS value ) AS single_selectors
	OUTER APPLY (
		SELECT 	
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'PlatformedProductId' AND Value NOT LIKE '%:%', CAST(Value AS UNIQUEIDENTIFIER), NULL)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS platforms_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'ProductId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS products_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'SpecificId',	 CAST(Value AS UNIQUEIDENTIFIER), NULL)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS specifics_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'BuildId',		 Value, NULL)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS builds_ids,
			STRING_AGG(CONVERT(NVARCHAR(MAX), IIF(Name = 'FixedInBuild', Value, NULL)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS fixed_in_builds_ids
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
		WHERE	Ticket_Id = ti.ticket_id) AS multi_selectors
	OUTER APPLY (
		SELECT	 TOP 1 AuditOwner AS closed_by, CAST(EntityModified AS DATE) AS closed_on
		FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
		WHERE	 Ticket_Id = ti.ticket_id AND Name = 'TicketStatus' AND Value = 'Closed'
		ORDER BY EntityModified DESC) AS closed_status_info
	OUTER APPLY (
		SELECT	 TOP 1 AuditOwner AS fixed_by, CAST(EntityModified AS DATE) AS fixed_on
		FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
		WHERE	 Ticket_Id = ti.ticket_id AND Name = 'FixedInBuild'
		ORDER BY EntityModified DESC) AS fixed_info
	OUTER APPLY (
		SELECT   TOP 1 t.Id, t.Name
		FROM	 DXStatisticsV2.dbo.TribeTeamMapping AS ttm
				 INNER JOIN CRM.dbo.Tribes AS t ON t.Id = ttm.Tribe
		WHERE    ttm.SupportTeam = ti.support_team 
		ORDER BY t.Name ) AS tribes
	OUTER APPLY (
		SELECT 	 STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') WITHIN GROUP (ORDER BY UserGroup_Id ASC) AS groups
		FROM 	 CRM.dbo.Customer_UserGroup
		WHERE 	 Customer_Id = ti.user_crmid ) AS ug
	OUTER APPLY (
		SELECT   ticket_scid, ticket_type 
		FROM     #TicketsWithLicenses AS twl
		WHERE    ticket_id = (SELECT TOP 1 Value
						      FROM	 SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
						      WHERE  Name = 'Duplicate' AND Ticket_Id = ti.ticket_id)) AS dups
	LEFT JOIN ticket_tags AS tt ON tt.ticket_id = ti.ticket_id