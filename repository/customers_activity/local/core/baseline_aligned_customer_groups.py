from sql_queries.customers_activity.meta import TicketsWithIterationsMeta, BaselineAlignedCustomersGroupsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.core.filters import build_filter_string


def get_baseline_aligned_mode_query(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    return f"""(SELECT {get_common_select_fields()}
        {TicketsWithIterationsMeta.creation_date} AS original_{TicketsWithIterationsMeta.creation_date},
        DATE({TicketsWithIterationsMeta.creation_date}, '-'||offest_in_days||' DAYS') AS {TicketsWithIterationsMeta.creation_date}
FROM    {CustomersActivityDBIndex.get_tickets_with_iterations_name()} AS twi
INNER JOIN (
    SELECT  {BaselineAlignedCustomersGroupsMeta.user_crmid},
            {BaselineAlignedCustomersGroupsMeta.assignment_date},
            {BaselineAlignedCustomersGroupsMeta.removal_date},
            CAST(JULIANDAY({BaselineAlignedCustomersGroupsMeta.assignment_date})-JULIANDAY('{kwargs['range_start']}') AS INTEGER) AS offest_in_days
    FROM    {CustomersActivityDBIndex.get_tracked_customers_groups_name()}
    WHERE   {build_filter_string([
                f"{BaselineAlignedCustomersGroupsMeta.assignment_date} BETWEEN '{kwargs['range_start']}' AND '{kwargs['range_end']}'",
                filter_generator.generate_customer_groups_filter(params=kwargs['customers_groups'], col=BaselineAlignedCustomersGroupsMeta.id)
            ])}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE creation_date BETWEEN {BaselineAlignedCustomersGroupsMeta.assignment_date} AND {BaselineAlignedCustomersGroupsMeta.removal_date}
UNION ALL
SELECT  {get_common_select_fields()}
        {TicketsWithIterationsMeta.creation_date} AS original_{TicketsWithIterationsMeta.creation_date},
        {TicketsWithIterationsMeta.creation_date} AS {TicketsWithIterationsMeta.creation_date}
FROM    {CustomersActivityDBIndex.get_tickets_with_iterations_name()} AS twi
LEFT JOIN (
    SELECT  {BaselineAlignedCustomersGroupsMeta.user_crmid}
    FROM    {CustomersActivityDBIndex.get_tracked_customers_groups_name()}
    WHERE   {build_filter_string([
                f"{BaselineAlignedCustomersGroupsMeta.assignment_date} BETWEEN '{kwargs['range_start']}' AND '{kwargs['range_end']}'",
                filter_generator.generate_customer_groups_filter(params=kwargs['customers_groups'], col=BaselineAlignedCustomersGroupsMeta.id)
            ])}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE {build_filter_string([
            'tcg.user_crmid IS NULL',
            filter_generator.generate_customer_groups_filter(params=kwargs['customers_groups'], col=TicketsWithIterationsMeta.user_groups)
        ])}
)"""


def get_common_select_fields() -> str:
    return f"""
        {TicketsWithIterationsMeta.user_id},
        {TicketsWithIterationsMeta.ticket_scid},
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
        {TicketsWithIterationsMeta.emp_crmid},"""
