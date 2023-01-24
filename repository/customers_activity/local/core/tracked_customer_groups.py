from sql_queries.customers_activity.meta import TicketsWithIterationsMeta, TrackedCustomersGroupsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator


def get_tracked_customers_groups_query(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    return f"""
    (   SELECT  {TicketsWithIterationsMeta.user_id},
                {TicketsWithIterationsMeta.ticket_scid},
                {TicketsWithIterationsMeta.creation_date} AS original_{TicketsWithIterationsMeta.creation_date},
                DATE({TicketsWithIterationsMeta.creation_date}, '-'||offest_in_days||' DAYS') AS {TicketsWithIterationsMeta.creation_date},
                {TicketsWithIterationsMeta.tribe_id},
                {TicketsWithIterationsMeta.tribe_name},
                {TicketsWithIterationsMeta.user_groups},
                {TicketsWithIterationsMeta.ticket_type},
                {TicketsWithIterationsMeta.ticket_tags},
                {TicketsWithIterationsMeta.reply_id},
                {TicketsWithIterationsMeta.component_id},
                {TicketsWithIterationsMeta.feature_id},
                {TicketsWithIterationsMeta.license_status},
                {TicketsWithIterationsMeta.conversion_status},
                {TicketsWithIterationsMeta.platforms},
                {TicketsWithIterationsMeta.products},
                {TicketsWithIterationsMeta.emp_post_id},
                {TicketsWithIterationsMeta.emp_name},
                {TicketsWithIterationsMeta.emp_position_name},
                {TicketsWithIterationsMeta.emp_tribe_name},
                {TicketsWithIterationsMeta.emp_position_id},
                {TicketsWithIterationsMeta.emp_tribe_id},
                {TicketsWithIterationsMeta.emp_crmid}
        FROM    {CustomersActivityDBIndex.get_tickets_with_iterations_name()} AS twi
        INNER JOIN (
            SELECT  {TrackedCustomersGroupsMeta.user_crmid}, 
                    {TrackedCustomersGroupsMeta.assignment_date}, 
                    {TrackedCustomersGroupsMeta.removal_date},
                    CAST(JULIANDAY(MIN({TrackedCustomersGroupsMeta.assignment_date}) OVER (PARTITION BY {TrackedCustomersGroupsMeta.user_crmid}, {TrackedCustomersGroupsMeta.id}))
                        -JULIANDAY(MIN({TrackedCustomersGroupsMeta.assignment_date}) OVER (PARTITION BY {TrackedCustomersGroupsMeta.id})) AS INTEGER) AS offest_in_days
            FROM    {CustomersActivityDBIndex.get_tracked_customers_groups_name()}
            WHERE   {TrackedCustomersGroupsMeta.assignment_date} BETWEEN '{kwargs['range_start']}' AND '{kwargs['range_end']}'
                    {filter_generator.generate_customer_groups_filter(
                        params=kwargs['customers_groups'],
                        col=TrackedCustomersGroupsMeta.id
                    )}
        ) AS tcg ON tcg.user_crmid = twi.user_crmid
        WHERE {TicketsWithIterationsMeta.creation_date} BETWEEN {TrackedCustomersGroupsMeta.assignment_date} AND {TrackedCustomersGroupsMeta.removal_date}
    )"""
