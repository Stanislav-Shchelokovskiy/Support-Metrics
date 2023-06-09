from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.index import CustomersActivityDBIndex
from sql_queries.meta import (
    CustomersGroupsMeta,
    TrackedCustomersGroupsMeta,
    CustomersMeta,
)

from repository.local.validation_repository import ValidationRepositoryQueries


# yapf: disable
class Customers(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CustomersMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        search_param = kwargs['search']
        filter_values = kwargs['filter_values']
        ids_filter = '\nOR '.join([f"{CustomersMeta.id} = '{value}'" for value in filter_values])
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': CustomersActivityDBIndex.get_customers_name(),
            'where_group_limit': f'WHERE\n{ids_filter}' if ids_filter else f"WHERE {CustomersMeta.name} LIKE '{search_param}%'\nLIMIT {kwargs['take']} OFFSET {kwargs['skip']}",
        }


class CustomersValidation(ValidationRepositoryQueries):
    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'values': ',\n'.join([f"('{value}')" for value in kwargs['values']]),
            'field': CustomersMeta.id,
            'table': CustomersActivityDBIndex.get_customers_name(),
        }


class CustomersGroups(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CustomersGroupsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': CustomersActivityDBIndex.get_customers_groups_name(),
            'where_group_limit': f'ORDER BY {CustomersGroupsMeta.name}',
        }


class TrackedCustomersGroups(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TrackedCustomersGroupsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'select': cols,
            'from': CustomersActivityDBIndex.get_tracked_customers_groups_name(),
            'where_group_limit': f'GROUP BY {cols}\nORDER BY {TrackedCustomersGroupsMeta.name}',
        }
