from repository.customers_activity.local.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.core.tracked_customer_groups import get_tracked_customers_groups_query
from repository.customers_activity.local.core.customers_rank import get_ranked_tickets_with_iterations_query


def get_tickets_with_iterations_table(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    if kwargs['use_tracked_customer_groups']:
        return get_tracked_customers_groups_query(
            kwargs=kwargs,
            filter_generator=filter_generator,
        )
    return get_ranked_tickets_with_iterations_query(
        kwargs=kwargs,
        filter_generator=filter_generator,
    )
