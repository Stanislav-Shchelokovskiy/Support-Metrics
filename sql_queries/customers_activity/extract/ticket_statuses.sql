DECLARE @status_id TINYINT = 6  
SELECT
    Value AS {id},
    DisplayText AS {name}
FROM SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketFieldValues
WHERE TicketField_Id = @status_id