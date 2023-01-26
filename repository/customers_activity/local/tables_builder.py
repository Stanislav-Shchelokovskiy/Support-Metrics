from toolbox.sql.sql_query import SqlQuery
from toolbox.sql.query_executors.sqlite_query_executor import SQLiteNonQueryExecutor
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    EmployeesIterationsMeta,
    PositionsMeta,
    TribeMeta,
    TribesMeta,
    EmployeesMeta,
    CustomersMeta,
)


class TablesBuilder:
    #yapf: disable
    def build_tickets_with_iterations(self, rank_period_offset: str):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_tickets_with_iterations_path(),
            format_params={
                **TicketsWithIterationsMeta.get_attrs(),
                **EmployeesIterationsMeta.get_attrs(),
                'TicketsWithIterations': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
                'CustomersTickets': CustomersActivityDBIndex.get_customers_tickets_name(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
                'rank_period_offset': rank_period_offset,
            }
        )
        SQLiteNonQueryExecutor().execute_non_query(query)

    def build_emp_positions(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_emp_positions_path(),
            format_params={
                **PositionsMeta.get_attrs(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
                'EmpPositions': CustomersActivityDBIndex.get_emp_positions_name(),
                'position_id': EmployeesIterationsMeta.position_id,
                'position_name': EmployeesIterationsMeta.position_name,
            }
        )
        SQLiteNonQueryExecutor().execute_non_query(query)

    def build_emp_tribes(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_emp_tribes_path(),
            format_params={
                **TribeMeta.get_attrs(),
                **TribesMeta.get_attrs(),
                'EmpTribes': CustomersActivityDBIndex.get_emp_tribes_name(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
            }
        )
        SQLiteNonQueryExecutor().execute_non_query(query)

    def build_employees(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_employees_path(),
            format_params={
                **EmployeesMeta.get_attrs(),
                'Employees': CustomersActivityDBIndex.get_employees_name(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
            }
        )
        SQLiteNonQueryExecutor().execute_non_query(query)

    def build_users(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_customers_path(),
            format_params={
                **CustomersMeta.get_attrs(),
                'Users': CustomersActivityDBIndex.get_customers_name(),
                'TicketsWithIterations': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
            }
        )
        SQLiteNonQueryExecutor().execute_non_query(query)

    def vacuum(self):
        SQLiteNonQueryExecutor().execute_script_non_query('vacuum;')

    def run_analyze(self):
        SQLiteNonQueryExecutor().execute_script_non_query('pragma optimize;')
