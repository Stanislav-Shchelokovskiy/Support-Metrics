from toolbox.sql.generators.utils import build_filter_string
from toolbox.sql.generators.filter_clause_generator_factory import FilterParametersNode
import repository.local.generators.filters_generators.tickets_with_iterations.common as common
import repository.local.generators.filters_generators.tickets_with_iterations.platforms_products as platforms_products
import repository.local.generators.filters_generators.tickets_with_iterations.tickets as tickets
import repository.local.generators.filters_generators.tickets_with_iterations.ticket_types as ticket_types
import repository.local.generators.filters_generators.tickets_with_iterations.bugs as bugs
import repository.local.generators.filters_generators.tickets_with_iterations.cat as cat
import repository.local.generators.filters_generators.tickets_with_iterations.customers as customers
import repository.local.generators.filters_generators.tickets_with_iterations.employees as employees


def get_creation_date_with_offset_start_filter(
    range_start: str,
    range_end: str,
    **kwargs,
) -> str:
    return common.generate_creation_date_with_rank_offset_start_filter(
        range_start=range_start,
        range_end=range_end,
    )


def try_get_creation_date_and_tickets_filters(
    use_baseline_aligned_mode: bool,
    **kwargs,
) -> str:
    if use_baseline_aligned_mode:
        return ''
    return get_creation_date_and_tickets_filters(**kwargs)


def get_creation_date_and_tickets_filters(
    filter_prefix: str = 'WHERE',
    **kwargs,
) -> str:
    return build_filter_string(
        (
            get_creation_date_filter(filter_prefix=filter_prefix, kwargs=kwargs),
            get_tickets_filter(**kwargs),
        )
    )


def get_creation_date_filter(
    filter_prefix: str,
    kwargs: dict,
) -> str:
    return common.generate_creation_date_filter(
        range_start=kwargs['range_start'],
        range_end=kwargs['range_end'],
        filter_prefix=filter_prefix,
    )


# yapf: disable
def get_tickets_filter(**kwargs) -> str:
    return build_filter_string((
        # index start
        ticket_types.generate_ticket_types_filter(params=kwargs['tickets_types']),
        customers.generate_license_status_filter(params=kwargs['license_statuses']),
        employees.generate_emp_positions_filter(params=kwargs['positions_ids']),
        tickets.generate_privacy_filter(params=kwargs['is_private']),
        tickets.generate_tribes_filter(params=kwargs['tribe_ids']),
        tickets.generate_tents_filter(params=kwargs['tent_ids']),
        # index end
        platforms_products.generate_platforms_filter(params=kwargs['platforms_ids']),
        platforms_products.generate_products_filter(params=kwargs['products_ids']),
        ticket_types.generate_duplicated_to_ticket_types_filter(params=kwargs['duplicated_to_tickets_types']),
        tickets.generate_builds_filter(params=kwargs['builds']),
        bugs.generate_fixed_in_builds_filter(params=kwargs['fixed_in_builds']),
        bugs.generate_severity_filter(params=kwargs['severity']),
        bugs.generate_ticket_status_filter(params=kwargs['ticket_status']),
        tickets.generate_is_employee_filter(params=kwargs['is_employee']),
        tickets.generate_closed_for_n_days(params=kwargs['closed_for_n_days']),
        tickets.generate_frameworks_filter(params=kwargs['frameworks']),
        tickets.generate_operating_systems_filter(params=kwargs['operating_system_id']),
        tickets.generate_ides_filter(params=kwargs['ide_id']),
        tickets.generate_ticket_tags_filter(params=kwargs['tickets_tags']),
        try_get_customer_groups_filter(**kwargs),
        customers.generate_conversion_status_filter(params=kwargs['conversion_statuses']),
        employees.generate_emp_tribes_filter(params=kwargs['emp_tribe_ids']),
        employees.generate_emp_tents_filter(params=kwargs['emp_tent_ids']),
        employees.generate_employees_filter(params=kwargs['emp_ids']),
        bugs.generate_assigned_to_filter(params=kwargs['assigned_to_ids']),
        bugs.generate_closed_by_filter(params=kwargs['closed_by_ids']),
        bugs.generate_closed_on_filter(params=kwargs['closed_between']),
        bugs.generate_fixed_by_filter(params=kwargs['fixed_by_ids']),
        bugs.generate_fixed_on_filter(params=kwargs['fixed_between']),
        cat.generate_reply_types_filter(params=kwargs['reply_ids']),
        cat.generate_components_filter(params=kwargs['components_ids']),
        cat.generate_features_filter(params=kwargs['feature_ids']),
        customers.generate_customers_filter(params=kwargs['customers_crmids']),
    ))
# yapf: enable


def try_get_customer_groups_filter(
    customers_groups: FilterParametersNode,
    ignore_groups_filter: bool = False,
    **kwargs,
) -> str:
    if ignore_groups_filter:
        return ''
    return customers.generate_customer_groups_filter(params=customers_groups)
