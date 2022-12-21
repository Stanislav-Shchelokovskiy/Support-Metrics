SELECT
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )                           AS {period},
    COUNT(DISTINCT {user_id})   AS {people},
    COUNT({scid})               AS {tickets},
    SUM({iterations})           AS {iterations}
FROM 
    {table_name}
WHERE
    {creation_date} BETWEEN '{range_start}' AND '{range_end}'
    {tribes_fitler}
    {customer_groups_filter}
    {ticket_types_filter}
    {ticket_tags_filter}
    {reply_types_filter}
    {components_filter}
    {features_filter}
    {license_status_filter}
    {conversion_status_filter}
GROUP BY
    IIF(
        '{group_by_period}' = '%Y-%W', 
        STRFTIME('%Y-%m-%d', {creation_date}, 'weekday 0', '-6 day'), 
        STRFTIME('{group_by_period}', {creation_date})
    )