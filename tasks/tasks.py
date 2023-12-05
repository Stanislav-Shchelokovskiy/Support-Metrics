from pandas import DataFrame
from toolbox.utils.env import recalculate_from_beginning
from toolbox.sql.field import Field
from toolbox.sql.sql_query import SqlQuery
from toolbox.sql.query_executors.sqlite_query_executor import SQLiteNonQueryExecutor
from toolbox.sql.connections import SqliteConnection
from toolbox.sql.crud_queries.protocols import CRUDQuery
from toolbox.sql.crud_queries import (
    SqliteUpsertQuery,
    SqliteCreateTableQuery,
    SqliteCreateTableFromTableQuery,
    DeleteRowsOlderThanQuery,
    DropTableQuery,
)
from toolbox.sql.db_operations import SaveTableOperation
from toolbox.sql.repository import Repository
from toolbox.sql import MetaData
from repository import RepositoryFactory

import sql_queries.meta.employees as employees
import sql_queries.meta.platforms_products as platforms_products
import sql_queries.meta.cat as cat
import sql_queries.meta.customers as customers
import sql_queries.meta.aggs as aggs
import sql_queries.meta.tickets as tickets
import sql_queries.meta.tribes_tents as tribes_tents

import sql_queries.index.path.transform_load as TransformLoadPathIndex


def __save_table(cls: MetaData = MetaData, *queries: CRUDQuery):
    [
        SaveTableOperation(
            conn=SqliteConnection(),
            query=query,
            create_index_statements=cls.get_indices(),
        )() for query in queries
    ]


def __as_query_field(x: Field):
    return x.as_query_field()


# yapf: disable
def __create_table(
    repository: Repository,
    cls: MetaData,
    recreate=True,
    **kwargs,
):
    df: DataFrame = repository.get_data(**kwargs)
    __save_table(
        cls,
        SqliteCreateTableQuery(
            target_table_name=cls.get_name(),
            unique_key_fields=cls.get_key_fields(__as_query_field),
            values_fields=cls.get_conflicting_fields(__as_query_field, preserve_order=True),
            recreate=recreate,
        ),
        SqliteUpsertQuery(
            table_name=cls.get_name(),
            cols=df.columns,
            key_cols=cls.get_key_fields(),
            confilcting_cols=cls.get_conflicting_fields(),
            rows=df.itertuples(index=False),
        )
    )


def load_employees_iterations(
    start_date: str,
    end_date: str,
    employees_json: str,
):
    __create_table(
        repository=RepositoryFactory.remote.create_employees_iterations_repository(),
        cls=employees.EmployeesIterations,
        recreate=recalculate_from_beginning(),
        start_date=start_date,
        end_date=end_date,
        employees_json=employees_json,
    )
    return employees_json


def load_tickets(start_date: str, end_date: str):
    __create_table(
        repository=RepositoryFactory.remote.create_tickets_repository(),
        cls=aggs.Tickets,
        recreate=recalculate_from_beginning(),
        start_date=start_date,
        end_date=end_date,
    )


def load_platforms_products():
    __create_table(
        repository=RepositoryFactory.remote.create_platforms_products_repository(),
        cls=platforms_products.PlatformsProducts,
    )


def load_components_features():
    __create_table(
        repository=RepositoryFactory.remote.create_cat_components_features_repository(),
        cls=cat.CatComponentsFeatures,
    )


def load_groups():
    __create_table(
        repository=RepositoryFactory.remote.create_customers_groups_repository(),
        cls=customers.CustomersGroups,
    )


def load_tracked_groups(start_date: str, end_date: str):
    __create_table(
        repository=RepositoryFactory.remote.create_tracked_customers_groups_repository(),
        cls=customers.TrackedCustomersGroups,
        recreate=recalculate_from_beginning(),
        start_date=start_date,
        end_date=end_date,
    )


