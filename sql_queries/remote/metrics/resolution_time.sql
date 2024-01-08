DECLARE @start		DATE = DATEADD({years_of_history}, CONVERT(DATE, GETUTCDATE()))
DECLARE @end		DATE = CONVERT(DATE, GETUTCDATE())
DECLARE @employees 	VARCHAR(MAX) = N'{employees_json}'

DECLARE @question  	TINYINT = 1
DECLARE @bug       	TINYINT = 2
DECLARE @suggestion	TINYINT = 3
DECLARE @note      	TINYINT = 3;

WITH posts AS (
	SELECT  tickets.FriendlyId		AS ticket_scid,
			posts.Id				AS post_id,
			posts.Created			AS post_created,
			tickets.is_ticket_owner	AS is_ticket_owner,
			employees.crmid			AS emp_crmid
	FROM (  SELECT	psts.Created, psts.Owner, psts.Ticket_Id, psts.Id
			FROM	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Posts AS psts
			/*      we offset start by a week in order to include iterations started erlier than @start.
					otherwise we miss such iterations. [1] */
			WHERE   psts.Created BETWEEN DATEADD(WEEK, -1 , @start) AND @end
					AND psts.Type  != @note
			) AS posts
			CROSS APPLY (
				SELECT  t.FriendlyId, CASE WHEN t.Owner = posts.Owner THEN 1 ELSE 0 END AS is_ticket_owner
				FROM    SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets AS t
				WHERE   t.Id = posts.Ticket_Id
					AND t.EntityType = @question
			) AS tickets
			OUTER APPLY (
					SELECT  e.crmid, e.is_service_user
					FROM    DXStatisticsV2.dbo.parse_employees(@employees) AS e
					WHERE   e.scid = posts.Owner
			) AS employees
	-- drop posts from service users
	WHERE employees.crmid IS NULL OR employees.is_service_user = 0
),

posts_with_prev_emp_crmid AS (
	SELECT  *, LAG(emp_crmid) OVER (PARTITION BY ticket_scid ORDER BY post_created) AS prev_emp_crmid
	FROM    posts
),

posts_split_into_iterations AS (
	SELECT  *, SUM(IIF(prev_emp_crmid IS NOT NULL AND emp_crmid IS NULL, 1, 0)) OVER (PARTITION BY ticket_scid ORDER BY post_created) AS iteration_no
	FROM posts_with_prev_emp_crmid
),

iterations_raw AS (
	SELECT  *,
			MIN(post_created) OVER (PARTITION BY ticket_scid, iteration_no) AS iteration_start,
			MAX(post_created) OVER (PARTITION BY ticket_scid, iteration_no) AS iteration_end,
			IIF(MIN(CASE WHEN emp_crmid IS NULL             THEN 0 ELSE 1 END) OVER (PARTITION BY ticket_scid, iteration_no) = 0 AND
					MAX(CASE WHEN emp_crmid IS NOT NULL THEN 1 ELSE 0 END) OVER (PARTITION BY ticket_scid, iteration_no) = 1,
					1, 0 ) AS is_iteration
	FROM    posts_split_into_iterations
),

iteration_lengths AS (
	SELECT  ticket_scid,
			emp_crmid,
			is_ticket_owner,
			iteration_no,
			iteration_start,
			iteration_end,
			DATEDIFF(MINUTE, iteration_start, iteration_end) AS iteration_len_in_minutes
	FROM    iterations_raw
	WHERE   is_iteration = 1
			AND emp_crmid IS NOT NULL
			AND is_ticket_owner = 0
			/* we restore previously extended period period here. see [1] above. */
			AND post_created >= @start
			/* Sequential answers are considered to be different iterations. ex T1161862, T1163662.
				This is because is_iteration is set to 1 from the very start to the very end of the iteration.
				We add additional conditions to recognize such cases and collapse them.*/
			AND post_created = iteration_end
)

SELECT  ticket_scid							AS {ticket_scid},
        SUM(iteration_len_in_minutes) / 60 	AS {resolution_in_hours}
FROM    iteration_lengths
GROUP BY ticket_scid
UNION
SELECT	tickets.FriendlyId,
		DATEDIFF(HOUR, tickets.Created, ISNULL(fixed_info.fixed_on, closed_info.closed_on))
FROM   	SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets AS tickets
		OUTER APPLY (
			SELECT	 TOP 1 AuditOwner AS closed_by, CAST(EntityModified AS DATE) AS closed_on
			FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
			WHERE	 Ticket_Id = tickets.Id AND Name = 'TicketStatus' AND Value = 'Closed'
			ORDER BY EntityModified DESC
		) AS closed_info
		OUTER APPLY (
			SELECT	 TOP 1 AuditOwner AS fixed_by, CAST(EntityModified AS DATE) AS fixed_on
			FROM	 scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
			WHERE	 Ticket_Id = tickets.Id AND Name = 'FixedInBuild'
			ORDER BY EntityModified DESC
		) AS fixed_info
WHERE 	Created BETWEEN @start AND @end
	AND EntityType = @bug
	AND (closed_info.closed_on IS NOT NULL OR fixed_info.fixed_on IS NOT NULL)
