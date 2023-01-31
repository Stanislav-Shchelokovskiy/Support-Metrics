from typing import Protocol, Literal
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator import FilterParameterNode
import repository.customers_activity.local.core.filters as filters


class Percentile(Protocol):
    metric: Literal['tickets', 'iterations']
    value: FilterParameterNode


def get_ranked_tickets_with_iterations_query(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    percentile: Percentile = kwargs['percentile']
    tbl = CustomersActivityDBIndex.get_tickets_with_iterations_name()
    return (
        f"""{tbl}
    INNER JOIN (
        SELECT {TicketsWithIterationsMeta.user_crmid}
        FROM ( SELECT {TicketsWithIterationsMeta.user_crmid},
                      ROW_NUMBER() OVER (ORDER BY COUNT(DISTINCT {get_rank_field(percentile)}) DESC) * 100.0 / COUNT(*) OVER () AS percentile
                FROM  {tbl}
                INDEXED BY idx_{tbl}_{percentile.metric}_inner
                WHERE
                    {filters.get_creation_date_with_offset_start_filter(kwargs=kwargs,filter_generator=filter_generator)}
                    {filters.get_tickets_filter(kwargs=kwargs,filter_generator=filter_generator)}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {filter_generator.get_percentile_filter('percentile', percentile.value)}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = {tbl}.{TicketsWithIterationsMeta.user_crmid}"""
    )


def get_rank_field(percentile: Percentile):
    if percentile.metric == 'tickets':
        return TicketsWithIterationsMeta.ticket_scid
    return TicketsWithIterationsMeta.emp_post_id
