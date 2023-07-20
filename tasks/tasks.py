import os
import json
import toolbox.utils.network as Network
from pandas import DataFrame
from toolbox.sql.connections import SqliteConnection
from toolbox.sql.crud_queries.protocols import CRUDQuery
from toolbox.sql.db_operations import SaveTableOperationDF, DFToCRUDQueryMapper
from toolbox.sql.repository import Repository
from repository import (
    RepositoryFactory,
    TablesBuilder,
    get_create_index_statements,
    get_create_table_statements,
)
import sql_queries.index.db as DbIndex



def _save_tables(*queries: CRUDQuery):
    [
        SaveTableOperationDF(
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
        )
    )


# yapf: disable


def load_tags():
    _save_table(
        tbl_name=DbIndex.tickets_tags,
        repository=RepositoryFactory.remote.create_tickets_tags_repository(),
    )


def load_groups():
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


def load_replies_types():
    _save_table(
        tbl_name=DbIndex.cat_replies_types,
        repository=RepositoryFactory.remote.create_cat_replies_types_repository(),
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


def load_tickets_types():
    _save_table(
        tbl_name=DbIndex.tickets_types,
        repository=RepositoryFactory.remote.create_tickets_types_repository(),
    )


def load_frameworks():
    _save_table(
        tbl_name=DbIndex.frameworks,
        repository=RepositoryFactory.remote.create_frameworks_repository(),
    )


def load_operating_systems():
    _save_table(
        tbl_name=DbIndex.operating_systems,
        repository=RepositoryFactory.remote.create_operating_systems_repository(),
    )


def load_builds():
    _save_table(
        tbl_name=DbIndex.builds,
        repository=RepositoryFactory.remote.create_builds_repository(),
    )


def load_severity_values():
    _save_table(
        tbl_name=DbIndex.severity,
        repository=RepositoryFactory.remote.create_severity_repository(),
    )


def load_ticket_statuses():
    _save_table(
        tbl_name=DbIndex.ticket_statuses,
        repository=RepositoryFactory.remote.create_ticket_statuses_repository(),
    )


def load_ides():
    _save_table(
        tbl_name=DbIndex.ides,
        repository=RepositoryFactory.remote.create_ides_repository(),
    )


def load_tribes():
    tribes_str = Network.get_data(end_point=f'http://{os.environ["QUERY_SERVICE"]}/get_available_tribes')
    tribes = json.loads(tribes_str)
    df = DataFrame.from_records(data=tribes)
    df = df.reset_index(drop=True)
    _save_tables(DFToCRUDQueryMapper(
            tbl_name=DbIndex.tribes,
            df=df,
        )
    )


def load_tents():
    tents_str = Network.get_data(end_point=f'http://{os.environ["QUERY_SERVICE"]}/get_tents')
    tents = json.loads(tents_str)
    df = DataFrame.from_records(data=tents)
    df = df.reset_index(drop=True)
    _save_tables(DFToCRUDQueryMapper(
            tbl_name=DbIndex.tents,
            df=df,
        )
    )


def load_license_statuses():
    _save_table(
        tbl_name=DbIndex.license_statuses,
        repository=RepositoryFactory.remote.create_license_statuses_repository(),
    )


def load_conversion_statuses():
    _save_table(
        tbl_name=DbIndex.conversion_statuses,
        repository=RepositoryFactory.remote.create_conversion_statuses_repository(),
    )

def load_csi():
    _save_table(
        tbl_name=DbIndex.csi,
        repository=RepositoryFactory.remote.create_csi_repository(),
    )


def process_staged_data(rank_period_offset: str):
    TablesBuilder.build_tickets_with_iterations(rank_period_offset=rank_period_offset)
    TablesBuilder.build_emp_positions()
    TablesBuilder.build_emp_tribes()
    TablesBuilder.build_emp_tents()
    TablesBuilder.build_users()
    TablesBuilder.vacuum()
    TablesBuilder.analyze()
