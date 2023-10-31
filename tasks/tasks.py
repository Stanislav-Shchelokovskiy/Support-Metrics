from pandas import DataFrame
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
from toolbox.sql.db_operations import SaveTableOperationDF, DFToCRUDQueryMapper, SaveTableOperation
from toolbox.sql.repository import Repository
from toolbox.sql import KnotMeta, IntKnotMeta
from repository import RepositoryFactory

from sql_queries.transform_load import (
    get_create_index_statements,
    get_create_table_statements,
)

from sql_queries.meta import (
    EmployeesIterationsMeta,
    TicketsWithPropertiesMeta,
    CustomersGroupsMeta,
    ConversionStatusesMeta,
    TicketsWithIterationsMeta,
    EmployeesMeta,
    BaselineAlignedCustomersGroupsMeta,
)
import sql_queries.index.name as name_index
import sql_queries.index.path.transform_load as TransformLoadPathIndex
from toolbox.utils.env import recalculate_from_beginning


def __save_tables(
    *queries: CRUDQuery,
    op=SaveTableOperation,
):
    [
        op(
            conn=SqliteConnection(),
            query=query,
            tables_defs=get_create_table_statements(),
            create_index_statements=get_create_index_statements(),
        )() for query in queries
    ]


def __save_table(tbl_name: str, repository: Repository, **kwargs):
    __save_tables(
        DFToCRUDQueryMapper(
            tbl_name=tbl_name,
            df=repository.get_data(**kwargs),
        ),
        op=SaveTableOperationDF,
    )


# yapf: disable
def load_groups():
    df = RepositoryFactory.remote.create_customers_groups_repository().get_data()
    __save_tables(
         SqliteCreateTableQuery(
            target_table_name=name_index.customers_groups,
            unique_key_fields=CustomersGroupsMeta.get_key_fields(lambda x: x.as_query_field()),
            values_fields=CustomersGroupsMeta.get_conflicting_fields(lambda x: x.as_query_field(), preserve_order=True),
            recreate=True,
        ),
        SqliteUpsertQuery(
            table_name=name_index.customers_groups,
            cols=df.columns,
            key_cols=CustomersGroupsMeta.get_key_fields(),
            confilcting_cols=CustomersGroupsMeta.get_conflicting_fields(),
            rows=df.itertuples(index=False),
        )
    )


def load_tracked_groups(start_date: str, end_date: str):
    df = RepositoryFactory.remote.create_tracked_customers_groups_repository().get_data(start_date=start_date,end_date=end_date,)
    __save_tables(
        SqliteCreateTableQuery(
            target_table_name=name_index.tracked_customers_groups,
            unique_key_fields=BaselineAlignedCustomersGroupsMeta.get_key_fields(lambda x: x.as_query_field()),
            values_fields=BaselineAlignedCustomersGroupsMeta.get_conflicting_fields(lambda x: x.as_query_field(), preserve_order=True),
            recreate=recalculate_from_beginning(),
        ),
        SqliteUpsertQuery(
            table_name=name_index.tracked_customers_groups,
            cols=df.columns,
            key_cols=BaselineAlignedCustomersGroupsMeta.get_key_fields(),
            confilcting_cols=BaselineAlignedCustomersGroupsMeta.get_conflicting_fields(),
            rows=df.itertuples(index=False),
        )
    )


def load_components_features():
    __save_table(
        tbl_name=name_index.cat_components_features,
        repository=RepositoryFactory.remote.create_cat_components_features_repository(),
    )


def load_platforms_products():
    __save_table(
        tbl_name=name_index.platforms_products,
        repository=RepositoryFactory.remote.create_platforms_products_repository(),
    )


def load_customers_tickets(start_date: str, end_date: str):
    __save_table(
        tbl_name=name_index.customers_tickets,
        repository=RepositoryFactory.remote.create_customers_tickets_repository(),
        start_date=start_date,
        end_date=end_date,
    )


def load_employees_iterations(start_date: str, end_date: str, employees_json: str):
    __save_table(
        tbl_name=name_index.employees_iterations,
        repository=RepositoryFactory.remote.create_employees_iterations_repository(),
        start_date=start_date,
        end_date=end_date,
        employees_json=employees_json,
    )