def load_employees(start_date: str, employees_json: str):
    __create_table(
        repository=RepositoryFactory.remote.create_employees_repository(),
        cls=employees.Employees,
        recreate=recalculate_from_beginning(),
        start_date=start_date,
        employees_json=employees_json,
    )
    return employees_json


def load_roles(employees_json: str):
    __create_table(
        repository=RepositoryFactory.remote.create_roles_repository(),
        cls=employees.Roles,
        employees_json=employees_json,
    )
    return employees_json


def load_csi():
    __create_table(
        repository=RepositoryFactory.remote.create_csi_repository(),
        cls=aggs.CSI,
    )


def load_resolution_time(years_of_history: str, employees_json: str):
    __create_table(
        repository=RepositoryFactory.remote.create_resolution_time_repository(),
        cls=aggs.ResolutionTime,
        years_of_history=years_of_history,
        employees_json=employees_json,
    )


def load_tags():
    __create_table(
        repository=RepositoryFactory.remote.create_tickets_tags_repository(),
        cls=tickets.TicketsTags,
    )


def load_replies_types():
    __create_table(
        repository=RepositoryFactory.remote.create_cat_replies_types_repository(),
        cls=cat.CatRepliesTypes,
    )


def load_frameworks():
    __create_table(
        repository=RepositoryFactory.remote.create_frameworks_repository(),
        cls=tickets.Frameworks,
    )


def load_operating_systems():
    __create_table(
        repository=RepositoryFactory.remote.create_operating_systems_repository(),
        cls=tickets.OperatingSystems,
    )


def load_builds():
    __create_table(
        repository=RepositoryFactory.remote.create_builds_repository(),
        cls=tickets.Builds,
    )


def load_severity():
    __create_table(
        repository=RepositoryFactory.remote.create_severity_repository(),
        cls=tickets.Severity,
    )


def load_ticket_statuses():
    __create_table(
        repository=RepositoryFactory.remote.create_ticket_statuses_repository(),
        cls=tickets.TicketStatuses,
    )


def load_ides():
    __create_table(
        repository=RepositoryFactory.remote.create_ides_repository(),
        cls=tickets.IDEs,
    )


def load_tribes():
    __create_table(
        repository=RepositoryFactory.remote.create_tribes_repository(),
        cls=tribes_tents.Tribes,
    )


def load_tents():
    __create_table(
        repository=RepositoryFactory.remote.create_tents_repository(),
        cls=tribes_tents.Tents,
    )


def load_tickets_types():
    __create_table(
        repository=RepositoryFactory.remote.create_tickets_types_repository(),
        cls=tickets.TicketsTypes,
    )


def load_license_statuses():
    __create_table(
        repository=RepositoryFactory.remote.create_license_statuses_repository(),
        cls=customers.LicenseStatuses,
    )


def load_conversion_statuses():
    __create_table(
        repository=RepositoryFactory.remote.create_conversion_statuses_repository(),
        cls=customers.ConversionStatuses,
    )


### transform staged data ###
__TICKETS_WITH_ITERATIONS_TEMP = 'TicketsWithIterationsTEMP'
def process_staged_data(
    rank_period_offset: str,
    years_of_history: str,
):
    __build_temp_tickets_with_iterations(rank_period_offset=rank_period_offset)
    __update_tickets_with_iterations()
    __build_employee_attr_tables()
    __build_customers()
    __post_process(years_of_history=years_of_history)


def __post_process(years_of_history: str):
    __execute(
        DeleteRowsOlderThanQuery(
            tbl=aggs.TicketsWithIterations.get_name(),
            date_field=aggs.TicketsWithIterations.creation_date,
            modifier=years_of_history,
        )
    )
    __execute(DropTableQuery(__TICKETS_WITH_ITERATIONS_TEMP))
    __execute(DropTableQuery(aggs.Tickets.get_name()))
    __execute(DropTableQuery(employees.EmployeesIterations.get_name()))
    __execute(DropTableQuery(aggs.ResolutionTime.get_name()))

    __execute('vacuum;')
    __execute('pragma optimize;')

    from toolbox.utils.env import reset_recalculate_from_beginning
    reset_recalculate_from_beginning()


