SELECT
    t.{user_id},
    t.{ticket_scid},
    t.{tribe_name},
    t.{iterations},
    t.{creation_date},
    ( SELECT name 
      FROM   {license_statuses_table}
      WHERE  id = t.license_status
      LIMIT 1 )  AS {license_status},
    ( SELECT name 
      FROM   {conversion_statuses_table}
      WHERE  id = t.conversion_status
      LIMIT 1 ) AS {conversion_status},
    ( SELECT name 
      FROM   {replies_types_table}
      WHERE  id = t.reply_id
      LIMIT 1 ) AS {reply},
    ( SELECT component_name 
      FROM   {components_features_table}
      WHERE  tribe_id = t.tribe_id AND 
             component_id = t.component_id
      LIMIT 1 ) AS {component},
    ( SELECT feature_name 
      FROM   {components_features_table}
      WHERE  tribe_id = t.tribe_id AND
             component_id = t.component_id AND
             feature_id = t.feature_id
      LIMIT 1 ) AS {feature}
FROM {table_name} AS t
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
      {platforms_filter}
      {products_filter}