SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

DECLARE @employees VARCHAR(MAX) = N'{employees_json}'
DECLARE @start DATE = '{start_date}'
DECLARE @end   DATE = '{end_date}'

DECLARE @no_line		TINYINT = 2

SELECT DISTINCT
	ticket_id		AS {ticket_id},
	post_id			AS {post_id},
	emp_crmid		AS {crmid},
	emp_scid		AS {scid},
	emp_tribe_id	AS {tribe_id},
	emp_tent_id		AS {tent_id},
	position_id		AS {position_id},
	emp_name		AS {name},
	position_name	AS {position_name},
	emp_tribe_name	AS {tribe_name},
	emp_tent_name	AS {tent_name}
FROM DXStatisticsV2.dbo.get_replies(@start, @end, @employees, DEFAULT, DEFAULT) AS tr
WHERE tr.line != @no_line
