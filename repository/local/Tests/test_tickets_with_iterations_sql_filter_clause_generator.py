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
from sql_queries.meta import TicketsWithIterationsMeta, BaselineAlignedModeMeta
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
            f"WHERE {TicketsWithIterationsMeta.creation_date} BETWEEN 'qwe' AND 'asd'",
        ),
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
                'filter_prefix': 'AND',
            },
            f"AND {TicketsWithIterationsMeta.creation_date} BETWEEN 'qwe' AND 'asd'",
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
            f"{TicketsWithIterationsMeta.creation_date} BETWEEN DATE('qwe', '-{config.get_rank_period_offset()}') AND 'asd'",
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


def test_generate_privacy_filter() -> str:
    return tickets.generate_privacy_filter(
        params=MockFilterParameterNode(include=True, value=100)
    ) == f'AND {TicketsWithIterationsMeta.is_private} = 100'


def test_generate_is_employee_filter() -> str:
    return tickets.generate_is_employee_filter(
        params=MockFilterParameterNode(include=True, value=100)
    ) == f'AND {TicketsWithIterationsMeta.is_employee} = 100'


@pytest.mark.parametrize(
    'generator, field', [
        (
            tickets.generate_tribes_filter,
            TicketsWithIterationsMeta.tribes_ids,
        ),
        (
            platforms_products.generate_platforms_filter,
            TicketsWithIterationsMeta.platforms,
        ),
        (
            platforms_products.generate_products_filter,
            TicketsWithIterationsMeta.products,
        ),
        (
            tickets.generate_builds_filter,
            TicketsWithIterationsMeta.builds,
        ),
        (
            bugs.generate_fixed_in_builds_filter,
            TicketsWithIterationsMeta.fixed_in_builds,
        ),
        (
            tickets.generate_frameworks_filter,
            TicketsWithIterationsMeta.frameworks,
        ),
        (
            tickets.generate_ticket_tags_filter,
            TicketsWithIterationsMeta.ticket_tags,
        ),
        (
            customers.generate_customer_groups_filter,
            TicketsWithIterationsMeta.user_groups,
        ),
    ]
)
def test_single_like_filters(
    generator,
    field: str,
    single_like_filter_cases,
):
    for values, output in single_like_filter_cases:
        assert generator(params=values) == output.format(field=field)


@pytest.mark.parametrize(
    'generator, field, values_converter', [
        (
            tickets.generate_tents_filter,
            TicketsWithIterationsMeta.tent_id,
            None,
        ),
        (
            ticket_types.generate_ticket_types_filter,
            TicketsWithIterationsMeta.ticket_type,
            str,
        ),
        (
            customers.generate_license_status_filter,
            TicketsWithIterationsMeta.license_status,
            str,
        ),
        (
            employees.generate_emp_positions_filter,
            TicketsWithIterationsMeta.emp_position_id,
            None,
        ),
        (
            customers.generate_tracked_customer_groups_filter,
            BaselineAlignedModeMeta.id,
            None,
        ),
        (
            ticket_types.generate_duplicated_to_ticket_types_filter,
            TicketsWithIterationsMeta.duplicated_to_ticket_type,
            str,
        ),
        (
            cat.generate_components_filter,
            TicketsWithIterationsMeta.component_id,
            None,
        ),
        (
            cat.generate_features_filter,
            TicketsWithIterationsMeta.feature_id,
            None,
        ),
        (
            customers.generate_conversion_status_filter,
            TicketsWithIterationsMeta.conversion_status,
            str,
        ),
        (
            employees.generate_emp_tribes_filter,
            TicketsWithIterationsMeta.emp_tribe_id,
            None,
        ),
        (
            employees.generate_employees_filter,
            TicketsWithIterationsMeta.emp_scid,
            None,
        ),
        (
            bugs.generate_assigned_to_filter,
            TicketsWithIterationsMeta.assigned_to,
            None,
        ),
        (
            bugs.generate_closed_by_filter,
            TicketsWithIterationsMeta.closed_by,
            None,
        ),
        (
            bugs.generate_fixed_by_filter,
            TicketsWithIterationsMeta.fixed_by,
            None,
        ),
        (
            cat.generate_reply_types_filter,
            TicketsWithIterationsMeta.reply_id,
            None,
        ),
        (
            customers.generate_customers_filter,
            TicketsWithIterationsMeta.user_crmid,
            None,
        ),
        (
            bugs.generate_severity_filter,
            TicketsWithIterationsMeta.severity,
            None,
        ),
        (
            bugs.generate_ticket_status_filter,
            TicketsWithIterationsMeta.ticket_status,
            None,
        ),
        (
            tickets.generate_operating_systems_filter,
            TicketsWithIterationsMeta.operating_system_id,
            None,
        ),
        (
            tickets.generate_ides_filter,
            TicketsWithIterationsMeta.ide_id,
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
    # yapf: disable
    for values, output in single_in_filter_cases(convert=values_converter, prefix='AND'):
        assert generator(params=values) == output.format(field=field)
    # yapf: enable


@pytest.mark.parametrize(
    'generator, field, values_converter', [
        (
            bugs.generate_closed_on_filter,
            TicketsWithIterationsMeta.closed_on,
            None,
        ),
        (
            bugs.generate_fixed_on_filter,
            TicketsWithIterationsMeta.fixed_on,
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
    # yapf: disable
    for values, output in between_filter_cases(convert=values_converter, prefix='AND'):
        assert generator(params=values) == output.format(field=field)
    # yapf: enable
