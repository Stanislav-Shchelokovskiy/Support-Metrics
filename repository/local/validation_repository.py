from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import ValidationMeta, MetaData
import sql_queries.index.path.local as LocalPathIndex


class ValidationRepositoryQueries(AsyncQueryDescriptor):

    def get_path(self, kwargs) -> str:
        return LocalPathIndex.validate

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return ValidationMeta

    def get_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'values': kwargs['values'],
            'field': kwargs['field'],
            'table': kwargs['table'],
        }
