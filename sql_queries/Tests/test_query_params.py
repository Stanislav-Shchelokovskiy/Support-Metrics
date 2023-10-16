import pytest
from os import getcwd
from pathlib import Path
from toolbox.sql import KnotMeta
import toolbox.sql.index as RootPath
from sql_queries.meta import (
    TicketsWithPropertiesMeta,
    CustomersGroupsMeta,
    CATComponentsFeaturesMeta,
    TicketsWithIterationsRawMeta,
    PlatformsProductsMeta,
    TicketsWithIterationsMeta,
    EmployeesIterationsMeta,
    EmployeesMeta,
    BaselineAlignedCustomersGroupsMeta,
    CSIMeta,
)
import sql_queries.index.path.extract as RemotePathIndex
import sql_queries.index.path.local as LocalPathIndex
import sql_queries.index.path.transform_load as TransofrmLoadPathIndex


# yapf: disable
@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            RemotePathIndex.tickets_with_licenses_and_users,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            RemotePathIndex.tickets_with_properties,
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
            RemotePathIndex.customers_groups,
            CustomersGroupsMeta.get_attrs(),
        ),
        (
            RemotePathIndex.tracked_customers_groups,
            {
                **BaselineAlignedCustomersGroupsMeta.get_attrs(),
                'start_date': 'qwe',
                'end_date': 'asd',
            },
        ),
        (
            RemotePathIndex.ticket_tags,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.replies_types,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.components_features,
            CATComponentsFeaturesMeta.get_attrs(),
        ),
        (
            RemotePathIndex.platforms_products,
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
            RemotePathIndex.employees,
            {
                **EmployeesMeta.get_attrs(),
                'start_date': 'start_date',
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
            RemotePathIndex.tickets_types,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.frameworks,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.operating_systems,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.builds,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.severity,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.ticket_statuses,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.ides,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.csi,
            CSIMeta.get_attrs(),
        ),
        (
            RemotePathIndex.tents,
            KnotMeta.get_attrs(),
        ),
        (
            RemotePathIndex.tribes,
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
