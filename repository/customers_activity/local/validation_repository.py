from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from sql_queries.index import CustomersActivitySqlPathIndex
from toolbox.sql import ValidationMeta, MetaData


class ValidationRepositoryQueries(AsyncQueryDescriptor):

    def get_path(self, kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_validate_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return ValidationMeta

    def get_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'values': kwargs['values'],
            'field': kwargs['field'],
            'table': kwargs['table'],
        }
