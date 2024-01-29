DECLARE @start		DATE = DATEADD({years_of_history}, CONVERT(DATE, GETUTCDATE()))
DECLARE @end		DATE = CONVERT(DATE, GETUTCDATE())
DECLARE @employees 	VARCHAR(MAX) = N'{employees_json}'

DECLARE @bug       	TINYINT = 2;

SELECT	ticket_scid														AS {ticket_scid},
		SUM(DATEDIFF(MINUTE, iteration_start, iteration_end)) / 60		AS {resolution_in_hours},
		DATEDIFF(MINUTE, MIN(iteration_start), MAX(iteration_end)) / 60	AS {lifetime_in_hours}
FROM    DXStatisticsV2.dbo.get_iterations(@start, @end, @employees) AS e
WHERE	ticket_type != @bug
GROUP BY ticket_scid
UNION
SELECT	tickets.FriendlyId,
		DATEDIFF(HOUR, tickets.Created, ISNULL(fixed_info.fixed_on, closed_info.closed_on)),
		DATEDIFF(HOUR, tickets.Created, ISNULL(fixed_info.fixed_on, closed_info.closed_on))
FROM   	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets AS tickets
		OUTER APPLY (
			SELECT	 TOP 1 AuditOwner AS closed_by, EntityModified AS closed_on
			FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
			WHERE	 Ticket_Id = tickets.Id AND Name = 'TicketStatus' AND Value = 'Closed'
			ORDER BY EntityModified DESC
		) AS closed_info
		OUTER APPLY (
			SELECT	 TOP 1 AuditOwner AS fixed_by, EntityModified AS fixed_on
			FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
			WHERE	 Ticket_Id = tickets.Id AND Name = 'FixedInBuild'
			ORDER BY EntityModified DESC
		) AS fixed_info
WHERE 	Created BETWEEN @start AND @end
	AND EntityType = @bug
	AND (closed_info.closed_on IS NOT NULL OR fixed_info.fixed_on IS NOT NULL)
