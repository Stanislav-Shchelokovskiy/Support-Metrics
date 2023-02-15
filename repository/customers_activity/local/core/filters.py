from typing import Iterable
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator


def get_creation_date_with_offset_start_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    return filter_generator.common.generate_creation_date_with_rank_offset_start_filter(
        range_start=kwargs['range_start'],
        range_end=kwargs['range_end'],
    )


def try_get_creation_date_and_tickets_filters(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    if kwargs['use_baseline_aligned_mode']:
        return ''
    return get_creation_date_and_tickets_filters(
        kwargs=kwargs,
        filter_generator=filter_generator,
    )


def get_creation_date_and_tickets_filters(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
    filter_prefix: str = 'WHERE'
):
    return build_filter_string(
        (
            get_creation_date_filter(
                kwargs=kwargs,
                filter_generator=filter_generator,
                filter_prefix=filter_prefix,
            ),
            get_tickets_filter(
                kwargs=kwargs,
                filter_generator=filter_generator,
            )
        )
    )


def get_creation_date_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
    filter_prefix: str,
) -> str:
    return filter_generator.common.generate_creation_date_filter(
        range_start=kwargs['range_start'],
        range_end=kwargs['range_end'],
        filter_prefix=filter_prefix,
    )


# yapf: disable
def get_tickets_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    return build_filter_string((
        # index start
            filter_generator.tickets_types.generate_ticket_types_filter(params=kwargs['tickets_types']),
            filter_generator.customers.generate_license_status_filter(params=kwargs['license_statuses']),
            filter_generator.employees.generate_emp_positions_filter(params=kwargs['positions_ids']),
            filter_generator.tickets.generate_privacy_filter(params=kwargs['is_private']),
            filter_generator.tickets.generate_tribes_filter(params=kwargs['tribe_ids']),
        # index end
            filter_generator.platforms_products.generate_platforms_filter(params=kwargs['platforms_ids']),
            filter_generator.platforms_products.generate_products_filter(params=kwargs['products_ids']),
            filter_generator.tickets_types.generate_duplicated_to_ticket_types_filter(params=kwargs['duplicated_to_tickets_types']),
            filter_generator.tickets.generate_builds_filter(params=kwargs['builds']),
            filter_generator.bugs.generate_fixed_in_builds_filter(params=kwargs['fixed_in_builds']),
            filter_generator.bugs.generate_severity_filter(params=kwargs['severity']),
            filter_generator.bugs.generate_ticket_status_filter(params=kwargs['ticket_status']),
            filter_generator.tickets.generate_frameworks_filter(params=kwargs['frameworks']),
            filter_generator.tickets.generate_operating_systems_filter(params=kwargs['operating_system_id']),
            filter_generator.tickets.generate_ides_filter(params=kwargs['ide_id']),
            filter_generator.tickets.generate_ticket_tags_filter(params=kwargs['tickets_tags']),
            try_get_customer_groups_filter(kwargs=kwargs, filter_generator=filter_generator),
            filter_generator.customers.generate_conversion_status_filter(params=kwargs['conversion_statuses']),
            filter_generator.employees.generate_emp_tribes_filter(params=kwargs['emp_tribe_ids']),
            filter_generator.employees.generate_employees_filter(params=kwargs['emp_ids']),
            filter_generator.cat.generate_reply_types_filter(params=kwargs['reply_ids']),
            filter_generator.cat.generate_components_filter(params=kwargs['components_ids']),
            filter_generator.cat.generate_features_filter(params=kwargs['feature_ids']),
            filter_generator.customers.generate_customers_filter(params=kwargs['customers_crmids']),
        ))
# yapf: enable


def try_get_customer_groups_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    if kwargs.get('ignore_groups_filter', False):
        return ''
    return filter_generator.customers.generate_customer_groups_filter(
        params=kwargs['customers_groups']
    )


def build_filter_string(filters: Iterable[str]) -> str:
    return '\n\t'.join(filter(None, filters))
