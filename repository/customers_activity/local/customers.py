from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    TrackedCustomersGroupsMeta,
    CustomersMeta,
)

from repository.customers_activity.local.validation_repository import ValidationRepository


# yapf: disable
class CustomersRepository(SqliteRepository):
    """
    Interface to a local table storing available customers.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        search_param = kwargs['search']
        filter_values=kwargs['filter_values']
        ids_filter = '\nOR '.join([f"{CustomersMeta.id} = '{value}'" for value in filter_values])
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_customers_name(),
            'filter_group_limit_clause': f'WHERE\n{ids_filter}' if ids_filter else f"WHERE {CustomersMeta.name} LIKE '{search_param}%'\nLIMIT {kwargs['take']} OFFSET {kwargs['skip']}",
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [CustomersMeta.id, CustomersMeta.name]

    def validate_values(self, **kwargs) -> str:
        validation_repository = ValidationRepository()
        return validation_repository.validate_values(
                kwargs={
                    'values': ',\n'.join([f"('{value}')" for value in kwargs['values']]),
                    'field': CustomersMeta.id,
                    'table': CustomersActivityDBIndex.get_customers_name(),
            })

class CustomersGroupsRepository(SqliteRepository):
    """
    Interface to a local table storing customers groups.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_customers_groups_name(),
            'filter_group_limit_clause': f'ORDER BY {CustomersGroupsMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TrackedCustomersGroupsRepository(SqliteRepository):
    """
    Interface to a local table storing customers groups we track and work with.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        cols = ', '.join(self.get_must_have_columns(kwargs))
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_tracked_customers_groups_name(),
            'filter_group_limit_clause': f'GROUP BY {cols}\nORDER BY {TrackedCustomersGroupsMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            TrackedCustomersGroupsMeta.id,
            TrackedCustomersGroupsMeta.name,
        ]
