DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date DATE = '{end_date}'

SELECT
	u.FriendlyId				AS {user_id},
	tribes.Id					AS {tribe_id},
	ti.TicketSCID				AS {scid},
	ti.TicketType				AS {ticket_type},
	CAST(ti.Created AS DATE)	AS {creation_date},
	ii.iterations				AS {iterations},
	ug.groups					AS {user_groups},
	tt.tags						AS {ticket_tags}
FROM 
	(SELECT *
	 FROM 	DXStatisticsV2.dbo.TicketInfos
	 WHERE 	Created BETWEEN @start_date AND @end_date ) AS ti
	CROSS APPLY (
		SELECT 	COUNT(TicketId) AS iterations
		FROM  	DXStatisticsV2.dbo.IterationItems AS ii
		WHERE 	TicketId = ti.Id ) AS ii
	INNER JOIN DXStatisticsV2.dbo.Users AS u ON u.Id = ti.OwnerGuid
	CROSS APPLY(
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), UserGroup_Id), ' ') AS groups
		FROM 	CRM.dbo.Customer_UserGroup
		WHERE 	Customer_Id = u.CRMid ) AS ug
	LEFT JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = ISNULL(ti.ProcessingSupportTeam, ti.SupportTeam)
	INNER JOIN CRM.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id
	OUTER APPLY(
		SELECT 	STRING_AGG(CONVERT(NVARCHAR(MAX), Tags), ' ') AS tags
		FROM 	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags
		WHERE 	Tickets = ti.Id ) AS tt