def load_employees(start_date: str, employees_json: str):
    df = RepositoryFactory.remote.create_employees_repository().get_data(
        start_date=start_date,
        employees_json=employees_json,
    )
    __save_tables(
        SqliteCreateTableQuery(
            target_table_name=name_index.employees,
            unique_key_fields=EmployeesMeta.get_key_fields(lambda x: x.as_query_field()),
            values_fields=EmployeesMeta.get_conflicting_fields(lambda x: x.as_query_field(), preserve_order=True),
            recreate=recalculate_from_beginning(),
        ),
        SqliteUpsertQuery(
            table_name=name_index.employees,
            cols=df.columns,
            key_cols=EmployeesMeta.get_key_fields(),
            confilcting_cols=EmployeesMeta.get_conflicting_fields(),
            rows=df.itertuples(index=False),
        )
    )


def load_csi():
    __save_table(
        tbl_name=name_index.csi,
        repository=RepositoryFactory.remote.create_csi_repository(),
    )


### Knots ###
def __as_query_field(x: Field):
    return x.as_query_field()


def __save_knot(
    repository: Repository,
    table_name: str,
    cls=KnotMeta,
    **kwargs,
):
    df: DataFrame = repository.get_data(**kwargs)

    __save_tables(
        SqliteCreateTableQuery(
            target_table_name=table_name,
            unique_key_fields=cls.get_key_fields(__as_query_field),
            values_fields=cls.get_conflicting_fields(__as_query_field, preserve_order=True),
            recreate=True,
        ),
        SqliteUpsertQuery(
            table_name=table_name,
            cols=df.columns,
            key_cols=cls.get_key_fields(),
            confilcting_cols=cls.get_conflicting_fields(),
            rows=df.itertuples(index=False),
        )
    )


def load_tags():
    __save_knot(
        repository=RepositoryFactory.remote.create_tickets_tags_repository(),
        table_name=name_index.tickets_tags,
    )


def load_replies_types():
    __save_knot(
        repository=RepositoryFactory.remote.create_cat_replies_types_repository(),
        table_name=name_index.cat_replies_types,
    )


def load_frameworks():
    __save_knot(
        repository=RepositoryFactory.remote.create_frameworks_repository(),
        table_name=name_index.frameworks,
    )


def load_operating_systems():
    __save_knot(
        repository=RepositoryFactory.remote.create_operating_systems_repository(),
        table_name=name_index.operating_systems,
    )


def load_builds():
    __save_knot(
        repository=RepositoryFactory.remote.create_builds_repository(),
        table_name=name_index.builds,
    )


def load_severity():
    __save_knot(
        repository=RepositoryFactory.remote.create_severity_repository(),
        table_name=name_index.severity,
    )


def load_ticket_statuses():
    __save_knot(
        repository=RepositoryFactory.remote.create_ticket_statuses_repository(),
        table_name=name_index.ticket_statuses,
    )


def load_ides():
    __save_knot(
        repository=RepositoryFactory.remote.create_ides_repository(),
        table_name=name_index.ides,
    )


def load_tribes():
    __save_knot(
        repository=RepositoryFactory.remote.create_tribes_repository(),
        table_name=name_index.tribes,
    )


def load_tents():
    __save_knot(
        repository=RepositoryFactory.remote.create_tents_repository(),
        table_name=name_index.tents,
    )



def load_tickets_types():
    __save_knot(
        repository=RepositoryFactory.remote.create_tickets_types_repository(),
        table_name=name_index.tickets_types,
        cls=IntKnotMeta,
    )


def load_license_statuses():
    __save_knot(
        repository=RepositoryFactory.remote.create_license_statuses_repository(),
        table_name=name_index.license_statuses,
        cls=IntKnotMeta,
    )


def load_conversion_statuses():
    __save_knot(
        repository=RepositoryFactory.remote.create_conversion_statuses_repository(),
        table_name=name_index.conversion_statuses,
        cls=ConversionStatusesMeta,
    )


### transform staged data ###
def process_staged_data(
    rank_period_offset: str,
    years_of_history:str,
):
    __build_temp_tickets_with_iterations(rank_period_offset=rank_period_offset)
    __update_tickets_with_iterations()
    __build_employee_attr_tables()
    __build_customers()
    __post_process(years_of_history=years_of_history)


