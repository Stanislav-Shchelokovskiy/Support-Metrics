DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date DATE = '{end_date}';


WITH ticket_tags AS (
	SELECT
		Tickets AS tickets,
		STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), ' ') AS tags
	FROM
		SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags
	GROUP BY
		Tickets
)

SELECT
	u.FriendlyId				AS {user_id},
	tribes.Id					AS {tribe_id},
	ti.TicketSCID				AS {scid},
	ti.TicketType				AS {ticket_type},
	CAST(ti.Created AS DATE)	AS {creation_date},
	ii.iterations				AS {iterations},
	ug.groups					AS {user_groups},
	tt.tags						AS {ticket_tags},
	CAST(cat.ReplyId	AS UNIQUEIDENTIFIER) AS {reply_id},
	CAST(cat.ControlId	AS UNIQUEIDENTIFIER) AS {control_id},
	CAST(cat.FeatureId	AS UNIQUEIDENTIFIER) AS {feature_id}
FROM 
	(SELECT *
	 FROM 	DXStatisticsV2.dbo.TicketInfos
	 WHERE 	Created BETWEEN @start_date AND @end_date ) AS ti
	OUTER APPLY (
		SELECT 	COUNT(TicketId) AS iterations
		FROM  	DXStatisticsV2.dbo.IterationItems AS ii
		WHERE 	TicketId = ti.Id ) AS ii
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
	INNER JOIN SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Users AS u ON u.Id = ti.OwnerGuid
	INNER JOIN CRM.dbo.Customers AS crmCustomer ON crmCustomer.FriendlyId = u.FriendlyId
	OUTER APPLY(
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') AS groups
		FROM 	CRM.dbo.Customer_UserGroup
		WHERE 	Customer_Id = crmCustomer.Id ) AS ug
	LEFT JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = ISNULL(ti.ProcessingSupportTeam, ti.SupportTeam)
	INNER JOIN CRM.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id
	LEFT JOIN ticket_tags AS tt ON tt.tickets = ti.Id