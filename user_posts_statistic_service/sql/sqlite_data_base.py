import os
import sqlite3
from pandas import DataFrame
from pathlib import Path


class SQLiteDataBase:

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
       # self._check_db_file_availability()
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

    def save_tables(self, tables: dict[str, DataFrame]) -> None:
        self._connect_or_reuse_connection()
        if tables is not None:
            for k, v in tables.items():
                v.to_sql(
                    name=k,
                    con=self._get_connection(),
                    if_exists='replace',
                    index=False,
                )
        self._try_disconnect()


class DbFileIsMissingException(Exception):
    pass