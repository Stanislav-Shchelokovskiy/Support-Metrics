from typing import Protocol, Literal
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.sql_filters_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
import repository.customers_activity.local.query_parts.filters as filters


class FilterParameterNode(Protocol):
    include: bool
    value: int


class Percentile(Protocol):
    metric: Literal['tickets', 'iterations']
    value: FilterParameterNode


def get_ranked_tickets_with_iterations_query(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    return (
        f"""{CustomersActivityDBIndex.get_tickets_with_iterations_name()} AS ti
    INNER JOIN (
        SELECT {TicketsWithIterationsMeta.user_crmid}
        FROM ( SELECT {TicketsWithIterationsMeta.user_crmid},
                      ROW_NUMBER() OVER (ORDER BY COUNT(DISTINCT {get_rank_field(kwargs)}) DESC) * 100.0 / COUNT(*) OVER () AS percentile
                FROM  {CustomersActivityDBIndex.get_tickets_with_iterations_name()}
                WHERE
                    {filters.get_creation_date_with_offset_start_filter(kwargs=kwargs,filter_generator=filter_generator)}
                    {filters.get_tickets_filter(kwargs=kwargs,filter_generator=filter_generator)}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {get_percentile_filter('percentile', kwargs['percentile'])}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = ti.{TicketsWithIterationsMeta.user_crmid}"""
    )


def get_rank_field(kwargs: dict):
    percentile: Percentile = kwargs['percentile']
    if percentile.metric == 'tickets':
        return TicketsWithIterationsMeta.ticket_scid
    return TicketsWithIterationsMeta.emp_post_id


def get_percentile_filter(alias: str, percentile: Percentile) -> str:

    def validate_percentile(val: int | None):
        if val is not None:
            if val < 0:
                val = 0
            if val > 100:
                val = 100
        else:
            val = 100
        return val

    value = percentile.value
    if value.include:
        return f'{alias} <= {validate_percentile(value.value)}'
    return f'{alias} > {validate_percentile(value.value)}'
