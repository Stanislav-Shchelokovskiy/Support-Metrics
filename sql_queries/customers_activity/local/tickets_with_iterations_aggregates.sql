SELECT
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )                           AS {period},
    COUNT(DISTINCT {user_id})   AS {people},
    COUNT({ticket_scid})        AS {tickets},
    SUM({iterations})           AS {iterations}
FROM 
    {tickets_with_iterations_table} AS t
    INNER JOIN (
		SELECT {ticket_id}
		FROM {employees_iterations_table}
        {positions_filter} 
    ) AS ei ON ei.ticket_id = t.ticket_id
WHERE
    {creation_date} BETWEEN '{range_start}' AND '{range_end}'
    {tribes_filter}
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