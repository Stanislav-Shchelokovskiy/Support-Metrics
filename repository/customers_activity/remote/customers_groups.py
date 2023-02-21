from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    BaselineAlignedCustomersGroupsMeta,
)


class CustomersGroups(RepositoryAlchemyQueries):
    """
    Loads groups we use to filter tickets by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_customers_groups_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersGroupsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return CustomersGroupsMeta.get_values()


class TrackedCustomersGroups(RepositoryAlchemyQueries):
    """
    Loads groups we use to filter and tickets align tickets by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tracked_customers_groups_path(
        )

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            **kwargs,
            **BaselineAlignedCustomersGroupsMeta.get_attrs(),
        }

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return BaselineAlignedCustomersGroupsMeta.get_values()
