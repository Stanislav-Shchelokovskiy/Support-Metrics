from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from toolbox.sql.sql_query import SqlQuery
from sql_queries.meta import (
    TicketsWithPropertiesMeta,
    EmployeesIterationsMeta,
)
import sql_queries.index.path.extract as RemotePathIndex


class EmployeesIterations(RepositoryAlchemyQueries):
    """
    Query to load employee iterations.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.employees_iterations

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **EmployeesIterationsMeta.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return EmployeesIterationsMeta.get_values()


class CustomersTickets(RepositoryAlchemyQueries):
    """
    Query to load customers with their tickets and licenses.
    """

    def get_prep_queries(self, **kwargs) -> Iterable[SqlQuery]:
        return (
            self.sql_query_type(
                query_file_path=RemotePathIndex.tickets_with_licenses_and_users,
                format_params=kwargs,
            ),
        )

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.tickets_with_properties

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketsWithPropertiesMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsWithPropertiesMeta.get_values()
