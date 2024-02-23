DROP TABLE IF EXISTS {TicketsWithIterations};
CREATE TABLE {TicketsWithIterations} AS
SELECT
	t.{user_crmid},
	t.{user_id},
	t.{is_employee},
    t.{user_register_date},
	t.{tribes_ids},
	t.{tribes_names},
    t.{tent_id},
    t.{tent_name},
	t.{ticket_id},
	t.{ticket_scid},
	t.{ticket_type},
	t.{creation_date},
	t.{is_private},
	t.{user_groups},
	t.{ticket_tags},
	t.{platforms},
	t.{products},
	t.{frameworks},
	t.{builds},
	t.{fixed_in_builds},
	t.{fixed_by},
	t.{fixed_on},
	t.{ticket_status},
	t.{closed_by},
	t.{closed_on},
	rt.{resolution_in_hours},
	rt.{lifetime_in_hours},
    t.{converted_to_bug_on},
	t.{severity},
	CAST(t.{duplicated_to_ticket_type} AS INT) AS {duplicated_to_ticket_type},
	t.{duplicated_to_ticket_scid},
	t.{assigned_to},
	t.{operating_system_id},
	t.{ide_id},
	t.{reply_id},
	t.{component_id},
	t.{feature_id},
	t.{license_name},
    t.{parent_license_name},
	t.{subscription_start},
	t.{expiration_date},
	t.{license_status},
	CAST(t.{conversion_status} AS INT)	AS {conversion_status},
    IFNULL(ei.{post_id}, '00000000-0000-0000-0000-000000000000')	AS {emp_post_id},
    ei.{crmid}         												AS {emp_crmid},
    ei.{scid}          												AS {emp_scid},
    ei.{tribe_id}      												AS {emp_tribe_id},
    ei.{tent_id}       												AS {emp_tent_id},
    ei.{position_id}   												AS {emp_position_id},
    ei.{name}          												AS {emp_name},
    ei.{position_name} 												AS {emp_position_name},
    ei.{tribe_name}    												AS {emp_tribe_name},
    ei.{tent_name}     												AS {emp_tent_name},
	ei.{roles}     													AS {roles}
FROM
    {CustomersTickets} AS t
	-- This makes sense only when period is greater than 6 months.
	-- This code throws aways customers that wrote only during the rank_period_offset period.
    -- INNER JOIN (
    --     SELECT   {user_crmid} 
    --     FROM     {CustomersTickets}
    --     WHERE    {creation_date} >= (SELECT DATE(MIN({creation_date}), '+{rank_period_offset}') FROM {CustomersTickets})
    --     GROUP BY {user_crmid}
    -- ) AS actual_t ON actual_t.{user_crmid} = t.{user_crmid}
    LEFT JOIN {EmployeesIterations} AS ei ON ei.{ticket_id} = t.{ticket_id}
	LEFT JOIN {ResolutionTime} AS rt ON rt.{ticket_scid} = t.{ticket_scid};
