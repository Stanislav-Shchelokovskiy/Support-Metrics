from typing import Iterable
from toolbox.sql.repository_queries import RepositoryQueries
from sql_queries.index import CustomersActivitySqlPathIndex


class ValidationRepositoryQueries(RepositoryQueries):

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_validate_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'values': kwargs['values'],
            'field': kwargs['field'],
            'table': kwargs['table'],
        }

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return ('value', 'valid', )
