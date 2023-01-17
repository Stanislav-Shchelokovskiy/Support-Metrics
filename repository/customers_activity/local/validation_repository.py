from toolbox.sql.repository import SqliteRepository
from sql_queries.index import CustomersActivitySqlPathIndex


class ValidationRepository(SqliteRepository):

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_validate_path()

    def validate_values(self, kwargs: dict) -> str:
        return self.get_data_json(**kwargs)

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'values': kwargs['values'],
            'field': kwargs['field'],
            'table': kwargs['table'],
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ['value', 'valid']
