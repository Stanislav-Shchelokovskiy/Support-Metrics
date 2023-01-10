from toolbox.sql.repository import Repository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    TrackedCustomersGroupsMeta,
)


class CustomersGroupsRepository(Repository):
    """
    Loads groups we use to filter tickets by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_customers_groups_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersGroupsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TrackedCustomersGroupsRepository(Repository):
    """
    Loads groups we use to filter and tickets align tickets by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tracked_customers_groups_path(
        )

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            **kwargs,
            **TrackedCustomersGroupsMeta.get_attrs(),
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TrackedCustomersGroupsMeta.get_values()
