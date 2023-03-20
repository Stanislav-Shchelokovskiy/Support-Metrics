from toolbox.sql.sql_query import SqlQuery
from sql_queries.index import CustomersActivityDBIndex, CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
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
)


def _knot_table_def(format_params: dict[str, str]):
    return SqlQuery(
        query_file_path=CustomersActivitySqlPathIndex.get_knot_path(),
        format_params=format_params,
    ).get_script()


# yapf: disable
def get_create_table_statements() -> dict[str, str]:
    return {
        CustomersActivityDBIndex.get_tribes_name():
            _knot_table_def(
                format_params={
                    'id': TribesMeta.id,
                    'id_type': 'TEXT',
                    'name': TribesMeta.name,
                    'table': CustomersActivityDBIndex.get_tribes_name(),
                }
            ),
        CustomersActivityDBIndex.get_tickets_tags_name():
            _knot_table_def(
                format_params={
                    'id': TicketsTagsMeta.id,
                    'id_type': 'TEXT',
                    'name': TicketsTagsMeta.name,
                    'table': CustomersActivityDBIndex.get_tickets_tags_name(),
                }
            ),

        CustomersActivityDBIndex.get_tickets_types_name():
            _knot_table_def(
                format_params={
                    'id': TicketsTypesMeta.id,
                    'id_type': 'INT',
                    'name': TicketsTypesMeta.name,
                    'table': CustomersActivityDBIndex.get_tickets_types_name(),
                }
            ),

        CustomersActivityDBIndex.get_frameworks_name():
            _knot_table_def(
                format_params={
                    'id': FrameworksMeta.id,
                    'id_type': 'TEXT',
                    'name': FrameworksMeta.name,
                    'table': CustomersActivityDBIndex.get_frameworks_name(),
                }
            ),

        CustomersActivityDBIndex.get_operating_systems_name():
            _knot_table_def(
                format_params={
                    'id': OperatingSystemsMeta.id,
                    'id_type': 'TEXT',
                    'name': OperatingSystemsMeta.name,
                    'table': CustomersActivityDBIndex.get_operating_systems_name(),
                }
            ),

        CustomersActivityDBIndex.get_builds_name():
            _knot_table_def(
                format_params={
                    'id': BuildsMeta.id,
                    'id_type': 'TEXT',
                    'name': BuildsMeta.name,
                    'table': CustomersActivityDBIndex.get_builds_name(),
                }
            ),

        CustomersActivityDBIndex.get_severity_name():
            _knot_table_def(
                format_params={
                    'id': SeverityMeta.id,
                    'id_type': 'TEXT',
                    'name': SeverityMeta.name,
                    'table': CustomersActivityDBIndex.get_severity_name(),
                }
            ),

        CustomersActivityDBIndex.get_ticket_statuses_name():
            _knot_table_def(
                format_params={
                    'id': TicketStatusesMeta.id,
                    'id_type': 'TEXT',
                    'name': TicketStatusesMeta.name,
                    'table': CustomersActivityDBIndex.get_ticket_statuses_name(),
                }
            ),

        CustomersActivityDBIndex.get_ides_name():
            _knot_table_def(
                format_params={
                    'id': IDEsMeta.id,
                    'id_type': 'TEXT',
                    'name': IDEsMeta.name,
                    'table': CustomersActivityDBIndex.get_ides_name(),
                }
            ),

        CustomersActivityDBIndex.get_customers_groups_name():
            _knot_table_def(
                format_params={
                    'id': CustomersGroupsMeta.id,
                    'id_type': 'TEXT',
                    'name': CustomersGroupsMeta.name,
                    'table': CustomersActivityDBIndex.get_customers_groups_name(),
                }
            ),

        CustomersActivityDBIndex.get_license_statuses_name():
            _knot_table_def(
                format_params={
                    'id': LicenseStatusesMeta.id,
                    'id_type': 'INT',
                    'name': LicenseStatusesMeta.name,
                    'table': CustomersActivityDBIndex.get_license_statuses_name(),
                }
            ),
        CustomersActivityDBIndex.get_cat_replies_types_name():
            _knot_table_def(
                format_params={
                    'id': CATRepliesTypesMeta.id,
                    'id_type': 'TEXT',
                    'name': CATRepliesTypesMeta.name,
                    'table': CustomersActivityDBIndex.get_cat_replies_types_name(),
                }
            ),
    }
