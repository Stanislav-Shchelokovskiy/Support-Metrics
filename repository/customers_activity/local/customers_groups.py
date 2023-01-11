from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta, TrackedCustomersGroupsMeta
)


# yapf: disable
class CustomersGroupsRepository(SqliteRepository):
    """
    Interface to a local table storing customers groups.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_customers_groups_name(),
            'filter_clause': '',
            'group_by_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TrackedCustomersGroupsRepository(SqliteRepository):
    """
    Interface to a local table storing customers groups we track and work with.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        cols = ', '.join(self.get_must_have_columns(kwargs))
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_tracked_customers_groups_name(),
            'filter_clause': '',
            'group_by_clause': f'GROUP BY {cols}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            TrackedCustomersGroupsMeta.id,
            TrackedCustomersGroupsMeta.name,
        ]
