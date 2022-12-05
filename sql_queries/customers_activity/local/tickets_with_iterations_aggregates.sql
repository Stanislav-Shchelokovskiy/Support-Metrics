SELECT
    STRFTIME('{group_by_period}', {creation_date}) AS {period},
    COUNT({scid}) AS {tickets},
    SUM({iterations}) AS {iterations}
FROM 
    {table_name}
WHERE
    {creation_date} BETWEEN '{range_start}' AND '{range_end}'
    {customer_groups_filter}
    {ticket_types_filter}
    {ticket_tags_filter}
    {tribes_fitler}
    {reply_types_filter}
GROUP BY
    STRFTIME('{group_by_period}', {creation_date})