import sql_queries.meta.aggs as aggs
import sql_queries.meta.customers as customers
from toolbox.sql.generators.utils import build_filter_string
from repository.local.core.filters import get_tickets_filter
import repository.local.generators.filters_generators.tickets_with_iterations.customers as CustomersSqlFilterClauseGenerator


def get_baseline_aligned_mode_query(**kwargs) -> str:
    return f"""(SELECT twi.*,
        CAST(JULIANDAY(creation_date)-JULIANDAY('{kwargs['range_start']}')-baseline_aligned_offest_in_days AS INT) AS {customers.BaselineAlignedMode.days_since_baseline}
FROM    {aggs.TicketsWithIterations.get_name()} AS twi
INNER JOIN (
    SELECT  {customers.BaselineAlignedMode.user_crmid},
            {customers.BaselineAlignedMode.assignment_date},
            {customers.BaselineAlignedMode.removal_date},
            CAST(JULIANDAY({customers.BaselineAlignedMode.assignment_date})-JULIANDAY('{kwargs['range_start']}') AS INTEGER) AS baseline_aligned_offest_in_days
    FROM    {customers.TrackedCustomersGroups.get_name()}
    WHERE   {build_filter_string([
                f"{customers.BaselineAlignedMode.assignment_date} BETWEEN '{kwargs['range_start']}' AND '{kwargs['range_end']}'",
                CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(params=kwargs['customers_groups'])
            ])}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE {build_filter_string([
                f'creation_date BETWEEN {customers.BaselineAlignedMode.assignment_date} AND {customers.BaselineAlignedMode.removal_date}',
                get_tickets_filter(ignore_groups_filter=True, **kwargs, )
            ])}
UNION ALL
SELECT  twi.*,
        CAST(JULIANDAY({aggs.TicketsWithIterations.creation_date})-JULIANDAY({max_of_min_customers_groups_creation_date_and_param(kwargs, param=f'twi.{aggs.TicketsWithIterations.user_register_date}')}) AS INT) AS {customers.BaselineAlignedMode.days_since_baseline}
FROM    ( SELECT *
          FROM   {aggs.TicketsWithIterations.get_name()}
          WHERE  {get_creation_date_and_tickets_filters(kwargs)}) AS twi
LEFT JOIN (
    SELECT {customers.BaselineAlignedMode.user_crmid}
    FROM   {customers.TrackedCustomersGroups.get_name()}
    {CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(
        params=kwargs['customers_groups'],
        col=customers.BaselineAlignedMode.id, filter_prefix='WHERE')}
) AS tcg ON tcg.user_crmid = twi.user_crmid
WHERE tcg.user_crmid IS NULL
) AS {aggs.TicketsWithIterations.get_alias()}"""


def get_creation_date_and_tickets_filters(kwargs):
    """If customer is added to the target group(s) then we take tickets created only between
    min creation_date among these groups (*) and max between range_start and (*)."""
    return build_filter_string(
        [
            f"""creation_date BETWEEN {max_of_min_customers_groups_creation_date_and_param(kwargs)} AND '{kwargs['range_end']}'""",
            get_tickets_filter(ignore_groups_filter=False, **kwargs)
        ]
    )


def max_of_min_customers_groups_creation_date_and_param(kwargs, param=None):
    param_or_range_start = param or f"'{kwargs['range_start']}'"
    return (
f"""(SELECT MAX(start)
FROM (  {get_min_customers_groups_creation_date(kwargs)}
        UNION ALL
        SELECT {param_or_range_start}
    ))"""
    )


def get_min_customers_groups_creation_date(kwargs):
    return f"""SELECT MIN({customers.CustomersGroups.creation_date}) AS start
                FROM {customers.CustomersGroups.get_name()}
                {CustomersSqlFilterClauseGenerator.generate_tracked_customer_groups_filter(
                    params=kwargs['customers_groups'],
                    col=customers.CustomersGroups.id,
                    filter_prefix='WHERE')}"""
