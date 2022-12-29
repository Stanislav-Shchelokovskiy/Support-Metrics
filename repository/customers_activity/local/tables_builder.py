from toolbox.sql.sql_query import SqlQuery
from toolbox.sql.query_executors.sqlite_query_executor import SQLitePostQueryExecutor
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
)


class TablesBuilder:
    #yapf: disable
    def build_tickets_with_iterations(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_tickets_with_iterations_path(),
            format_params={
                **TicketsWithIterationsMeta.get_attrs(),
                **EmployeesIterationsMeta.get_attrs(),
                'TicketsWithIterations': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
                'TicketsWithLicenses': CustomersActivityDBIndex.get_tickets_with_licenses_name(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
            }
        )
        query_executor = SQLitePostQueryExecutor()
        query_executor.execute(query)

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
        query_executor = SQLitePostQueryExecutor()
        query_executor.execute(query)

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
        query_executor = SQLitePostQueryExecutor()
        query_executor.execute(query)

    def build_employees(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_employees_path(),
            format_params={
                **EmployeesMeta.get_attrs(),
                'Employees': CustomersActivityDBIndex.get_employees_name(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
            }
        )
        query_executor = SQLitePostQueryExecutor()
        query_executor.execute(query)
