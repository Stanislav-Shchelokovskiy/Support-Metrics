from pandas import DataFrame
from toolbox.sql.sqlite_data_base import get_or_create_db
from sql_queries.index import CustomersActivityDBIndex
from repository.factory import RepositoryFactory


def _save_table(table: dict[str, DataFrame]):
    sqlitedb = get_or_create_db()
    sqlitedb.save_tables(table)


def load_tags():
    # yapf: disable
    tags_repository = RepositoryFactory.customers_activity.create_tags_repository()
    # yapf: enable
    df = tags_repository.get_data()
    _save_table({CustomersActivityDBIndex.get_tags_name(): df})


def load_groups():
    # yapf: disable
    groups_repository = RepositoryFactory.customers_activity.create_groups_repository()
    # yapf: enable
    df = groups_repository.get_data()
    _save_table({CustomersActivityDBIndex.get_groups_name(): df})


def load_tickets_with_iterations(start_date: str, end_date: str):
    # yapf: disable
    tickets_repository = RepositoryFactory.customers_activity.create_tickets_with_iterations_repository()
    df = tickets_repository.get_data(start_date=start_date, end_date=end_date)
    _save_table({CustomersActivityDBIndex.get_tickets_with_iterations_name(): df})
    # yapf: enable
