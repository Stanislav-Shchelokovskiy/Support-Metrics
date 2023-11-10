from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.meta.employees as employees
import sql_queries.index.path.extract as RemotePathIndex


class Employees(RepositoryAlchemyQueries):
    """
    Query to load employees.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.employees

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **employees.Employees.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return employees.Employees.get_values()
