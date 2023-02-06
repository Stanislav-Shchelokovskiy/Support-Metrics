from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    BaselineAlignedModeMeta,
)
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.core.filters import build_filter_string


def get_baseline_aligned_mode_query(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    return f"""(SELECT {get_common_select_fields()}
        CAST(JULIANDAY(creation_date)-JULIANDAY('{kwargs['range_start']}')-baseline_aligned_offest_in_days AS INT) AS {BaselineAlignedModeMeta.days_since_baseline}
FROM    {CustomersActivityDBIndex.get_tickets_with_iterations_name()} AS twi
INNER JOIN (
    SELECT  {BaselineAlignedModeMeta.user_crmid},
            {BaselineAlignedModeMeta.assignment_date},
            {BaselineAlignedModeMeta.removal_date},
            CAST(JULIANDAY({BaselineAlignedModeMeta.assignment_date})-JULIANDAY('{kwargs['range_start']}') AS INTEGER) AS baseline_aligned_offest_in_days
    FROM    {CustomersActivityDBIndex.get_tracked_customers_groups_name()}
    WHERE   {build_filter_string([
                f"{BaselineAlignedModeMeta.assignment_date} BETWEEN '{kwargs['range_start']}' AND '{kwargs['range_end']}'",
                filter_generator.generate_customer_groups_filter(params=kwargs['customers_groups'], col=BaselineAlignedModeMeta.id)
            ])}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE creation_date BETWEEN {BaselineAlignedModeMeta.assignment_date} AND {BaselineAlignedModeMeta.removal_date}
UNION ALL
SELECT  {get_common_select_fields()}
        CAST(JULIANDAY({TicketsWithIterationsMeta.creation_date})-JULIANDAY('{kwargs['range_start']}') AS INT) AS {BaselineAlignedModeMeta.days_since_baseline}
FROM    ( SELECT * 
          FROM {CustomersActivityDBIndex.get_tickets_with_iterations_name()}
          WHERE {filter_generator.generate_creation_date_filter(range_start=kwargs['range_start'],range_end=kwargs['range_end'])}) AS twi
LEFT JOIN (
    SELECT  {BaselineAlignedModeMeta.user_crmid}
    FROM    {CustomersActivityDBIndex.get_tracked_customers_groups_name()}
    {filter_generator.generate_customer_groups_filter(
        params=kwargs['customers_groups'], 
        col=BaselineAlignedModeMeta.id, filter_prefix='WHERE')}
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
        {TicketsWithIterationsMeta.creation_date},
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
