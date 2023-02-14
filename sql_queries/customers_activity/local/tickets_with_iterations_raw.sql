SELECT
    t.{user_id},
    t.{ticket_scid},
    t.{tribes_names},
    t.{creation_date},
    t.{license_name},
    t.{subscription_start},
    t.{expiration_date},
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
      WHERE  component_id = t.component_id
      LIMIT 1 ) AS {component},
    ( SELECT feature_name 
      FROM   {components_features_table}
      WHERE  feature_id = t.feature_id
      LIMIT 1 ) AS {feature},
    t.{emp_post_id},
    t.{emp_name},
    t.{emp_position_name},
    t.{emp_tribe_name}{baseline_aligned_mode_fields}
FROM ({tickets_with_iterations_table}) AS t
{tickets_filter}