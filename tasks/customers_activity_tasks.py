from pandas import DataFrame
from toolbox.sql.sqlite_db import get_or_create_db
from sql_queries.index import CustomersActivityDBIndex
from repository.factory import RepositoryFactory
from repository.index_creation_expressions_repository import IndexCreationExpressionsRepository


def _save_tables(tables: dict[str, DataFrame]):
    sqlitedb = get_or_create_db()
    sqlitedb.save_tables(
        tables=tables,
        create_index_expressions=IndexCreationExpressionsRepository.customers_activity_create_index_expressions,
    )


# yapf: disable
def load_tags():
    tags_repository = RepositoryFactory.customers_activity.remote.create_tags_repository()
    df = tags_repository.get_data()
    tbl_name = CustomersActivityDBIndex.get_tickets_tags_name()
    _save_tables(tables={tbl_name: df})


def load_groups():
    groups_repository = RepositoryFactory.customers_activity.remote.create_groups_repository()
    df = groups_repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_customers_groups_name(): df})


def load_reply_types():
    reply_types_repository = RepositoryFactory.customers_activity.remote.create_reply_types_repository()
    df = reply_types_repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_reply_types_name(): df})


def load_controls_features():
    controls_features_repository = RepositoryFactory.customers_activity.remote.create_controls_features_repository()
    df = controls_features_repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_controls_features_name(): df})


def load_tickets_with_iterations(start_date: str, end_date: str):
    tickets_repository = RepositoryFactory.customers_activity.remote.create_tickets_with_iterations_repository()
    df = tickets_repository.get_data(start_date=start_date, end_date=end_date)
    _save_tables(tables={CustomersActivityDBIndex.get_tickets_with_iterations_name(): df})


def fill_tickets_types():
    tickets_types_repository = RepositoryFactory.customers_activity.remote.create_tickets_types_repository()
    df = tickets_types_repository.get_data()
    _save_tables(tables={CustomersActivityDBIndex.get_tickets_types_name(): df})
# yapf: enable
