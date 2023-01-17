import requests
import json
import urllib3
from pandas import DataFrame
from toolbox.sql.sqlite_db import get_or_create_db
from sql_queries.index import CustomersActivityDBIndex
from repository.factory import RepositoryFactory, TablesBuilder
from repository.index_creation_expressions_repository import IndexCreationExpressionsRepository


urllib3.disable_warnings()


def _save_tables(tables: dict[str, DataFrame]):
    sqlitedb = get_or_create_db()
    sqlitedb.save_tables(
        tables=tables,
        create_index_expressions=IndexCreationExpressionsRepository.
        customers_activity_create_index_expressions,
    )


# yapf: disable
def load_tags():
    repository = RepositoryFactory.customers_activity.remote.create_tags_repository()
    df = repository.get_data()
    tbl_name = CustomersActivityDBIndex.get_tickets_tags_name()
    _save_tables(tables={tbl_name: df})


def load_groups():
    repository = RepositoryFactory.customers_activity.remote.create_groups_repository()
    df = repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_customers_groups_name(): df})

def load_tracked_groups(start_date: str):
    repository = RepositoryFactory.customers_activity.remote.create_tracked_groups_repository()
    df = repository.get_data(start_date=start_date)
    _save_tables(tables={CustomersActivityDBIndex.get_tracked_customers_groups_name(): df})

def load_replies_types():
    repository = RepositoryFactory.customers_activity.remote.create_replies_types_repository()
    df = repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_replies_types_name(): df})


def load_components_features():
    repository = RepositoryFactory.customers_activity.remote.create_components_features_repository()
    df = repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_components_features_name(): df})


def load_platforms_products():
    repository = RepositoryFactory.customers_activity.remote.create_platforms_products_repository()
    df = repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_platforms_products_name(): df})


def load_tickets_with_licenses(start_date: str, end_date: str):
    repository = RepositoryFactory.customers_activity.remote.create_tickets_with_licenses_repository()
    df = repository.get_data(start_date=start_date, end_date=end_date)
    _save_tables(tables={CustomersActivityDBIndex.get_tickets_with_licenses_name(): df})


def load_employees_iterations(start_date: str, end_date: str):
    repository = RepositoryFactory.customers_activity.remote.create_employees_iterations_repository()
    df = repository.get_data(start_date=start_date, end_date=end_date)
    _save_tables(tables={CustomersActivityDBIndex.get_employees_iterations_name(): df})


def load_tickets_types():
    types_str = requests.get(
        url='https://answerdesk-domain.hosting.devexpress.com/entityTypes?Company=c1f0951c-3885-44cf-accb-1a390f34c342',
        verify=False,
    ).text
    types = json.loads(types_str)['Page']
    df = DataFrame.from_records(data=types)
    df = df.rename(columns={'DisplayName': 'name', 'Id': 'id'})
    df = df.reset_index(drop=True)
    df = df[['name', 'id']]
    _save_tables(tables={CustomersActivityDBIndex.get_tickets_types_name(): df})


def load_license_statuses():
    repository = RepositoryFactory.customers_activity.remote.create_license_statuses_repository()
    df = repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_license_statuses_name(): df})


def load_conversion_statuses():
    repository = RepositoryFactory.customers_activity.remote.create_conversion_statuses_repository()
    df = repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_conversion_statuses_name(): df})


def build_tables(rank_period_offset: str):
    TablesBuilder.customers_activity.build_tickets_with_iterations(rank_period_offset=rank_period_offset)
    TablesBuilder.customers_activity.build_emp_positions()
    TablesBuilder.customers_activity.build_emp_tribes()
    TablesBuilder.customers_activity.build_employees()
    TablesBuilder.customers_activity.build_users()
# yapf: enable
