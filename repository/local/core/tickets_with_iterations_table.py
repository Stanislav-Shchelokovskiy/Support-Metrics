from repository.local.core.baseline_aligned_customer_groups import get_baseline_aligned_mode_query
from repository.local.core.customers_rank import get_ranked_tickets_with_iterations_query


def get_tickets_with_iterations_table(**kwargs, ) -> str:
    if kwargs['use_baseline_aligned_mode']:
        return get_baseline_aligned_mode_query(**kwargs)
    return get_ranked_tickets_with_iterations_query(**kwargs)
