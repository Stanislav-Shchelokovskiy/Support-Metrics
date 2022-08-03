from pandas import DataFrame

from repositories.client_posts_by_tribes_repository import ClientPoststByTribesRepository
from sql.sqlite_data_base import SQLiteDataBase


def update_client_posts_by_tribes() -> None:
    repository = ClientPoststByTribesRepository()
    client_posts_by_tribe_df = repository.get_data()
    db = SQLiteDataBase()
    db.save_tables({
        'client_posts_by_tribe': client_posts_by_tribe_df,
    }, )
