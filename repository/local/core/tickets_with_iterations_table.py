from collections.abc import Mapping
from repository.local.core.baseline_aligned_customer_groups import get_baseline_aligned_mode_query
from repository.local.core.customers_rank import get_ranked_tickets_with_iterations_query
from repository.local.core.csi import get_csi_query
from repository.local.core.ticket_lifetime import get_ticket_lifetime_query
from repository.local.aggs import is_csi, is_ticket_lifetime, is_baseline_aligned_mode


def get_tickets_with_iterations_table(**kwargs) -> str:
    if is_baseline_aligned_mode(kwargs):
        return get_baseline_aligned_mode_query(kwargs)
    tbl = get_ranked_tickets_with_iterations_query(kwargs)
    if is_csi(kwargs):
        return get_csi_query(tbl)
    if is_ticket_lifetime(kwargs):
        return get_ticket_lifetime_query(tbl, kwargs)
    return tbl
