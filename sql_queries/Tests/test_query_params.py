import pytest
from os import getcwd
from pathlib import Path
import toolbox.sql.index as RootPath
from sql_queries.meta import (
    TicketsWithPropertiesMeta,
    CustomersGroupsMeta,
    TicketsTagsMeta,
    CATRepliesTypesMeta,
    CATComponentsFeaturesMeta,
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
    CSIMeta,
)
import sql_queries.index.path.extract as ExtractPathIndex
import sql_queries.index.path.local as LocalPathIndex
import sql_queries.index.path.transform_load as TransofrmLoadPathIndex


# yapf: disable
@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            ExtractPathIndex.tickets_with_licenses_and_users,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            ExtractPathIndex.tickets_with_properties,
            TicketsWithPropertiesMeta.get_attrs(),
        ),
        (
            LocalPathIndex.tickets_with_iterations_raw,
            {
                **TicketsWithIterationsRawMeta.get_attrs(),
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
                'baseline_aligned_mode_fields': 'baseline_aligned_mode_fields',
                'tickets_with_iterations_table': 'table_name',
                'tbl_alias': 'tbl',
                'csi_table': 'tbl',
                'tickets_tags_table': 'tbl',
            },
        ),
        (
            ExtractPathIndex.customers_groups,
            CustomersGroupsMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.tracked_customers_groups,
            {
                **BaselineAlignedCustomersGroupsMeta.get_attrs(),
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            ExtractPathIndex.ticket_tags,
            TicketsTagsMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.replies_types,
            CATRepliesTypesMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.components_features,
            CATComponentsFeaturesMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.platforms_products,
            PlatformsProductsMeta.get_attrs(),
        ),
        (
            TransofrmLoadPathIndex.tickets_with_iterations,
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
            TransofrmLoadPathIndex.emp_positions,
            {
                **PositionsMeta.get_attrs(),
                'EmployeesIterations': 'EmployeesIterations',
                'EmpPositions': 'EmpPositions',
                'position_id': EmployeesIterationsMeta.position_id,
                'position_name': EmployeesIterationsMeta.position_name
            },
        ),
        (
            TransofrmLoadPathIndex.emp_tribes, {
                **TribeMeta.get_attrs(),
                **TribesMeta.get_attrs(),
                'EmpTribes': 'EmpTribes',
                'EmployeesIterations': 'EmployeesIterations',
            }
        ),
        (
            ExtractPathIndex.employees,
            {
                **EmployeesMeta.get_attrs(),
                'start_date': 'start_date',
            },
        ),
        (
            TransofrmLoadPathIndex.customers,
            {
                **CustomersMeta.get_attrs(),
                'Users': 'Users',
                'TicketsWithIterations': 'TicketsWithIterations',
            },
        ),
        (
            LocalPathIndex.validate,
            {
                'values': 'values',
                'field': 'field',
                'table': 'table',
            },
        ),
        (
            TransofrmLoadPathIndex.knot,
            {
                **KnotMeta.get_attrs(),
                'table': 'table',
                'id_type': 'type',
            },
        ),
        (
            ExtractPathIndex.tickets_types,
            TicketsTypesMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.frameworks,
            FrameworksMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.operating_systems,
            OperatingSystemsMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.builds,
            BuildsMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.severity,
            SeverityMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.ticket_statuses,
            TicketStatusesMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.ides,
            IDEsMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.csi,
            CSIMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.tents,
            KnotMeta.get_attrs(),
        ),
        (
            ExtractPathIndex.tribes,
            KnotMeta.get_attrs(),
        ),
    ],
)
def test_query_params(
    get_query_file_path: str,
    format_params: dict,
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        query = Path(get_query_file_path).read_text(encoding='utf-8')
        for key in format_params:
            assert f'{{{key}}}' in query
        query.format(**format_params)



def prepare_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        target=RootPath,
        name='get_cwd',
        value=lambda: getcwd() + '/sql_queries',
    )
