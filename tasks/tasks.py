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
)
import sql_queries.index.db as DbIndex
import sql_queries.index.path.transform_load as TransformLoadPathIndex


def _save_tables(
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


def _save_table(tbl_name: str, repository: Repository, **kwargs):
    _save_tables(
        DFToCRUDQueryMapper(
            tbl_name=tbl_name,
            df=repository.get_data(**kwargs),
        ),
        op=SaveTableOperationDF,
    )


# yapf: disable
def load_groups():
    _save_tables(
         SqliteCreateTableQuery(
            target_table_name=DbIndex.customers_groups,
            unique_key_fields=CustomersGroupsMeta.get_key_fields(lambda x: x.as_query_field()),
            values_fields=CustomersGroupsMeta.get_conflicting_fields(lambda x: x.as_query_field(), preserve_order=True),
            recreate=True,
        ),
    )
    _save_table(
        tbl_name=DbIndex.customers_groups,
        repository=RepositoryFactory.remote.create_customers_groups_repository(),
    )


def load_tracked_groups(start_date: str, end_date: str):
    _save_table(
        tbl_name=DbIndex.tracked_customers_groups,
        repository=RepositoryFactory.remote.create_tracked_customers_groups_repository(),
        start_date=start_date,
        end_date=end_date,
    )


def load_components_features():
    _save_table(
        tbl_name=DbIndex.cat_components_features,
        repository=RepositoryFactory.remote.create_cat_components_features_repository(),
    )


def load_platforms_products():
    _save_table(
        tbl_name=DbIndex.platforms_products,
        repository=RepositoryFactory.remote.create_platforms_products_repository(),
    )


def load_customers_tickets(start_date: str, end_date: str):
    _save_table(
        tbl_name=DbIndex.customers_tickets,
        repository=RepositoryFactory.remote.create_customers_tickets_repository(),
        start_date=start_date,
        end_date=end_date,
    )


def load_employees_iterations(start_date: str, end_date: str):
    _save_table(
        tbl_name=DbIndex.employees_iterations,
        repository=RepositoryFactory.remote.create_employees_iterations_repository(),
        start_date=start_date,
        end_date=end_date,
    )


def load_employees(start_date: str):
    _save_table(
        tbl_name=DbIndex.employees,
        repository=RepositoryFactory.remote.create_employees_repository(),
        start_date=start_date,
    )


def load_csi():
    _save_table(
        tbl_name=DbIndex.csi,
        repository=RepositoryFactory.remote.create_csi_repository(),
    )


### Knots ###
def as_query_field(x: Field):
    return x.as_query_field()


def __save_knot(
    repository: Repository,
    table_name: str,
    cls=KnotMeta,
    **kwargs,
):
    df: DataFrame = repository.get_data(**kwargs)

    _save_tables(
        SqliteCreateTableQuery(
            target_table_name=table_name,
            unique_key_fields=cls.get_key_fields(as_query_field),
            values_fields=cls.get_conflicting_fields(as_query_field, preserve_order=True),
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
        table_name=DbIndex.tickets_tags,
    )


def load_replies_types():
    __save_knot(
        repository=RepositoryFactory.remote.create_cat_replies_types_repository(),
        table_name=DbIndex.cat_replies_types,
    )


def load_frameworks():
    __save_knot(
        repository=RepositoryFactory.remote.create_frameworks_repository(),
        table_name=DbIndex.frameworks,
    )


def load_operating_systems():
    __save_knot(
        repository=RepositoryFactory.remote.create_operating_systems_repository(),
        table_name=DbIndex.operating_systems,
    )


def load_builds():
    __save_knot(
        repository=RepositoryFactory.remote.create_builds_repository(),
        table_name=DbIndex.builds,
    )


def load_severity():
    __save_knot(
        repository=RepositoryFactory.remote.create_severity_repository(),
        table_name=DbIndex.severity,
    )


def load_ticket_statuses():
    __save_knot(
        repository=RepositoryFactory.remote.create_ticket_statuses_repository(),
        table_name=DbIndex.ticket_statuses,
    )


def load_ides():
    __save_knot(
        repository=RepositoryFactory.remote.create_ides_repository(),
        table_name=DbIndex.ides,
    )


def load_tribes():
    __save_knot(
        repository=RepositoryFactory.remote.create_tribes_repository(),
        table_name=DbIndex.tribes,
    )


def load_tents():
    __save_knot(
        repository=RepositoryFactory.remote.create_tents_repository(),
        table_name=DbIndex.tents,
    )



def load_tickets_types():
    __save_knot(
        repository=RepositoryFactory.remote.create_tickets_types_repository(),
        table_name=DbIndex.tickets_types,
        cls=IntKnotMeta,
    )


def load_license_statuses():
    __save_knot(
        repository=RepositoryFactory.remote.create_license_statuses_repository(),
        table_name=DbIndex.license_statuses,
        cls=IntKnotMeta,
    )


def load_conversion_statuses():
    __save_knot(
        repository=RepositoryFactory.remote.create_conversion_statuses_repository(),
        table_name=DbIndex.conversion_statuses,
        cls=ConversionStatusesMeta,
    )



def process_staged_data(rank_period_offset: str):
    build_tickets_with_iterations(rank_period_offset=rank_period_offset)

    _save_tables(
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=DbIndex.employees_iterations,
            target_table_name=DbIndex.emp_positions,
            unique_key_fields=(EmployeesIterationsMeta.position_id.as_query_field(KnotMeta.id),),
            values_fields=(EmployeesIterationsMeta.position_name.as_query_field(KnotMeta.name),),
        ),
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=DbIndex.employees_iterations,
            target_table_name=DbIndex.emp_tribes,
            unique_key_fields=(EmployeesIterationsMeta.tribe_id.as_query_field(KnotMeta.id),),
            values_fields=(EmployeesIterationsMeta.tribe_name.as_query_field(KnotMeta.name),),
        ),
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=DbIndex.employees_iterations,
            target_table_name=DbIndex.emp_tents,
            unique_key_fields=(EmployeesIterationsMeta.tent_id.as_query_field(KnotMeta.id),),
            values_fields=(EmployeesIterationsMeta.tent_name.as_query_field(KnotMeta.name),),
        ),
        SqliteCreateTableFromTableQuery(
            source_table_or_subquery=DbIndex.tickets_with_iterations,
            target_table_name=DbIndex.customers,
            unique_key_fields=(TicketsWithPropertiesMeta.user_crmid.as_query_field(KnotMeta.id),),
            values_fields=(TicketsWithPropertiesMeta.user_id.as_query_field(KnotMeta.name),),
        ),
    )

    __execute('vacuum;')
    __execute('pragma optimize;')

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



def __execute(query):
    SQLiteNonQueryExecutor().execute_nonquery(query)
