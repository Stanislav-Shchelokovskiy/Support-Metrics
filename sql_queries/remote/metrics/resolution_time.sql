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
SELECT  tickets.FriendlyId,
        SUM(DATEDIFF(MINUTE, period_start, period_end)) / 60,
		DATEDIFF(MINUTE, MIN(period_start), MAX(period_end)) / 60
FROM    SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets AS tickets
    	OUTER APPLY (
			SELECT TOP 1 Modified AS happened_on
			FROM 	scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets
			WHERE 	AuditAction IN (0 /* Insert */, 1 /* Update */)
				AND EntityOid = tickets.Id
				AND	ChangedProperties LIKE '%EntityType%'
				AND	EntityType = @bug
			ORDER BY AuditAction DESC, happened_on DESC
		) AS conversion_to_bug
        CROSS APPLY (
            SELECT	EntityModified                                      AS period_start,
                    LEAD(EntityModified) OVER (ORDER BY EntityModified) AS period_end,
                    CAST(Value AS VARCHAR(20))                          AS status
            FROM	scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
            WHERE	Ticket_Id = tickets.Id
                AND Name = 'TicketStatus'
        ) AS au
WHERE   Created BETWEEN @start AND @end
	AND EntityType = @bug
    AND au.status = 'ActiveForDevelopers'
    AND au.period_start >= conversion_to_bug.happened_on
    AND au.period_end IS NOT NULL
GROUP BY FriendlyId
