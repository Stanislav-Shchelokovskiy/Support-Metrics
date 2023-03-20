from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    BaselineAlignedModeMeta,
)
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.core.filters import (
    build_filter_string,
    get_creation_date_and_tickets_filters,
    get_tickets_filter,
)
import repository.customers_activity.local.generators.filters_generators.tickets_with_iterations.customers as CustomersSqlFilterClauseGenerator


def get_baseline_aligned_mode_query(**kwargs) -> str:
    return f"""(SELECT twi.*,
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
                CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(params=kwargs['customers_groups'])
            ])}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE {build_filter_string([
                f'creation_date BETWEEN {BaselineAlignedModeMeta.assignment_date} AND {BaselineAlignedModeMeta.removal_date}',
                get_tickets_filter(ignore_groups_filter=True, **kwargs, )
            ])}
UNION ALL
SELECT  twi.*,
        CAST(JULIANDAY({TicketsWithIterationsMeta.creation_date})-JULIANDAY('{kwargs['range_start']}') AS INT) AS {BaselineAlignedModeMeta.days_since_baseline}
FROM    ( SELECT *
          FROM   {CustomersActivityDBIndex.get_tickets_with_iterations_name()}
          WHERE  {get_creation_date_and_tickets_filters(filter_prefix='', **kwargs)}) AS twi
LEFT JOIN (
    SELECT {BaselineAlignedModeMeta.user_crmid}
    FROM   {CustomersActivityDBIndex.get_tracked_customers_groups_name()}
    {CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(
        params=kwargs['customers_groups'],
        col=BaselineAlignedModeMeta.id, filter_prefix='WHERE')}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE tcg.user_crmid IS NULL
)"""
