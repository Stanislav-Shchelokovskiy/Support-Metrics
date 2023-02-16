SELECT
    t.{user_id},
    t.{ticket_scid},
    ( SELECT name 
      FROM   {tickets_types_table}
      WHERE  id = t.ticket_type
      LIMIT 1 )  AS {ticket_type},
    t.{tribes_names},
    ( SELECT GROUP_CONCAT(platform_name, '; ')
      FROM (SELECT DISTINCT platform_name
            FROM {platforms_products_table}
            WHERE platform_id IN (SELECT value FROM JSON_EACH('["' || replace(t.platforms, ';', '", "') || '"]')))) AS {platforms},
    ( SELECT GROUP_CONCAT(product_name, '; ')
      FROM (SELECT DISTINCT product_name 
            FROM {platforms_products_table}
            WHERE product_id IN (SELECT value FROM JSON_EACH('["' || replace(t.products, ';', '", "') || '"]')))) AS {products},
    t.{is_private},
    t.{creation_date},
    t.license_name AS {license_name},
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
    t.{builds},
    t.{fixed_in_builds},
    ( SELECT name 
      FROM   {employees_table}
      WHERE  crmid = t.fixed_by
      LIMIT 1 )  AS {fixed_by},
    t.{fixed_on},
    t.{ticket_status},
    ( SELECT name 
      FROM   {employees_table}
      WHERE  crmid = t.closed_by
      LIMIT 1 )  AS {closed_by},
    t.{closed_on},
    ( SELECT name 
      FROM   {severity_table}
      WHERE  id = t.severity
      LIMIT 1 )  AS {severity},
    ( SELECT name 
      FROM   {tickets_types_table}
      WHERE  id = t.duplicated_to_ticket_type
      LIMIT 1 )  AS {duplicated_to_ticket_type},
    t.{duplicated_to_ticket_scid},
    ( SELECT name 
      FROM   {employees_table}
      WHERE  crmid = t.assigned_to
      LIMIT 1 )  AS {assigned_to},
     ( SELECT name 
      FROM   {operating_systems_table}
      WHERE  id = t.operating_system_id
      LIMIT 1 )  AS {operating_system},
    ( SELECT name 
      FROM   {ides_table}
      WHERE  id = t.ide_id
      LIMIT 1 )  AS {ide},
    t.{emp_post_id},
    t.{emp_name},
    t.{emp_position_name},
    t.{emp_tribe_name}{baseline_aligned_mode_fields}
FROM ({tickets_with_iterations_table}) AS t
{tickets_filter}