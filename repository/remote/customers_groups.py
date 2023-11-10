from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.meta.customers as customers
import sql_queries.index.path.extract as RemotePathIndex


class CustomersGroups(RepositoryAlchemyQueries):
    """
    Query to load groups we use to filter tickets by.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.customers_groups

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return customers.CustomersGroups.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return customers.CustomersGroups.get_values()


class TrackedCustomersGroups(RepositoryAlchemyQueries):
    """
    Query to load groups we use to filter and tickets align tickets by.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.tracked_customers_groups

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            **kwargs,
            **customers.TrackedCustomersGroups.get_attrs(),
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return customers.TrackedCustomersGroups.get_values()
