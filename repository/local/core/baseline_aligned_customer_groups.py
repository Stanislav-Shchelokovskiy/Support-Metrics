from sql_queries.meta import (
    TicketsWithIterationsMeta,
    BaselineAlignedModeMeta,
    CustomersGroupsMeta,
)
from toolbox.sql.generators.utils import build_filter_string
from repository.local.core.filters import get_tickets_filter
import repository.local.generators.filters_generators.tickets_with_iterations.customers as CustomersSqlFilterClauseGenerator
import sql_queries.index.db as DbIndex


def get_baseline_aligned_mode_query(**kwargs) -> str:
    return f"""(SELECT twi.*,
        CAST(JULIANDAY(creation_date)-JULIANDAY('{kwargs['range_start']}')-baseline_aligned_offest_in_days AS INT) AS {BaselineAlignedModeMeta.days_since_baseline}
FROM    {DbIndex.tickets_with_iterations} AS twi
INNER JOIN (
    SELECT  {BaselineAlignedModeMeta.user_crmid},
            {BaselineAlignedModeMeta.assignment_date},
            {BaselineAlignedModeMeta.removal_date},
            CAST(JULIANDAY({BaselineAlignedModeMeta.assignment_date})-JULIANDAY('{kwargs['range_start']}') AS INTEGER) AS baseline_aligned_offest_in_days
    FROM    {DbIndex.tracked_customers_groups}
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
        CAST(JULIANDAY({TicketsWithIterationsMeta.creation_date})-JULIANDAY(({get_min_customers_groups_creation_date(kwargs)})) AS INT) AS {BaselineAlignedModeMeta.days_since_baseline}
FROM    ( SELECT *
          FROM   {DbIndex.tickets_with_iterations}
          WHERE  {get_creation_date_and_tickets_filters(kwargs)}) AS twi
LEFT JOIN (
    SELECT {BaselineAlignedModeMeta.user_crmid}
    FROM   {DbIndex.tracked_customers_groups}
    {CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(
        params=kwargs['customers_groups'],
        col=BaselineAlignedModeMeta.id, filter_prefix='WHERE')}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE tcg.user_crmid IS NULL
) AS {DbIndex.tickets_with_iterations_alias}"""


def get_creation_date_and_tickets_filters(kwargs):
    """If customer is added to the target group(s) then we take tickets created only between
    min creation_date among these groups (*) and max between range_start and (*)."""
    return build_filter_string(
        [
            f"""creation_date BETWEEN ( SELECT MAX(start)
                                        FROM (  {get_min_customers_groups_creation_date(kwargs)}
                                                UNION ALL
                                                SELECT '{kwargs['range_start']}'
                                            )   ) AND '{kwargs['range_end']}'""",
            get_tickets_filter(ignore_groups_filter=False, **kwargs)
        ]
    )


def get_min_customers_groups_creation_date(kwargs):
    return f"""SELECT MIN({CustomersGroupsMeta.creation_date}) AS start
                FROM {DbIndex.customers_groups}
                {CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(
                    params=kwargs['customers_groups'],
                    col=CustomersGroupsMeta.id,
                    filter_prefix='WHERE')}"""
