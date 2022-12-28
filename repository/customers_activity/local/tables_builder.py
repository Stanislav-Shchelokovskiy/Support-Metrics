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

    def build_positions(self):
        query = SqlQuery(
            query_file_path=CustomersActivitySqlPathIndex.get_positions_path(),
            format_params={
                **PositionsMeta.get_attrs(),
                'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
                'Positions': CustomersActivityDBIndex.get_positions_name(),
                'pos_id': EmployeesIterationsMeta.pos_id,
                'pos_name': EmployeesIterationsMeta.pos_name,
            }
        )
        query_executor = SQLitePostQueryExecutor()
        query_executor.execute(query)
