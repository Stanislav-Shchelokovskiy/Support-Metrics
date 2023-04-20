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
    CustomersMeta,
    TentMeta,
    TentsMeta,
)


def build_tickets_with_iterations(rank_period_offset: str):
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
    __execute(query)


def build_emp_positions():
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
    __execute(query)


def build_emp_tribes():
    query = SqlQuery(
        query_file_path=CustomersActivitySqlPathIndex.get_emp_tribes_path(),
        format_params={
            **TribeMeta.get_attrs(),
            **TribesMeta.get_attrs(),
            'EmpTribes': CustomersActivityDBIndex.get_emp_tribes_name(),
            'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
        }
    )
    __execute(query)

def build_emp_tents():
    query = SqlQuery(
        query_file_path=CustomersActivitySqlPathIndex.get_emp_tents_path(),
        format_params={
            **TentMeta.get_attrs(),
            **TentsMeta.get_attrs(),
            'EmpTents': CustomersActivityDBIndex.get_emp_tents_name(),
            'EmployeesIterations': CustomersActivityDBIndex.get_employees_iterations_name(),
        }
    )
    __execute(query)

def build_users():
    query = SqlQuery(
        query_file_path=CustomersActivitySqlPathIndex.get_customers_path(),
        format_params={
            **CustomersMeta.get_attrs(),
            'Users': CustomersActivityDBIndex.get_customers_name(),
            'TicketsWithIterations': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
        }
    )
    __execute(query)


def vacuum():
    __execute('vacuum;')


def analyze():
    __execute('pragma optimize;')


def __execute(query):
    SQLiteNonQueryExecutor().execute_nonquery(query)
