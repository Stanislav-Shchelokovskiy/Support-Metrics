from typing import Protocol, Literal, runtime_checkable
from sql_queries.meta import TicketsWithIterationsMeta
from toolbox.sql.generators.filter_clause_generator_factory import FilterParameterNode
import repository.local.generators.filters_generators.tickets_with_iterations.limit as LimitsSqlFilterClauseGenerator
import repository.local.core.filters as filters
import sql_queries.index.db as DbIndex


@runtime_checkable
class Percentile(Protocol):
    metric: Literal['tickets', 'iterations']
    value: FilterParameterNode

    @classmethod
    def to_valid_literal(cls, v: str):
        if v.lower() == 'tickets':
            return 'tickets'
        return 'iterations'


def get_ranked_tickets_with_iterations_query(**kwargs) -> str:
    percentile: Percentile = kwargs['percentile']
    tbl = DbIndex.tickets_with_iterations
    return (
        f"""{tbl} AS {DbIndex.tickets_with_iterations_alias}
    INNER JOIN (
        SELECT {TicketsWithIterationsMeta.user_crmid} AS crmid
        FROM ( SELECT {TicketsWithIterationsMeta.user_crmid},
                      ROW_NUMBER() OVER (ORDER BY COUNT(DISTINCT {get_rank_field(percentile)}) DESC) * 100.0 / COUNT(*) OVER () AS percentile
                FROM  {tbl}
                INDEXED BY idx_{tbl}_{percentile.metric}_inner
                WHERE
                    {filters.get_creation_date_with_offset_start_filter(**kwargs)}
                    {filters.get_tickets_filter(**kwargs)}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {LimitsSqlFilterClauseGenerator.generate_percentile_filter(alias='percentile', percentile=percentile.value)}
    ) AS usr_rnk ON usr_rnk.crmid = {DbIndex.tickets_with_iterations_alias}.{TicketsWithIterationsMeta.user_crmid}
    {filters.try_get_creation_date_and_tickets_filters(**kwargs)}"""
    )


def get_rank_field(percentile: Percentile) -> str:
    if percentile.metric == 'tickets':
        return TicketsWithIterationsMeta.ticket_scid
    return TicketsWithIterationsMeta.emp_post_id
