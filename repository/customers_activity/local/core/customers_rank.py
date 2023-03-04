from typing import Protocol, Literal, runtime_checkable
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import FilterParameterNode
import repository.customers_activity.local.core.filters as filters


@runtime_checkable
class Percentile(Protocol):
    metric: Literal['tickets', 'iterations']
    value: FilterParameterNode


def get_ranked_tickets_with_iterations_query(
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
    **kwargs,
) -> str:
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
                    {filters.get_creation_date_with_offset_start_filter(filter_generator=filter_generator, **kwargs)}
                    {filters.get_tickets_filter(filter_generator=filter_generator, **kwargs)}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {filter_generator.limit.get_percentile_filter(alias='percentile', percentile=percentile.value)}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = {tbl}.{TicketsWithIterationsMeta.user_crmid}"""
    )


def get_rank_field(percentile: Percentile) -> str:
    if percentile.metric == 'tickets':
        return TicketsWithIterationsMeta.ticket_scid
    return TicketsWithIterationsMeta.emp_post_id
