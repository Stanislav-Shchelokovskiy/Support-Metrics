from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from toolbox.sql.sql_query import SqlQuery
import sql_queries.meta.aggs as aggs
import sql_queries.meta.employees as employees
import sql_queries.index.path.extract as RemotePathIndex


class EmployeesIterations(RepositoryAlchemyQueries):
    """
    Query to load employee iterations.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.employees_iterations

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **employees.EmployeesIterations.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return employees.EmployeesIterations.get_values()


class Tickets(RepositoryAlchemyQueries):
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
        return aggs.Tickets.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return aggs.Tickets.get_values()
