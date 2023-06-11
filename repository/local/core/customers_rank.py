from typing import Protocol, Literal, runtime_checkable
from sql_queries.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from toolbox.sql.generators.filter_clause_generator_factory import FilterParameterNode
import repository.local.generators.filters_generators.tickets_with_iterations.limit as LimitsSqlFilterClauseGenerator
import repository.local.core.filters as filters


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
                    {filters.get_creation_date_with_offset_start_filter(**kwargs)}
                    {filters.get_tickets_filter(**kwargs)}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {LimitsSqlFilterClauseGenerator.generate_percentile_filter(alias='percentile', percentile=percentile.value)}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = {tbl}.{TicketsWithIterationsMeta.user_crmid}"""
    )


def get_rank_field(percentile: Percentile) -> str:
    if percentile.metric == 'tickets':
        return TicketsWithIterationsMeta.ticket_scid
    return TicketsWithIterationsMeta.emp_post_id
