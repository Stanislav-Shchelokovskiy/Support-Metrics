from toolbox.sql.sql_query import SqlQuery
from toolbox.sql.query_executors.sqlite_query_executor import SQLiteNonQueryExecutor

from sql_queries.meta import (
    TicketsWithIterationsMeta,
    EmployeesIterationsMeta,
    PositionsMeta,
    TribeMeta,
    TribesMeta,
    CustomersMeta,
    TentMeta,
    TentsMeta,
)
import sql_queries.index.db as DbIndex
import sql_queries.index.path.transform_load as TransformLoadPathIndex



def build_tickets_with_iterations(rank_period_offset: str):
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.tickets_with_iterations,
        format_params={
            **TicketsWithIterationsMeta.get_attrs(),
            **EmployeesIterationsMeta.get_attrs(),
            'TicketsWithIterations': DbIndex.tickets_with_iterations,
            'CustomersTickets': DbIndex.customers_tickets,
            'EmployeesIterations': DbIndex.employees_iterations,
            'rank_period_offset': rank_period_offset,
        }
    )
    __execute(query)


def build_emp_positions():
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.emp_positions,
        format_params={
            **PositionsMeta.get_attrs(),
            'EmployeesIterations': DbIndex.employees_iterations,
            'EmpPositions': DbIndex.emp_positions,
            'position_id': EmployeesIterationsMeta.position_id,
            'position_name': EmployeesIterationsMeta.position_name,
        }
    )
    __execute(query)


def build_emp_tribes():
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.emp_tribes,
        format_params={
            **TribeMeta.get_attrs(),
            **TribesMeta.get_attrs(),
            'EmpTribes': DbIndex.emp_tribes,
            'EmployeesIterations': DbIndex.employees_iterations,
        }
    )
    __execute(query)

def build_emp_tents():
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.emp_tents,
        format_params={
            **TentMeta.get_attrs(),
            **TentsMeta.get_attrs(),
            'EmpTents': DbIndex.emp_tents,
            'EmployeesIterations': DbIndex.employees_iterations,
        }
    )
    __execute(query)

def build_users():
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.customers,
        format_params={
            **CustomersMeta.get_attrs(),
            'Users': DbIndex.customers,
            'TicketsWithIterations': DbIndex.tickets_with_iterations,
        }
    )
    __execute(query)


def vacuum():
    __execute('vacuum;')


def analyze():
    __execute('pragma optimize;')


def __execute(query):
    SQLiteNonQueryExecutor().execute_nonquery(query)
