SELECT
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )                               AS {period},
    COUNT(DISTINCT {user_id})       AS {people},
    COUNT(DISTINCT {ticket_scid})   AS {tickets},
    COUNT({emp_post_id})            AS {iterations}
FROM {tickets_with_iterations_table}
WHERE
    {creation_date_filter}
    {tribes_filter}
    {positions_filter}
    {emp_tribes_filter}
    {emps_filter}
    {customer_groups_filter}
    {ticket_types_filter}
    {ticket_tags_filter}
    {reply_types_filter}
    {components_filter}
    {features_filter}
    {license_status_filter}
    {conversion_status_filter}
    {platforms_filter}
    {products_filter}
GROUP BY
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )