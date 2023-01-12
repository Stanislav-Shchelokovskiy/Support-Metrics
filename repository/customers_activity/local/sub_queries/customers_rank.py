from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.sql_query_params_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator


def get_ranked_tickets_with_iterations_query(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    return (
        f"""{CustomersActivityDBIndex.get_tickets_with_iterations_name()} AS ti 
    INNER JOIN ( 
        SELECT {TicketsWithIterationsMeta.user_crmid}
        FROM ( SELECT {TicketsWithIterationsMeta.user_crmid},
                      NTILE(100) OVER (ORDER BY COUNT(DISTINCT {TicketsWithIterationsMeta.ticket_scid}) DESC) AS tickets_rank,
                      NTILE(100) OVER (ORDER BY COUNT({TicketsWithIterationsMeta.emp_post_id}) DESC) AS iterations_rank
                FROM  {CustomersActivityDBIndex.get_tickets_with_iterations_name()}
                WHERE {filter_generator.generate_creation_date_with_offset_start_filter(range_start=kwargs['range_start'], range_end=kwargs['range_end'])}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {get_rank_filter(kwargs)}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = ti.{TicketsWithIterationsMeta.user_crmid}"""
    )


def get_rank_filter(kwargs: dict) -> str:
    tickets_rank = kwargs['tickets_rank']
    if tickets_rank is not None:
        return f'tickets_rank <= {validate_rank(tickets_rank)}'
    iterations_rank = kwargs['iterations_rank']
    if iterations_rank is None:
        return 'tickets_rank <= 100'
    return f'iterations_rank <= {validate_rank(iterations_rank)}'


def validate_rank(rank: int | None):
    if rank is not None:
        if rank < 0:
            rank = 0
        if rank > 100:
            rank = 100
    else:
        rank = 100
    return rank
