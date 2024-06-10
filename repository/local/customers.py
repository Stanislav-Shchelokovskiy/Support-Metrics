from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from repository.local.validation_repository import ValidationRepositoryQueries
import sql_queries.meta.customers as customers
import repository.local.generators.filters_generators.conversion_statuses as ConversionStatusesSqlFilterClauseGenerator


# yapf: disable
class Customers(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return customers.Customers

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        search_param = kwargs['search']
        filter_values = kwargs['filter_values']
        ids_filter = '\nOR '.join([f"{customers.Customers.id} = '{value}'" for value in filter_values])
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': customers.Customers.get_name(),
            'where_group_limit': f'WHERE\n{ids_filter}' if ids_filter else f"WHERE {customers.Customers.name} LIKE '{search_param}%'\nLIMIT {kwargs['take']} OFFSET {kwargs['skip']}",
        }


class CustomersValidation(ValidationRepositoryQueries):
    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'values': ',\n'.join([f"('{value}')" for value in kwargs['values']]),
            'field': customers.Customers.id,
            'table': customers.Customers.get_name(),
        }


class CustomersGroups(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return customers.CustomersGroups

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': customers.CustomersGroups.get_name(),
            'where_group_limit': f'ORDER BY {customers.CustomersGroups.name}',
        }


class TrackedCustomersGroups(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return customers.TrackedGroups

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'select': cols,
            'from': customers.TrackedGroups.get_name(),
            'where_group_limit': f'GROUP BY {cols}\nORDER BY {customers.TrackedGroups.name}',
        }


class LicenseStatuses(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return customers.LicenseStatuses

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': customers.LicenseStatuses.get_name(),
            'where_group_limit': '',
        }


class ConversionStatuses(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return customers.ConversionStatuses

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': customers.ConversionStatuses.get_name(),
            'where_group_limit': ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter(
                    license_status_ids=kwargs['license_status_ids']
                ),
        }
