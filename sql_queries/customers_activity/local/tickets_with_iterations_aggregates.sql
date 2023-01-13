SELECT
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )                               AS {period},
    COUNT(DISTINCT {user_id})       AS {people},
    COUNT(DISTINCT {ticket_scid})   AS {tickets},
    COUNT({emp_post_id})            AS {iterations}
FROM 
    {tickets_with_iterations_table}
WHERE
    {tickets_filter}
GROUP BY
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )
ORDER BY {period}