DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date DATE = '{end_date}';


WITH tickets_with_iterations AS (
	SELECT
		TicketId AS id,
		COUNT(TicketId) AS iterations
	FROM  DXStatisticsV2.dbo.IterationItems AS ii
	WHERE DateStart BETWEEN @start_date AND @end_date
	GROUP BY TicketId
),

user_groups AS (
	SELECT
		Customer_Id AS crmid,
		STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') AS groups
	FROM 
		CRM.dbo.Customer_UserGroup
	GROUP BY 
		Customer_Id
),

ticket_tags AS (
	SELECT
		Tickets AS ticket_id,
		STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), ' ') AS tags
	FROM 
		[DXStatisticsV2].[dbo].[TicketTags] AS tt
	GROUP BY
		Tickets
)

	SELECT
		u.FriendlyId				AS {user_id},
		tribes.Id					AS {tribe_id},
		tribes.Name					AS {tribe_name},
		ti.TicketSCID				AS {scid},
		ti.TicketType				AS {ticket_type},
		CAST(ti.Created AS DATE)	AS {creation_date},
		ii.iterations				AS {iterations},
		ug.groups					AS {user_groups},
		tt.tags						AS {ticket_tags}
	FROM 
		DXStatisticsV2.dbo.TicketInfos AS ti
		INNER JOIN tickets_with_iterations AS ii ON ii.Id = ti.Id
		INNER JOIN DXStatisticsV2.dbo.Users AS u ON u.Id = ti.OwnerGuid
		LEFT JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = ISNULL(ti.ProcessingSupportTeam, ti.SupportTeam)
		INNER JOIN CRM.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id
		LEFT JOIN user_groups AS ug ON ug.crmid = u.CRMid
		LEFT JOIN ticket_tags AS tt ON tt.ticket_id = ti.Id
	WHERE
		ti.Created BETWEEN @start_date AND @end_date