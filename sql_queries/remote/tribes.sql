SELECT 
	tribe_id   AS {id},
	tribe_name AS {name}
FROM  DXStatisticsV2.dbo.get_available_tribes()
ORDER BY {name}