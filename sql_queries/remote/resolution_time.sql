DECLARE @start		DATE = DATEADD({years_of_history}, CONVERT(DATE, GETUTCDATE()))
DECLARE @end		DATE = CONVERT(DATE, GETUTCDATE())

SELECT	tickets.FriendlyId									AS {ticket_scid},
        CAST(tickets.Created AS DATE)						AS {creation_date},
		DATEDIFF(HOUR, tickets.Created, closed.timestamp)	AS {resolution_in_hours}
FROM   	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets AS tickets
		OUTER APPLY (
				SELECT	 TOP 1 EntityModified AS timestamp
				FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
				WHERE	 Ticket_Id = tickets.Id AND Name = 'TicketStatus' AND Value = 'Closed'
				ORDER BY EntityModified DESC
		) AS closed
WHERE 	Created BETWEEN @start AND @end
	AND closed.timestamp IS NOT NULL