def __build_temp_tickets_with_iterations(rank_period_offset: str):
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.tickets_with_iterations,
        format_params={
            **aggs.TicketsWithIterations.get_attrs(),
            **employees.EmployeesIterations.get_attrs(),
            'TicketsWithIterations': __TICKETS_WITH_ITERATIONS_TEMP,
            'CustomersTickets': aggs.Tickets.get_name(),
            'ResolutionTime': aggs.ResolutionTime.get_name(),
            'EmployeesIterations': employees.EmployeesIterations.get_name(),
            'rank_period_offset': rank_period_offset,
        }
    )
    __execute(query)


def __update_tickets_with_iterations():
    __save_table(
        aggs.TicketsWithIterations,
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=__TICKETS_WITH_ITERATIONS_TEMP,
            target_table_name=aggs.TicketsWithIterations.get_name(),
            unique_key_fields=aggs.TicketsWithIterations.get_key_fields(),
            values_fields=aggs.TicketsWithIterations.get_values(__as_query_field),
            unique_fields=aggs.TicketsWithIterations.get_index_fields(),
            recreate=recalculate_from_beginning(),
        ),
    )

    # align user_register_date with creation_date as they may mismatch
    # due to account transferring/merging.
    # user_register_date = MIN(creation_date, user_register_date)
    # this is necessary for BAM
    __execute(
        f"""
        UPDATE {aggs.TicketsWithIterations.get_name()} AS twi
        SET {aggs.TicketsWithIterations.user_register_date} = (
        SELECT MIN(d)
        FROM (  
                SELECT  MIN(twi_upper.{aggs.TicketsWithIterations.creation_date}) AS d
                FROM    {aggs.TicketsWithIterations.get_name()} AS twi_upper
                WHERE   twi_upper.{aggs.TicketsWithIterations.user_crmid} =  twi.{aggs.TicketsWithIterations.user_crmid}
                UNION
                SELECT  MIN(twi_lower.{aggs.TicketsWithIterations.user_register_date})
                FROM    {aggs.TicketsWithIterations.get_name()} AS twi_lower
                WHERE   twi_lower.{aggs.TicketsWithIterations.user_crmid} =  twi.{aggs.TicketsWithIterations.user_crmid}
             )
        )"""
    )


def __build_employee_attr_tables():
    __save_table(
        employees.Positions,
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=employees.Employees.get_name(),
            target_table_name=employees.Positions.get_name(),
            unique_key_fields=(employees.Employees.position_id.as_query_field(employees.Positions.id),),
            values_fields=(employees.Employees.position_name.as_query_field(employees.Positions.name),),
        ),
    )
    __save_table(
        employees.EmpTribes,
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=employees.Employees.get_name(),
            target_table_name=employees.EmpTribes.get_name(),
            unique_key_fields=(employees.Employees.tribe_id.as_query_field(employees.EmpTribes.id),),
            values_fields=(employees.Employees.tribe_name.as_query_field(employees.EmpTribes.name),),
        ),
    )
    __save_table(
        employees.EmpTents,
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=employees.Employees.get_name(),
            target_table_name=employees.EmpTents.get_name(),
            unique_key_fields=(employees.Employees.tent_id.as_query_field(employees.EmpTents.id),),
            values_fields=(employees.Employees.tent_name.as_query_field(employees.EmpTents.name),),
        ),
    )


def __build_customers():
    __save_table(
        customers.Customers,
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=aggs.TicketsWithIterations.get_name(),
            target_table_name=customers.Customers.get_name(),
            unique_key_fields=(aggs.TicketsWithIterations.user_crmid.as_query_field(customers.Customers.id),),
            values_fields=(aggs.TicketsWithIterations.user_id.as_query_field(customers.Customers.name),),
        ),
    )


def __execute(query):
    SQLiteNonQueryExecutor().execute_nonquery(query)
