from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.core.baseline_aligned_customer_groups import get_baseline_aligned_mode_query
from repository.customers_activity.local.core.customers_rank import get_ranked_tickets_with_iterations_query


def get_tickets_with_iterations_table(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    if kwargs['use_baseline_aligned_mode']:
        return get_baseline_aligned_mode_query(
            kwargs=kwargs,
            filter_generator=filter_generator,
        )
    return get_ranked_tickets_with_iterations_query(
        kwargs=kwargs,
        filter_generator=filter_generator,
    )
