SELECT
    {group_by_period}               AS {period},
    COUNT(DISTINCT {user_id})       AS {people},
    COUNT(DISTINCT {ticket_scid})   AS {tickets},
    COUNT({emp_post_id})            AS {iterations}
FROM 
    {tickets_with_iterations_table}
WHERE
    {tickets_filter}
GROUP BY {group_by_period}
ORDER BY {period}