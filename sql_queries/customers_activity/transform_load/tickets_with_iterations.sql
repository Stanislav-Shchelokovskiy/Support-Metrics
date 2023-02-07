DROP TABLE IF EXISTS {TicketsWithIterations};
CREATE TABLE {TicketsWithIterations} AS
SELECT
    t.{user_crmid},
    t.{user_id},
    t.{tribe_id},
    t.{tribe_name},
    t.{ticket_id},
    t.{ticket_scid},
    t.{ticket_type},
    t.{creation_date},
    t.{is_private},
    t.{user_groups},
    t.{ticket_tags},
    t.{platforms},
    t.{products},
    t.{specifics},
    t.{builds},
    t.{fixed_in_builds},
    t.{fixed_by},
    t.{fixed_on},
    t.{ticket_status},
    t.{closed_by},
    t.{closed_on},
    t.{severity},
    t.{license_status},
    CAST(t.{conversion_status} AS INT)         AS {conversion_status},
    CAST(t.{duplicated_to_ticket_type} AS INT) AS {duplicated_to_ticket_type},
    t.{duplicated_to_ticket_scid},
    t.{operating_system_id},
    t.{ide_id},
    t.{reply_id},
    t.{component_id},
    t.{feature_id},
    ei.{post_id}       AS {emp_post_id},
    ei.{crmid}         AS {emp_crmid},
    ei.{tribe_id}      AS {emp_tribe_id},
    ei.{position_id}   AS {emp_position_id},
    ei.{name}          AS {emp_name},
    ei.{position_name} AS {emp_position_name},
    ei.{tribe_name}    AS {emp_tribe_name}
FROM
    {CustomersTickets} AS t
    INNER JOIN (
        SELECT   {user_crmid} 
        FROM     {CustomersTickets}
        WHERE    {creation_date} >= (SELECT DATE(MIN({creation_date}), '+{rank_period_offset}') FROM {CustomersTickets})
        GROUP BY {user_crmid}
    ) AS actual_t ON actual_t.{user_crmid} = t.{user_crmid}
    LEFT JOIN {EmployeesIterations} AS ei ON ei.{ticket_id} = t.{ticket_id};


CREATE INDEX idx_{TicketsWithIterations}_tickets_inner ON {TicketsWithIterations}(
    {user_crmid}, 
    {ticket_scid},
    {creation_date},
    {tribe_id},
    {ticket_type},
    {license_status},
    {emp_position_id}
);

CREATE INDEX idx_{TicketsWithIterations}_iterations_inner ON {TicketsWithIterations}(
    {user_crmid}, 
    {emp_post_id},
    {creation_date},
    {tribe_id},
    {ticket_type},
    {license_status},
    {emp_position_id}
);

CREATE INDEX idx_{TicketsWithIterations}_outer ON {TicketsWithIterations}(
    {user_crmid},
    {creation_date},
    {tribe_id},
    {user_id},
    {ticket_scid},
    {emp_post_id}
);
