SELECT
    t.{user_id},
    t.{scid},
    t.{tribe_name},
    t.{iterations},
    t.{creation_date},
    t.{license_status},
    r.name AS {reply},
    ( SELECT component_name 
      FROM {components_features_table}
      WHERE tribe_id = t.tribe_id AND 
            component_id = t.component_id
      LIMIT 1 ) AS {component},
    ( SELECT feature_name 
      FROM {components_features_table}
      WHERE tribe_id = t.tribe_id AND
            component_id = t.component_id AND
            feature_id = t.feature_id
      LIMIT 1 ) AS {feature}
FROM (  SELECT  *
        FROM    {table_name} 
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