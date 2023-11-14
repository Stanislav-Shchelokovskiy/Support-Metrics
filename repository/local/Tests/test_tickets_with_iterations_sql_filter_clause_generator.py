import pytest
import repository.local.generators.filters_generators.tickets_with_iterations.limit as limit
import repository.local.generators.filters_generators.tickets_with_iterations.common as common
import repository.local.generators.filters_generators.tickets_with_iterations.platforms_products as platforms_products
import repository.local.generators.filters_generators.tickets_with_iterations.tickets as tickets
import repository.local.generators.filters_generators.tickets_with_iterations.ticket_types as ticket_types
import repository.local.generators.filters_generators.tickets_with_iterations.bugs as bugs
import repository.local.generators.filters_generators.tickets_with_iterations.cat as cat
import repository.local.generators.filters_generators.tickets_with_iterations.customers as customers
import repository.local.generators.filters_generators.tickets_with_iterations.employees as employees
from sql_queries.meta.aggs import TicketsWithIterations
from sql_queries.meta.customers import BaselineAlignedMode
from toolbox.sql.generators.Tests.mocks import (
    MockFilterParameterNode,
    MockPercentile,
)
import configs.config as config


@pytest.mark.parametrize(
    'kwargs, output', [
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
            },
            f"WHERE {TicketsWithIterations.creation_date} BETWEEN 'qwe' AND 'asd'",
        ),
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
                'filter_prefix': 'AND',
            },
            f"AND {TicketsWithIterations.creation_date} BETWEEN 'qwe' AND 'asd'",
        ),
    ]
)
def test_generate_creation_date_filter(
    kwargs: dict,
    output,
):
    assert common.generate_creation_date_filter(**kwargs) == output


@pytest.mark.parametrize(
    'kwargs, output', [
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
            },
            f"{TicketsWithIterations.creation_date} BETWEEN DATE('qwe', '-{config.get_rank_period_offset()}') AND 'asd'",
        ),
    ]
)
def test_generate_creation_date_with_offset_start_filter(
    kwargs: dict,
    output,
):
    assert common.generate_creation_date_with_rank_offset_start_filter(
        **kwargs
    ) == output


@pytest.mark.parametrize(
    'alias, percentile, output', [
        (
            'alias',
            MockFilterParameterNode(include=True, value=100),
            'alias <= 100',
        ),
        (
            'alias',
            MockFilterParameterNode(include=False, value=100),
            'alias > 100',
        ),
        (
            'alias',
            MockFilterParameterNode(include=True, value=50),
            'alias <= 50',
        ),
        (
            'alias',
            MockFilterParameterNode(include=False, value=50),
            'alias > 50',
        ),
    ]
)
def test_get_percentile_filter(
    alias: str,
    percentile: MockPercentile,
    output: str,
):
    assert limit.generate_percentile_filter(
        alias=alias,
        percentile=percentile,
    ) == output


@pytest.mark.parametrize(
    'generator, field, value_converter', [
        (
            tickets.generate_privacy_filter,
            TicketsWithIterations.is_private,
            int,
        ),
        (
            tickets.generate_is_employee_filter,
            TicketsWithIterations.is_employee,
            int,
        ),
    ]
)
def test_equals_filters(
    generator,
    field: str,
    value_converter,
    equals_filter_cases,
) -> str:
    __run_test(generator, field, equals_filter_cases, value_converter, 'AND')


@pytest.mark.parametrize(
    'generator, field, value_converter', [
        (
            tickets.generate_closed_for_n_days,
            TicketsWithIterations.closed_on,
            lambda x: f"DATE('now', '-{x} DAYS')"
        ),
    ]
)
def test_less_equals_filters(
    generator,
    field: str,
    value_converter,
    less_equals_filter_cases,
) -> str:
    __run_test(generator, field, less_equals_filter_cases, value_converter, 'AND')


@pytest.mark.parametrize(
    'generator, field, value_converter', [
        (
            tickets.generate_resolution_in_hours,
            TicketsWithIterations.resolution_in_hours,
            int,
        ),
    ]
)
def test_less_filters(
    generator,
    field: str,
    value_converter,
    less_filter_cases,
) -> str:
    __run_test(generator, field, less_filter_cases, value_converter, 'AND')


