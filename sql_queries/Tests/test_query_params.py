import pytest
from os import getcwd
from typing import Callable
from pathlib import Path
import toolbox.sql.index as RootPath
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.meta import (
    TicketsWithPropertiesMeta,
    CustomersGroupsMeta,
    TicketsTagsMeta,
    CATRepliesTypesMeta,
    CATComponentsFeaturesMeta,
    TicketsWithIterationsAggregatesMeta,
    TicketsWithIterationsRawMeta,
    PlatformsProductsMeta,
    TicketsWithIterationsMeta,
    PositionsMeta,
    EmployeesIterationsMeta,
    TribeMeta,
    TribesMeta,
    EmployeesMeta,
    BaselineAlignedCustomersGroupsMeta,
    CustomersMeta,
    KnotMeta,
    TicketsTypesMeta,
    FrameworksMeta,
    OperatingSystemsMeta,
    BuildsMeta,
    SeverityMeta,
    TicketStatusesMeta,
    IDEsMeta,
)


tickets_with_iterations_common_params = {
    'tickets_with_iterations_table': 'table_name',
    'tickets_filter': 'tickets_filter',
}


# yapf: disable
@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            CustomersActivitySqlPathIndex.get_tickets_with_licenses_and_users_path,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_properties_path,
            TicketsWithPropertiesMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path,
            {
                **TicketsWithIterationsRawMeta.get_attrs(),
                **tickets_with_iterations_common_params,
                'tickets_types_table': 'tickets_types_table',
                'license_statuses_table': 'license_statuses_table',
                'conversion_statuses_table': 'conversion_statuses_table',
                'replies_types_table': 'replies_types_table',
                'components_features_table': 'components_features_table',
                'employees_table': 'employees_table',
                'severity_table': 'severity_table',
                'operating_systems_table': 'operating_systems_table',
                'ides_table': 'ides_table',
                'platforms_products_table': 'platforms_products_table',
                'baseline_aligned_mode_fields': 'baseline_aligned_mode_fields'
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_aggregates_path,
            {
                **TicketsWithIterationsAggregatesMeta.get_attrs(),
                **tickets_with_iterations_common_params,
                'group_by_period': 'group_by_period',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_customers_groups_path,
            CustomersGroupsMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_tracked_customers_groups_path,
            {
                **BaselineAlignedCustomersGroupsMeta.get_attrs(),
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_ticket_tags_path,
            TicketsTagsMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_replies_types_path,
            CATRepliesTypesMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_components_features_path,
            CATComponentsFeaturesMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_platforms_products_path,
            PlatformsProductsMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_path,
            {
                **TicketsWithIterationsMeta.get_attrs(),
                **EmployeesIterationsMeta.get_attrs(),
                'TicketsWithIterations': 'TicketsWithIterations',
                'CustomersTickets': 'CustomersTickets',
                'EmployeesIterations': 'EmployeesIterations',
                'rank_period_offset': 'rank_period_offset',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_emp_positions_path,
            {
                **PositionsMeta.get_attrs(),
                'EmployeesIterations': 'EmployeesIterations',
                'EmpPositions': 'EmpPositions',
                'position_id': EmployeesIterationsMeta.position_id,
                'position_name': EmployeesIterationsMeta.position_name
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_emp_tribes_path, {
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
                'start_date': 'start_date',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_customers_path,
            {
                **CustomersMeta.get_attrs(),
                'Users': 'Users',
                'TicketsWithIterations': 'TicketsWithIterations',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_validate_path,
            {
                'values': 'values',
                'field': 'field',
                'table': 'table',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_knot_path,
            {
                **KnotMeta.get_attrs(),
                'table': 'table',
                'id_type': 'type',
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_types_path,
            TicketsTypesMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_frameworks_path,
            FrameworksMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_operating_systems_path,
            OperatingSystemsMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_builds_path,
            BuildsMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_severity_path,
            SeverityMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_ticket_statuses_path,
            TicketStatusesMeta.get_attrs(),
        ),
        (
            CustomersActivitySqlPathIndex.get_ides_path,
            IDEsMeta.get_attrs(),
        ),
    ],
)
def test_query_params(
    get_query_file_path: Callable[[], str],
    format_params: dict,
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        query = Path(get_query_file_path()).read_text(encoding='utf-8')
        for key in format_params:
            assert f'{{{key}}}' in query



def prepare_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        target=RootPath,
        name='get_cwd',
        value=lambda: getcwd() + '/sql_queries',
    )
