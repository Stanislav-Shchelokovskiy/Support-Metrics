from toolbox.sql.sql_query import SqlQuery
from sql_queries.index import CustomersActivityDBIndex, CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    TribesMeta,
    TicketsTagsMeta,
    TicketsTypesMeta,
    CustomersGroupsMeta,
    LicenseStatusesMeta,
    CATRepliesTypesMeta,
    TrackedCustomersGroupsMeta,
)


def _knot_table_def(format_params: dict[str, str]):
    return SqlQuery(
        query_file_path=CustomersActivitySqlPathIndex.get_knot_path(),
        format_params=format_params,
    ).get_query()


# yapf: disable
def get_create_table_statements() -> dict[str, str]:
    return {
        CustomersActivityDBIndex.get_tribes_name():
            _knot_table_def(
                format_params={
                    'id' : TribesMeta.id,
                    'name': TribesMeta.name,
                    'table': CustomersActivityDBIndex.get_tribes_name(),
                }
            ),
        CustomersActivityDBIndex.get_tickets_tags_name():
            _knot_table_def(
                format_params={
                    'id' : TicketsTagsMeta.id,
                    'name': TicketsTagsMeta.name,
                    'table': CustomersActivityDBIndex.get_tickets_tags_name(),
                }
            ),

        CustomersActivityDBIndex.get_tickets_types_name():
            _knot_table_def(
                format_params={
                    'id' : TicketsTypesMeta.id,
                    'name': TicketsTypesMeta.name,
                    'table': CustomersActivityDBIndex.get_tickets_types_name(),
                }
            ),

        CustomersActivityDBIndex.get_customers_groups_name():
            _knot_table_def(
                format_params={
                    'id' : CustomersGroupsMeta.id,
                    'name': CustomersGroupsMeta.name,
                    'table': CustomersActivityDBIndex.get_customers_groups_name(),
                }
            ),

        CustomersActivityDBIndex.get_license_statuses_name():
            _knot_table_def(
                format_params={
                    'id' : LicenseStatusesMeta.id,
                    'name': LicenseStatusesMeta.name,
                    'table': CustomersActivityDBIndex.get_license_statuses_name(),
                }
            ),
        CustomersActivityDBIndex.get_cat_replies_types_name():
            _knot_table_def(
                format_params={
                    'id' : CATRepliesTypesMeta.id,
                    'name': CATRepliesTypesMeta.name,
                    'table': CustomersActivityDBIndex.get_cat_replies_types_name(),
                }
            ),
        CustomersActivityDBIndex.get_tracked_customers_groups_name():
            _knot_table_def(
                format_params={
                    'id' : TrackedCustomersGroupsMeta.id,
                    'name': TrackedCustomersGroupsMeta.name,
                    'table': CustomersActivityDBIndex.get_tracked_customers_groups_name(),
                }
            ),
    }