@pytest.mark.parametrize(
    'generator, field', [
        (
            tickets.generate_tribes_filter,
            TicketsWithIterations.tribes_ids,
        ),
        (
            platforms_products.generate_platforms_filter,
            TicketsWithIterations.platforms,
        ),
        (
            platforms_products.generate_products_filter,
            TicketsWithIterations.products,
        ),
        (
            tickets.generate_builds_filter,
            TicketsWithIterations.builds,
        ),
        (
            bugs.generate_fixed_in_builds_filter,
            TicketsWithIterations.fixed_in_builds,
        ),
        (
            tickets.generate_frameworks_filter,
            TicketsWithIterations.frameworks,
        ),
        (
            tickets.generate_ticket_tags_filter,
            TicketsWithIterations.ticket_tags,
        ),
        (
            customers.generate_customer_groups_filter,
            TicketsWithIterations.user_groups,
        ),
    ]
)
def test_single_like_filters(
    generator,
    field: str,
    single_like_filter_cases,
):
    __run_test(generator, field, single_like_filter_cases)


@pytest.mark.parametrize(
    'generator, field, values_converter', [
        (
            tickets.generate_tents_filter,
            TicketsWithIterations.tent_id,
            None,
        ),
        (
            ticket_types.generate_ticket_types_filter,
            TicketsWithIterations.ticket_type,
            str,
        ),
        (
            customers.generate_license_status_filter,
            TicketsWithIterations.license_status,
            str,
        ),
        (
            employees.generate_emp_positions_filter,
            TicketsWithIterations.emp_position_id,
            None,
        ),
        (
            customers.generate_tracked_customer_groups_filter,
            BaselineAlignedMode.id,
            None,
        ),
        (
            ticket_types.generate_duplicated_to_ticket_types_filter,
            TicketsWithIterations.duplicated_to_ticket_type,
            str,
        ),
        (
            cat.generate_components_filter,
            TicketsWithIterations.component_id,
            None,
        ),
        (
            cat.generate_features_filter,
            TicketsWithIterations.feature_id,
            None,
        ),
        (
            customers.generate_conversion_status_filter,
            TicketsWithIterations.conversion_status,
            str,
        ),
        (
            employees.generate_emp_tribes_filter,
            TicketsWithIterations.emp_tribe_id,
            None,
        ),
        (
            employees.generate_employees_filter,
            TicketsWithIterations.emp_scid,
            None,
        ),
        (
            bugs.generate_assigned_to_filter,
            TicketsWithIterations.assigned_to,
            None,
        ),
        (
            bugs.generate_closed_by_filter,
            TicketsWithIterations.closed_by,
            None,
        ),
        (
            bugs.generate_fixed_by_filter,
            TicketsWithIterations.fixed_by,
            None,
        ),
        (
            cat.generate_reply_types_filter,
            TicketsWithIterations.reply_id,
            None,
        ),
        (
            customers.generate_customers_filter,
            TicketsWithIterations.user_crmid,
            None,
        ),
        (
            bugs.generate_severity_filter,
            TicketsWithIterations.severity,
            None,
        ),
        (
            bugs.generate_ticket_status_filter,
            TicketsWithIterations.ticket_status,
            None,
        ),
        (
            tickets.generate_operating_systems_filter,
            TicketsWithIterations.operating_system_id,
            None,
        ),
        (
            tickets.generate_ides_filter,
            TicketsWithIterations.ide_id,
            None,
        ),
    ]
)
def test_single_in_filters(
    generator,
    field: str,
    values_converter,
    single_in_filter_cases,
):
    __run_test(generator, field, single_in_filter_cases, values_converter, 'AND')


@pytest.mark.parametrize(
    'generator, field, values_converter', [
        (
            bugs.generate_closed_on_filter,
            TicketsWithIterations.closed_on,
            None,
        ),
        (
            bugs.generate_fixed_on_filter,
            TicketsWithIterations.fixed_on,
            None,
        ),
    ]
)
def test_between_filters(
    generator,
    field: str,
    values_converter,
    between_filter_cases,
):
    __run_test(generator, field, between_filter_cases, values_converter, 'AND')


def __run_test(generator, field, filter_cases, converter=None, prefix='WHERE'):
    for params, output in filter_cases(convert=converter, prefix=prefix):
        assert generator(params=params) == output.format(field=field)
