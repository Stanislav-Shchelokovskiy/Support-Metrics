import pytest
from typing import Callable
from os import getcwd
from toolbox.sql.index import RootPath
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
)
from toolbox.sql.sql_query import SqlQuery
from sql_queries.customers_activity.meta import (
    TicketsWithLicensesMeta,
    CustomersGroupsMeta,
    TicketsTagsMeta,
    TicketsWithIterationsPeriodMeta,
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
    TicketsWithIterationsAggregatesMeta,
    TicketsWithIterationsRawMeta,
    PlatformsProductsMeta,
    TicketsWithIterationsMeta,
    PositionsMeta,
    EmployeesIterationsMeta,
    TribeMeta,
    TribesMeta,
    EmployeesMeta,
)


tickets_with_iterations_common_params = {
    'tickets_with_iterations_table': 'table_name',
    'creation_date': 'creation_date',
    'range_start': 'range_start',
    'range_end': 'range_end',
    'tribes_filter': 'tribes_filter',
    'positions_filter': 'positions_filter',
    'emp_tribes_filter': 'emp_tribes_filter',
    'customer_groups_filter': 'customer_groups_filter',
    'ticket_types_filter': 'ticket_types_filter',
    'ticket_tags_filter': 'ticket_tags_filter',
    'reply_types_filter': 'reply_types_filter',
    'components_filter': 'components_filter',
    'features_filter': 'features_filter',
    'license_status_filter': 'license_status_filter',
    'conversion_status_filter': 'conversion_status_filter',
    'platforms_filter': 'platforms_filter',
    'products_filter': 'products_filter',
}


@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            CustomersActivitySqlPathIndex.get_tickets_with_licenses_path,
            {
                **TicketsWithLicensesMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path,
            {
                **TicketsWithIterationsRawMeta.get_attrs(),
                **tickets_with_iterations_common_params,
                'license_statuses_table': 'license_statuses_table',
                'conversion_statuses_table': 'conversion_statuses_table',
                'replies_types_table': 'replies_types_table',
                'components_features_table': 'components_features_table',
            },
        ),
        (
            CustomersActivitySqlPathIndex.
            get_tickets_with_iterations_aggregates_path,
            {
                **TicketsWithIterationsAggregatesMeta.get_attrs(),
                **tickets_with_iterations_common_params,
                'group_by_period': 'group_by_period',
            },
        ),
        (
            CustomersActivitySqlPathIndex.
            get_fill_tickets_with_licenses_path,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_customers_groups_path,
            {
                **CustomersGroupsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_ticket_tags_path,
            {
                **TicketsTagsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_replies_types_path,
            {
                **ReplyTypesMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_components_features_path,
            {
                **ComponentsFeaturesMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_platforms_products_path,
            {
                **PlatformsProductsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.
            get_tickets_period_path,
            {
                'table_name': 'test',
                **TicketsWithIterationsPeriodMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_general_select_path,
            {
                'DISTINCT': 'empty_string | DISTINCT',
                'columns': 'qwe, asd',
                'table_name': 'test',
                'filter_clause': '',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_path,
            {
                **TicketsWithIterationsMeta.get_attrs(),
                **EmployeesIterationsMeta.get_attrs(),
                'TicketsWithIterations': 'TicketsWithIterations',
                'TicketsWithLicenses': 'TicketsWithLicenses',
                'EmployeesIterations': 'EmployeesIterations',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_emp_positions_path,
            {
                **PositionsMeta.get_attrs(),
                'EmployeesIterations': 'EmployeesIterations',
                'EmpPositions': 'EmpPositions',
                'pos_id': EmployeesIterationsMeta.pos_id,
                'pos_name': EmployeesIterationsMeta.pos_name
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_emp_tribes_path,
            {
                **TribeMeta.get_attrs(),
                **TribesMeta.get_attrs(),
                'EmpTribes': 'EmpTribes',
                'EmployeesIterations': 'EmployeesIterations',
            }
        ),
        (
            CustomersActivitySqlPathIndex.get_employees_path,
            {
                **EmployeesMeta.get_attrs(),
                'Employees': 'Employees',
                'EmployeesIterations': 'EmployeesIterations',
            },
        ),
    ],
)
def test_query_params(
    get_query_file_path: Callable[[], str],
    format_params: dict,
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        SqlQuery(
            query_file_path=get_query_file_path(),
            format_params=format_params,
        ).get_query()


def prepare_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        target=RootPath,
        name='get_cwd',
        value=lambda: getcwd() + '/sql_queries',
    )
