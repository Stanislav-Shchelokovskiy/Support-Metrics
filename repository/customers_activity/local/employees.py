from typing import Iterable
from toolbox.sql.repository_queries import RepositoryQueries
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    PositionsMeta,
    TribesMeta,
    EmployeesMeta,
)
from repository.customers_activity.local.generators.filters_generators.employees import EmployeesSqlFilterClauseGenerator


# yapf: disable
class EmpPositions(RepositoryQueries):
    """
    Interface to a local table storing available emp positions.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_positions_name(),
            'filter_group_limit_clause': f'ORDER BY {PositionsMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return PositionsMeta.get_values()


class EmpTribes(RepositoryQueries):
    """
    Interface to a local table storing available emp tribes.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_tribes_name(),
            'filter_group_limit_clause': f'ORDER BY {TribesMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TribesMeta.get_values()


class Employees(RepositoryQueries):
    """
    Interface to a local table storing employees.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        filter = EmployeesSqlFilterClauseGenerator.generate_positions_tribes_filter(
                    position_ids=kwargs['position_ids'],
                    tribe_ids=kwargs['tribe_ids'],
                )
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_employees_name(),
            'filter_group_limit_clause': f'{filter}\nORDER BY {EmployeesMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return (EmployeesMeta.crmid, EmployeesMeta.name,)
