DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date DATE = '{end_date}';


WITH tickets_with_iterations AS (
	SELECT
		TicketId AS id,
		COUNT(TicketId) AS iterations
	FROM  DXStatisticsV2.dbo.IterationItems AS ii
	WHERE DateStart BETWEEN @start_date AND @end_date
	GROUP BY TicketId
)

SELECT
	u.FriendlyId				AS {friendly_id},
	tribes.Id					AS {tribe_id},
	tribes.Name					AS {tribe_name},
	ti.TicketSCID				AS {ticket_scid},
	ti.TicketType				AS {ticket_type},
	CAST(ti.Created AS DATE)	AS {creation_date},
	ii.iterations				AS {iterations}
FROM 
	DXStatisticsV2.dbo.TicketInfos AS ti
	INNER JOIN tickets_with_iterations AS ii ON ii.Id = ti.Id
	INNER JOIN DXStatisticsV2.dbo.Users AS u ON u.Id = ti.OwnerGuid
	LEFT JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = ISNULL(ti.ProcessingSupportTeam, ti.SupportTeam)
	INNER JOIN CRM.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id

	-- should be generated and inserted --
	INNER JOIN (SELECT DISTINCT Customer_Id AS crmid
				FROM CRM.dbo.Customer_UserGroup 
				WHERE UserGroup_Id IN (
						'CFAD19C6-B8BD-48AD-B934-9DF15E35DD5F', --Support | MAU | Sent to Ray
						'55749CB5-062C-409A-9482-F403FD80D750', --Support | Expired Licenses | Sent to Ray
						'47D9152B-9E5C-46A3-B90E-B8F6BB826D8F', --Support | MAU | Confirmed
						'68B232E2-79D6-48B4-B307-2CA2D8BC9874'	--Support | MAU | Under Review
					)) AS uig ON uig.crmid = u.CRMid
	
	-- should be generated and inserted --
	INNER JOIN (
		SELECT DISTINCT Tickets AS ticket_id
		FROM [DXStatisticsV2].[dbo].[TicketTags] AS tt
		WHERE tt.Tags IN (30, 50, 59)
	) AS tt ON tt.ticket_id = ti.Id

ORDER BY
	{friendly_id},
	{creation_date}

-- #TicketType# --
-- 3 -- suggestion 
-- 6 -- breaking change
-- 7 -- License Status Clarification
-- 1 -- question
-- 4 -- KB
-- 5 -- example
-- 122 -- internal ticket request
-- 2 -- bug report
-- 11 -- redirect
-- 8 -- Security advisory