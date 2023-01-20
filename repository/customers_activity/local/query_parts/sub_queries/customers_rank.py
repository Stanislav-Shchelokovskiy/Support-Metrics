from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.sql_filters_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
import repository.customers_activity.local.query_parts.filters as filters


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
        WHERE percentile <= {get_percentile_value(kwargs)}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = ti.{TicketsWithIterationsMeta.user_crmid}"""
    )


def get_rank_field(kwargs: dict):
    if kwargs.get('tickets_percentile') is not None:
        return TicketsWithIterationsMeta.ticket_scid
    return TicketsWithIterationsMeta.emp_post_id


def get_percentile_value(kwargs: dict) -> int:

    def validate_percentile(val: int | None):
        if val is not None:
            if val < 0:
                val = 0
            if val > 100:
                val = 100
        else:
            val = 100
        return val

    tickets_percentile = kwargs.get('tickets_percentile')
    if tickets_percentile is not None:
        return validate_percentile(tickets_percentile)
    iterations_percentile = kwargs.get('iterations_percentile')
    if iterations_percentile is None:
        return 100
    return validate_percentile(iterations_percentile)
