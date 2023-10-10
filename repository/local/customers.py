from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData, KnotMeta
from sql_queries.meta import CustomersGroupsMeta
from repository.local.validation_repository import ValidationRepositoryQueries
import sql_queries.index.db as DbIndex


# yapf: disable
class Customers(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return KnotMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        search_param = kwargs['search']
        filter_values = kwargs['filter_values']
        ids_filter = '\nOR '.join([f"{KnotMeta.id} = '{value}'" for value in filter_values])
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.customers,
            'where_group_limit': f'WHERE\n{ids_filter}' if ids_filter else f"WHERE {KnotMeta.name} LIKE '{search_param}%'\nLIMIT {kwargs['take']} OFFSET {kwargs['skip']}",
        }


class CustomersValidation(ValidationRepositoryQueries):
    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'values': ',\n'.join([f"('{value}')" for value in kwargs['values']]),
            'field': KnotMeta.id,
            'table': DbIndex.customers,
        }


class CustomersGroups(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CustomersGroupsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.customers_groups,
            'where_group_limit': f'ORDER BY {CustomersGroupsMeta.name}',
        }


class TrackedCustomersGroups(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return KnotMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'select': cols,
            'from': DbIndex.tracked_customers_groups,
            'where_group_limit': f'GROUP BY {cols}\nORDER BY {KnotMeta.name}',
        }
