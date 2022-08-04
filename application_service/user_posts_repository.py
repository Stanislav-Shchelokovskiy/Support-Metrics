import os
import sqlite3
from pandas import DataFrame, read_sql
from pathlib import Path


class UserPostsRepository:

    def __init__(
        self,
        db_file_name: str = None,
    ):
        self.db_file = Path(db_file_name or os.environ['SQLITE_DATABASE'])
        self._db_connection: sqlite3.Connection = None
        self._db_connections_count: int = 0

    def _check_db_file_availability(self):
        if not self.db_file.exists():
            raise DbFileIsMissingException()

    def _connect(self) -> None:
        self._check_db_file_availability()
        self._disconnect()
        self._db_connection = sqlite3.connect(database=self.db_file)

    def _disconnect(self) -> None:
        if self._db_connection is not None:
            self._db_connection.close()
            self._db_connection = None

    def _connect_or_reuse_connection(self):
        if not self._db_connection:
            self._connect()
        self._acknowledge_connection()

    def _try_disconnect(self) -> None:
        self._remove_connection()
        if self._all_connections_removed():
            self._disconnect()

    def _acknowledge_connection(self) -> None:
        self._db_connections_count += 1

    def _remove_connection(self) -> None:
        self._db_connections_count -= 1
        if self._db_connections_count < 0:
            self._db_connections_count = 0

    def _all_connections_removed(self) -> bool:
        return not self._db_connections_count

    def _get_connection(self) -> sqlite3.Connection:
        return self._db_connection

    def get_available_tribes(self) -> list[str]:
        self._connect_or_reuse_connection()
        cursor = self._get_connection().cursor()
        available_tribes = [
            row[0] for row in cursor.execute(
                f"""SELECT DISTINCT {UserPoststByTribes.tribe_name}
                    FROM {os.environ['USER_POSTS_TABLE_NAME']}"""
            )
        ]
        self._try_disconnect()
        return available_tribes

    def get_user_posts(self, tribe_name: str) -> DataFrame:
        self._connect_or_reuse_connection()
        user_posts_df = read_sql(
            sql=f"""SELECT *
                    FROM {os.environ['USER_POSTS_TABLE_NAME']}
                    WHERE {UserPoststByTribes.tribe_name} LIKE '{tribe_name}'"""
            if tribe_name else f"""SELECT *
                    FROM {os.environ['USER_POSTS_TABLE_NAME']}""",
            con=self._get_connection(),
        )
        self._try_disconnect()
        return user_posts_df


class UserPoststByTribes:
    tribe_name = 'tribe_name'


class DbFileIsMissingException(Exception):
    pass