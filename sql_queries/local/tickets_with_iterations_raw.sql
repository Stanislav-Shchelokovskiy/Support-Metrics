SELECT
    {tbl_alias}.{user_id},
    {tbl_alias}.{is_employee},
    {tbl_alias}.{ticket_scid},
    ( SELECT CASE WHEN AVG(rating) < -0.3 THEN -1
                  WHEN AVG(rating) > 0.3  THEN 1
                  WHEN AVG(rating) BETWEEN -0.3 AND 0.3 THEN 0
                  ELSE NULL END
      FROM   {csi_table}
      WHERE  ticket_scid = {tbl_alias}.{ticket_scid} 
      LIMIT 1 ) AS {csi},
    ( SELECT name 
      FROM   {tickets_types_table}
      WHERE  id = {tbl_alias}.ticket_type
      LIMIT 1 )  AS {ticket_type},
    {tbl_alias}.{tribes_names},
    {tbl_alias}.{tent_name},
    ( SELECT GROUP_CONCAT(platform_name, '; ')
      FROM (SELECT DISTINCT platform_name
            FROM {platforms_products_table}
            WHERE platform_id IN (SELECT value FROM JSON_EACH('["' || replace({tbl_alias}.platforms, ';', '", "') || '"]')))) AS {platforms},
    ( SELECT GROUP_CONCAT(product_name, '; ')
      FROM (SELECT DISTINCT product_name 
            FROM {platforms_products_table}
            WHERE product_id IN (SELECT value FROM JSON_EACH('["' || replace({tbl_alias}.products, ';', '", "') || '"]')))) AS {products},
    ( SELECT GROUP_CONCAT(name, '; ')
      FROM (SELECT name
            FROM {tickets_tags_table}
            WHERE id IN (SELECT value FROM JSON_EACH('["' || replace({tbl_alias}.ticket_tags, ';', '", "') || '"]')))) AS {ticket_tags},
    {tbl_alias}.{is_private},
    {tbl_alias}.{creation_date},
    {tbl_alias}.license_name AS {license_name},
    {tbl_alias}.parent_license_name AS {parent_license_name},
    {tbl_alias}.{subscription_start},
    {tbl_alias}.{expiration_date},
    ( SELECT name 
      FROM   {license_statuses_table}
      WHERE  id = {tbl_alias}.license_status
      LIMIT 1 )  AS {license_status},
    ( SELECT name 
      FROM   {conversion_statuses_table}
      WHERE  id = {tbl_alias}.conversion_status
      LIMIT 1 ) AS {conversion_status},
    ( SELECT name 
      FROM   {replies_types_table}
      WHERE  id = {tbl_alias}.reply_id
      LIMIT 1 ) AS {reply},
    ( SELECT component_name 
      FROM   {components_features_table}
      WHERE  component_id = {tbl_alias}.component_id
      LIMIT 1 ) AS {component},
    ( SELECT feature_name 
      FROM   {components_features_table}
      WHERE  feature_id = {tbl_alias}.feature_id
      LIMIT 1 ) AS {feature},
    {tbl_alias}.{builds},
    {tbl_alias}.{fixed_in_builds},
    ( SELECT name 
      FROM   {employees_table}
      WHERE  scid = {tbl_alias}.fixed_by
      LIMIT 1 )  AS {fixed_by},
    {tbl_alias}.{fixed_on},
    {tbl_alias}.{ticket_status},
    ( SELECT name 
      FROM   {employees_table}
      WHERE  scid = {tbl_alias}.closed_by
      LIMIT 1 )  AS {closed_by},
    {tbl_alias}.{closed_on},
    {tbl_alias}.{resolution_in_hours},
    ( SELECT name 
      FROM   {severity_table}
      WHERE  id = {tbl_alias}.severity
      LIMIT 1 )  AS {severity},
    {tbl_alias}.{converted_to_bug_on},
    ( SELECT name 
      FROM   {tickets_types_table}
      WHERE  id = {tbl_alias}.duplicated_to_ticket_type
      LIMIT 1 )  AS {duplicated_to_ticket_type},
    {tbl_alias}.{duplicated_to_ticket_scid},
    ( SELECT name 
      FROM   {employees_table}
      WHERE  scid = {tbl_alias}.assigned_to
      LIMIT 1 )  AS {assigned_to},
     ( SELECT name 
      FROM   {operating_systems_table}
      WHERE  id = {tbl_alias}.operating_system_id
      LIMIT 1 )  AS {operating_system},
    ( SELECT name 
      FROM   {ides_table}
      WHERE  id = {tbl_alias}.ide_id
      LIMIT 1 )  AS {ide},
    {tbl_alias}.{emp_post_id},
    {tbl_alias}.{emp_name},
    {tbl_alias}.{emp_position_name},
    {tbl_alias}.{emp_tribe_name},
    {tbl_alias}.{emp_tent_name},
    ( SELECT GROUP_CONCAT(name, '; ')
      FROM (SELECT DISTINCT name
            FROM {roles_table}
            WHERE id IN (SELECT value FROM JSON_EACH('["' || replace({tbl_alias}.{roles}, ';', '", "') || '"]')))) AS {roles}{baseline_aligned_mode_fields}
FROM {tickets_with_iterations_table}