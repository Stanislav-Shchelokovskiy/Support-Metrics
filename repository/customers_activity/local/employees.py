from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    PositionsMeta,
    TribesMeta,
    EmployeesMeta,
)
from repository.customers_activity.local.sql_filters_generator.employees import EmployeesSqlFilterClauseGenerator


# yapf: disable
class EmpPositionsRepository(SqliteRepository):
    """
    Interface to a local table storing available emp positions.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_positions_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return PositionsMeta.get_values()


class EmpTribesRepository(SqliteRepository):
    """
    Interface to a local table storing available emp tribes.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_emp_tribes_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TribesMeta.get_values()


class EmployeesRepository(SqliteRepository):
    """
    Interface to a local table storing employees.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_employees_name(),
            'filter_group_limit_clause': EmployeesSqlFilterClauseGenerator.generate_positions_tribes_filter(
                    position_ids=kwargs['position_ids'],
                    tribe_ids=kwargs['tribe_ids'],
                ),
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [EmployeesMeta.crmid, EmployeesMeta.name]