def __post_process(years_of_history: str):
    __execute(DeleteRowsOlderThanQuery(
            tbl=name_index.tickets_with_iterations,
            date_field=TicketsWithIterationsMeta.creation_date,
            modifier=years_of_history,
        )
    )
    __execute(DropTableQuery(name_index.tickets_with_iterations_temp))
    __execute(DropTableQuery(name_index.customers_tickets))
    __execute(DropTableQuery(name_index.employees_iterations))

    __execute('vacuum;')
    __execute('pragma optimize;')

    from toolbox.utils.env import reset_recalculate_from_beginning
    reset_recalculate_from_beginning()


def __build_temp_tickets_with_iterations(rank_period_offset: str):
    query = SqlQuery(
        query_file_path=TransformLoadPathIndex.tickets_with_iterations,
        format_params={
            **TicketsWithIterationsMeta.get_attrs(),
            **EmployeesIterationsMeta.get_attrs(),
            'TicketsWithIterations': name_index.tickets_with_iterations_temp,
            'CustomersTickets': name_index.customers_tickets,
            'EmployeesIterations': name_index.employees_iterations,
            'rank_period_offset': rank_period_offset,
        }
    )
    __execute(query)


def __update_tickets_with_iterations():
    __save_tables(
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=name_index.tickets_with_iterations_temp,
            target_table_name=name_index.tickets_with_iterations,
            unique_key_fields=None,
            values_fields=TicketsWithIterationsMeta.get_values(lambda x: x.as_query_field()),
            unique_fields=TicketsWithIterationsMeta.get_key_fields(),
            recreate=recalculate_from_beginning(),
        ),
    )

    # align user_register_date with creation_date as they may mismatch
    # due to account transferring/merging.
    # user_register_date = MIN(creation_date, user_register_date)
    # this is necessary for BAM
    __execute(f"""
        UPDATE {name_index.tickets_with_iterations} AS twi
        SET {TicketsWithIterationsMeta.user_register_date} = (
        SELECT MIN(d)
        FROM (  
                SELECT  MIN(twi_upper.{TicketsWithIterationsMeta.creation_date}) AS d
                FROM    {name_index.tickets_with_iterations} AS twi_upper
                WHERE   twi_upper.{TicketsWithIterationsMeta.user_crmid} =  twi.{TicketsWithIterationsMeta.user_crmid}
                UNION
                SELECT  MIN(twi_lower.{TicketsWithIterationsMeta.user_register_date})
                FROM    {name_index.tickets_with_iterations} AS twi_lower
                WHERE   twi_lower.{TicketsWithIterationsMeta.user_crmid} =  twi.{TicketsWithIterationsMeta.user_crmid}
             )
        )"""
    )


def __build_employee_attr_tables():
    __save_tables(
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=name_index.employees,
            target_table_name=name_index.emp_positions,
            unique_key_fields=(EmployeesMeta.position_id.as_query_field(KnotMeta.id),),
            values_fields=(EmployeesMeta.position_name.as_query_field(KnotMeta.name),),
        ),
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=name_index.employees,
            target_table_name=name_index.emp_tribes,
            unique_key_fields=(EmployeesMeta.tribe_id.as_query_field(KnotMeta.id),),
            values_fields=(EmployeesMeta.tribe_name.as_query_field(KnotMeta.name),),
        ),
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=name_index.employees,
            target_table_name=name_index.emp_tents,
            unique_key_fields=(EmployeesMeta.tent_id.as_query_field(KnotMeta.id),),
            values_fields=(EmployeesMeta.tent_name.as_query_field(KnotMeta.name),),
        ),
    )


def __build_customers():
    __save_tables(
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=name_index.tickets_with_iterations,
            target_table_name=name_index.customers,
            unique_key_fields=(TicketsWithPropertiesMeta.user_crmid.as_query_field(KnotMeta.id),),
            values_fields=(TicketsWithPropertiesMeta.user_id.as_query_field(KnotMeta.name),),
        ),
    )


def __execute(query):
    SQLiteNonQueryExecutor().execute_nonquery(query)
