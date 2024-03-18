SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

DECLARE @employees VARCHAR(MAX) = N'{employees_json}'
DECLARE @start DATE = '{start_date}'
DECLARE @end   DATE = '{end_date}'

DECLARE @no_line		TINYINT = 2;

WITH replies AS (
	SELECT DISTINCT
		reply_timestamp AS reply_timestamp,
        LEAD(reply_timestamp, 1, '3000-01-01') OVER (PARTITION BY ticket_id ORDER BY reply_timestamp ASC) AS next_reply_timestamp,
		ticket_id,
		post_id,
		emp_crmid,
		emp_scid,
		emp_tribe_id,
		emp_tent_id,
		position_id,
		emp_name,
		position_name,
		emp_tribe_name,
		emp_tent_name,
		roles
	FROM DXStatisticsV2.dbo.get_replies(@start, @end, @employees, DEFAULT, DEFAULT) AS tr
	WHERE tr.line != @no_line
)

SELECT 	r.ticket_id			AS {ticket_id},
		r.post_id			AS {post_id},
		r.emp_crmid			AS {crmid},
		r.emp_scid			AS {scid},
		r.emp_tribe_id		AS {tribe_id},
		r.emp_tent_id		AS {tent_id},
		r.position_id		AS {position_id},
		r.emp_name			AS {name},
		r.position_name		AS {position_name},
		r.emp_tribe_name	AS {tribe_name},
		r.emp_tent_name		AS {tent_name},
		r.roles				AS {roles},
		audit_tp.*
FROM	replies AS r
		OUTER APPLY (
            SELECT  MIN([Tribe])            AS {post_tribe_id},
                    MIN([ProcessingTent])   AS {post_tent_id},
                    MIN([ReplyId])          AS {post_reply_id},
                    MIN([ControlId])        AS {post_component_id},
                    MIN([FeatureId])        AS {post_feature_id}
            FROM    (
                SELECT *
                FROM    (
                    SELECT  Name                                                                        AS name,
                            CAST(Value AS UNIQUEIDENTIFIER)                                             AS value,
                            EntityModified                                                              AS period_start,
                            LEAD(EntityModified) OVER (PARTITION BY Name ORDER BY EntityModified ASC)   AS period_end
                    FROM    scpaid_audit.[c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
                    WHERE	Ticket_Id = r.ticket_id
                        AND Name IN ('Tribe', 'ProcessingTent', 'ReplyId', 'ControlId', 'FeatureId')
                )AS au_inner
                WHERE   au_inner.period_start <= r.reply_timestamp 
                    AND (au_inner.period_end IS NULL OR au_inner.period_end < r.next_reply_timestamp)
            ) AS au
            PIVOT(MIN(value) FOR name IN ([Tribe], [ProcessingTent], [ReplyId], [ControlId], [FeatureId])) AS value
        ) AS audit_tp
