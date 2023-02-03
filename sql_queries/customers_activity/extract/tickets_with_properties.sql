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
	ti.conversion_status		AS {conversion_status},
	dups.ticket_type			AS {duplicated_to_ticket_type},
	dups.ticket_scid			AS {duplicated_to_ticket_scid}
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
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') WITHIN GROUP (ORDER BY UserGroup_Id ASC) AS groups
		FROM 	CRM.dbo.Customer_UserGroup
		WHERE 	Customer_Id = ti.user_crmid ) AS ug
	OUTER APPLY (
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), CAST(Value AS UNIQUEIDENTIFIER)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS ids
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
		WHERE	Name = 'PlatformedProductId' AND Ticket_Id = ti.ticket_id AND Value NOT LIKE '%:%') AS platforms
	OUTER APPLY (
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), CAST(Value AS UNIQUEIDENTIFIER)), ' ') WITHIN GROUP (ORDER BY Value ASC) AS ids
		FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
		WHERE	Name = 'ProductId' AND Ticket_Id = ti.ticket_id) AS products
	OUTER APPLY (
		SELECT ticket_scid, ticket_type 
		FROM #TicketsWithLicenses AS twl
		WHERE ticket_id = (SELECT	TOP 1 Value
						   FROM		SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
						   WHERE	Name = 'Duplicate' AND Ticket_Id = ti.ticket_id)) AS dups
	OUTER APPLY (
		SELECT  TOP 1 t.Id, t.Name
		FROM	DXStatisticsV2.dbo.TribeTeamMapping AS ttm
				INNER JOIN CRM.dbo.Tribes AS t ON t.Id = ttm.Tribe
		WHERE   ttm.SupportTeam = ti.support_team 
		ORDER BY t.Name ) AS tribes
	LEFT JOIN ticket_tags AS tt ON tt.ticket_id = ti.ticket_id