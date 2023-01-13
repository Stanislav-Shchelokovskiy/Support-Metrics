from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.sql_query_params_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
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
                      NTILE(100) OVER (ORDER BY COUNT(DISTINCT {TicketsWithIterationsMeta.ticket_scid}) DESC) AS tickets_rank,
                      NTILE(100) OVER (ORDER BY COUNT({TicketsWithIterationsMeta.emp_post_id}) DESC) AS iterations_rank
                FROM  {CustomersActivityDBIndex.get_tickets_with_iterations_name()}
                WHERE 
                    {filters.get_creation_date_with_offset_stars_filter(kwargs=kwargs,filter_generator=filter_generator)}
                    {filters.get_tickets_filter(kwargs=kwargs,filter_generator=filter_generator)}
                GROUP BY {TicketsWithIterationsMeta.user_crmid} ) AS rnk
        WHERE {filters.get_rank_filter(kwargs)}
    ) AS usr_rnk ON usr_rnk.{TicketsWithIterationsMeta.user_crmid} = ti.{TicketsWithIterationsMeta.user_crmid}"""
    )
