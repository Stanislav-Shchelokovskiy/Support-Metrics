from toolbox.sql.sql_query import SqlQuery
from sql_queries.meta import (
    TribesMeta,
    TicketsTagsMeta,
    TicketsTypesMeta,
    CustomersGroupsMeta,
    LicenseStatusesMeta,
    CATRepliesTypesMeta,
    FrameworksMeta,
    OperatingSystemsMeta,
    BuildsMeta,
    SeverityMeta,
    TicketStatusesMeta,
    IDEsMeta,
    EmployeesMeta,
)
import sql_queries.index.db as DbIndex
import sql_queries.index.path.transform_load as TransformLoadPathIndex


def _knot_table_def(format_params: dict[str, str]):
    return SqlQuery(
        query_file_path=TransformLoadPathIndex.knot,
        format_params=format_params,
    ).get_script()


# yapf: disable
def get_create_table_statements() -> dict[str, str]:
    return __create_table_statements

__create_table_statements = {
        DbIndex.tribes:
            _knot_table_def(
                format_params={
                    'id': TribesMeta.id,
                    'id_type': 'TEXT',
                    'name': TribesMeta.name,
                    'table': DbIndex.tribes,
                }
            ),

        DbIndex.tents:
            _knot_table_def(
                format_params={
                    'id': TribesMeta.id,
                    'id_type': 'TEXT',
                    'name': TribesMeta.name,
                    'table': DbIndex.tents,
                }
            ),

        DbIndex.tickets_tags:
            _knot_table_def(
                format_params={
                    'id': TicketsTagsMeta.id,
                    'id_type': 'TEXT',
                    'name': TicketsTagsMeta.name,
                    'table': DbIndex.tickets_tags,
                }
            ),

        DbIndex.tickets_types:
            _knot_table_def(
                format_params={
                    'id': TicketsTypesMeta.id,
                    'id_type': 'INT',
                    'name': TicketsTypesMeta.name,
                    'table': DbIndex.tickets_types,
                }
            ),

        DbIndex.frameworks:
            _knot_table_def(
                format_params={
                    'id': FrameworksMeta.id,
                    'id_type': 'TEXT',
                    'name': FrameworksMeta.name,
                    'table': DbIndex.frameworks,
                }
            ),

        DbIndex.operating_systems:
            _knot_table_def(
                format_params={
                    'id': OperatingSystemsMeta.id,
                    'id_type': 'TEXT',
                    'name': OperatingSystemsMeta.name,
                    'table': DbIndex.operating_systems,
                }
            ),

        DbIndex.builds:
            _knot_table_def(
                format_params={
                    'id': BuildsMeta.id,
                    'id_type': 'TEXT',
                    'name': BuildsMeta.name,
                    'table': DbIndex.builds,
                }
            ),

        DbIndex.severity:
            _knot_table_def(
                format_params={
                    'id': SeverityMeta.id,
                    'id_type': 'TEXT',
                    'name': SeverityMeta.name,
                    'table': DbIndex.severity,
                }
            ),

        DbIndex.ticket_statuses:
            _knot_table_def(
                format_params={
                    'id': TicketStatusesMeta.id,
                    'id_type': 'TEXT',
                    'name': TicketStatusesMeta.name,
                    'table': DbIndex.ticket_statuses,
                }
            ),

        DbIndex.ides:
            _knot_table_def(
                format_params={
                    'id': IDEsMeta.id,
                    'id_type': 'TEXT',
                    'name': IDEsMeta.name,
                    'table': DbIndex.ides,
                }
            ),

        DbIndex.customers_groups:
            SqlQuery(
                query_file_path=TransformLoadPathIndex.customers_groups,
                format_params={
                    **CustomersGroupsMeta.get_attrs(),
                    'CustomersGroups': DbIndex.customers_groups,
                }
            ).get_script(),

        DbIndex.license_statuses:
            _knot_table_def(
                format_params={
                    'id': LicenseStatusesMeta.id,
                    'id_type': 'INT',
                    'name': LicenseStatusesMeta.name,
                    'table': DbIndex.license_statuses,
                }
            ),

        DbIndex.cat_replies_types:
            _knot_table_def(
                format_params={
                    'id': CATRepliesTypesMeta.id,
                    'id_type': 'TEXT',
                    'name': CATRepliesTypesMeta.name,
                    'table': DbIndex.cat_replies_types,
                }
            ),

        DbIndex.employees:
            SqlQuery(
                query_file_path=TransformLoadPathIndex.emps,
                format_params={
                    **EmployeesMeta.get_attrs(),
                    'Employees': DbIndex.employees
                }
            ).get_script(),
    }
