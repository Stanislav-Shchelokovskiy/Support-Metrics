SELECT *
FROM {table_name}
WHERE
    {creation_date} BETWEEN '{range_start}' AND '{range_end}'
    {customer_groups_filter}
    {ticket_types_filter}
    {ticket_tags_filter}
    {tribes_fitler}
    {reply_types_filter}
    {controls_filter}
    {features_filter}