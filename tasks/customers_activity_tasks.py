from pandas import DataFrame
from toolbox.sql.sqlite_db import get_or_create_db
from sql_queries.index import CustomersActivityDBIndex
from repository.factory import RepositoryFactory


def _save_table(table: dict[str, DataFrame]):
    sqlitedb = get_or_create_db()
    sqlitedb.save_tables(table)


    # yapf: disable
def load_tags():
    tags_repository = RepositoryFactory.customers_activity.remote.create_tags_repository()
    df = tags_repository.get_data()
    _save_table({CustomersActivityDBIndex.get_tickets_tags_name(): df})


def load_groups():
    groups_repository = RepositoryFactory.customers_activity.remote.create_groups_repository()
    df = groups_repository.get_data()
    _save_table({CustomersActivityDBIndex.get_customers_groups_name(): df})


def load_tickets_with_iterations(start_date: str, end_date: str):
    tickets_repository = RepositoryFactory.customers_activity.remote.create_tickets_with_iterations_repository()
    df = tickets_repository.get_data(start_date=start_date, end_date=end_date)
    _save_table({CustomersActivityDBIndex.get_tickets_with_iterations_name(): df})


def fill_tickets_types():
    tickets_types_repository = RepositoryFactory.customers_activity.remote.create_tickets_types_repository()
    df = tickets_types_repository.get_data()
    _save_table({CustomersActivityDBIndex.get_tickets_types_name(): df})
# yapf: enable
