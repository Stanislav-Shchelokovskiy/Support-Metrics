SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

DECLARE @start_date DATE = '{start_date}'
DECLARE @end_date   DATE = '{end_date}'

DECLARE @no_line		TINYINT = 2

SELECT DISTINCT
	ticket_id		AS {ticket_id},
	post_id			AS {post_id},
	user_crmid		AS {crmid},
	user_id			AS {scid},
	user_tribe_id	AS {tribe_id},
	user_tent_id	AS {tent_id},
	position_id		AS {position_id},
	user_name		AS {name},
	position_name	AS {position_name},
	user_tribe_name	AS {tribe_name},
	user_tent_name	AS {tent_name}
FROM DXStatisticsV2.dbo.get_tribe_replies(@start_date, @end_date, DEFAULT) AS tr
WHERE tr.line != @no_line