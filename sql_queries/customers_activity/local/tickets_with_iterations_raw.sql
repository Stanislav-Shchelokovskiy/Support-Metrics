SELECT
    t.{user_id},
    t.{scid},
    t.{tribe_name},
    t.{iterations},
    t.{creation_date},
    r.Name AS {reply},
    c.component_name AS {component},
    f.feature_name AS {feature}
FROM (  SELECT
            user_id,
            scid,
            tribe_name,
            iterations,
            creation_date,
            reply_id,
            component_id,
            feature_id
        FROM
            {table_name} 
        WHERE
            {creation_date} BETWEEN '{range_start}' AND '{range_end}'
            {customer_groups_filter}
            {ticket_types_filter}
            {ticket_tags_filter}
            {tribes_fitler}
            {reply_types_filter}
            {components_filter}
            {features_filter}
    ) AS t
    LEFT JOIN {replies_types_table} AS r ON r.id = t.reply_id
    LEFT JOIN {components_features_table} AS c ON c.component_id = t.component_id
    LEFT JOIN {components_features_table} AS f ON f.feature_id = t.feature_id