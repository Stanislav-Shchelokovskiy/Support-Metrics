from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    PositionsMeta,
    TribesMeta,
    EmployeeMeta,
    TentsMeta,
)
import repository.customers_activity.local.generators.filters_generators.employees as EmployeesSqlFilterClauseGenerator


# yapf: disable
class EmpPositions(AsyncQueryDescriptor):
    """
    Query to a local table storing available emp positions.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return PositionsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_positions_name(),
            'filter_group_limit_clause': f'ORDER BY {PositionsMeta.name}',
        }


class EmpTribes(AsyncQueryDescriptor):
    """
    Query to a local table storing available emp tribes.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TribesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_tribes_name(),
            'filter_group_limit_clause': f'ORDER BY {TribesMeta.name}',
        }


class EmpTents(AsyncQueryDescriptor):
    """
    Query to a local table storing available emp tents.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TentsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_tents_name(),
            'filter_group_limit_clause': f'ORDER BY {TentsMeta.name}',
        }


class Employees(AsyncQueryDescriptor):
    """
    Query to a local table storing employees.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return EmployeeMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = EmployeesSqlFilterClauseGenerator.generate_positions_tribes_tents_filter(
                    position_ids=kwargs['position_ids'],
                    tribe_ids=kwargs['tribe_ids'],
                    tent_ids=kwargs['tent_ids'],
                )
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_employees_name(),
            'filter_group_limit_clause': f'{filter}\nORDER BY {EmployeeMeta.name}',
        }
