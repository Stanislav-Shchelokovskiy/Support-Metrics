import os

from repositories.user_posts_by_tribes_repository import UserPoststByTribesRepository
from sql.sqlite_data_base import SQLiteDataBase


def update_client_posts_by_tribes() -> None:
    repository = UserPoststByTribesRepository()
    user_posts_by_tribe_df = repository.get_data()
    db = SQLiteDataBase()
    db.save_tables({
        os.environ['USER_POSTS_TABLE_NAME']: user_posts_by_tribe_df,
    }, )
