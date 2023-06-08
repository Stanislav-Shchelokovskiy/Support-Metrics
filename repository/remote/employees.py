from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.meta import EmployeesMeta


class Employees(RepositoryAlchemyQueries):
    """
    Query to load employees.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_employees_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **EmployeesMeta.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return EmployeesMeta.get_values()
