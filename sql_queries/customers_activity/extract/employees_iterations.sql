SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date   DATE = '{end_date}'

DECLARE @note			TINYINT = 3
DECLARE @description	TINYINT = 0

SELECT
	ii.TicketId		AS {ticket_id},
	ii.PostId		AS {post_id},
	e.crmid			AS {crmid},
	e.tribe_id		AS {tribe_id},
	e.position_id	AS {position_id},
	e.name			AS {name},
	e.position_name AS {position_name},
	e.tribe_name	AS {tribe_name}
FROM ( SELECT 	TicketId, PostId
	   FROM  	DXStatisticsV2.dbo.IterationItems AS ii
	   WHERE 	DateStart BETWEEN @start_date AND @end_date ) AS ii
	 CROSS APPLY ( SELECT Id, Owner
				   FROM   DXStatisticsV2.dbo.Posts
				   WHERE  Created BETWEEN @start_date AND @end_date AND 
						  Id = ii.PostId AND
						  Type NOT IN (@note, @description)) AS p
	 CROSS APPLY ( SELECT *
				   FROM   DXStatisticsV2.dbo.support_analytics_employees()
				   WHERE  scid = p.Owner) AS e