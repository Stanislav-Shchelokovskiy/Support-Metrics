SELECT 
	CAST(Value AS UNIQUEIDENTIFIER) AS {id}, 
	MIN(DisplayValue)				AS {name}
FROM SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
WHERE Name = 'IDE'
GROUP BY Value