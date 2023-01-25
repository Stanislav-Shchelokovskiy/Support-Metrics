DROP TABLE IF EXISTS {TicketsWithIterations};
CREATE TABLE {TicketsWithIterations} AS
SELECT
    t.{user_crmid},
    t.{user_id},
    t.{tribe_id},
    t.{tribe_name},
    t.{ticket_scid},
    t.{ticket_type},
    t.{creation_date},
    t.{user_groups},
    t.{ticket_tags},
    t.{platforms},
    t.{products},
    t.{reply_id},
    t.{component_id},
    t.{feature_id},
    t.{license_status},
    t.{conversion_status},
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
        SELECT  DISTINCT {user_crmid} 
        FROM    {CustomersTickets} 
        WHERE   {creation_date} >= (SELECT DATE(MIN({creation_date}), '+{rank_period_offset}') FROM {CustomersTickets}) 
    ) AS actual_t ON actual_t.{user_crmid} = t.{user_crmid}
    LEFT JOIN {EmployeesIterations} AS ei ON ei.{ticket_id} = t.{ticket_id};


CREATE INDEX idx_{TicketsWithIterations}_inner ON CustomersActivity_TicketsWithIterations(
    {user_crmid}, 
    {emp_post_id},
    {creation_date},
    {tribe_id},
    {ticket_type},
    {license_status},
    {emp_position_id}
);

CREATE INDEX idx_{TicketsWithIterations}_outer ON CustomersActivity_TicketsWithIterations(
    {user_crmid},
    {creation_date},
    {user_id},
    {ticket_scid},
    {emp_post_id}
);
