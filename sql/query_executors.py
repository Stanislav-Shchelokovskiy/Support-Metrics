import os
import sqlite3
from typing import Any, Dict, List, NamedTuple
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from pandas import DataFrame, read_sql
from abc import ABC, abstractmethod

from sql.sql_query import SqlQuery


class ConnectionParams(NamedTuple):
    user: str
    password: str
    server: str
    data_base: str


class SqlQueryExecutor(ABC):
    """
    Executes and sql query passed to the execute method.
    """

    @abstractmethod
    def execute(
        self,
        sql_query: SqlQuery,
        kargs: Dict[str, Any],
    ) -> DataFrame:
        pass

    def execute_many(
        self,
        sql_queries: List[SqlQuery],
        kargs: Dict[str, Any],
    ) -> DataFrame:
        pass

    def _execute_sql_query(
        self,
        sql_query: SqlQuery,
        connection: Any,
        kargs: Dict[str, Any],
    ) -> DataFrame:
        return read_sql(
            sql=sql_query.get_query(),
            con=connection,
            **kargs,
        )


class MSSqlQueryExecutor(SqlQueryExecutor):

    def __init__(
        self,
        user_env: str = 'SQL_USER',
        password_env: str = 'SQL_PASSWORD',
        server_env: str = 'SQL_SERVER',
        data_base_env: str = 'SQL_DATABASE',
    ):
        self.user_env = user_env
        self.password_env = password_env
        self.server_env = server_env
        self.data_base_env = data_base_env

    def _get_connection_params(self) -> ConnectionParams:
        return ConnectionParams(
            user=os.environ[self.user_env],
            password=os.environ[self.password_env],
            server=os.environ[self.server_env],
            data_base=os.environ[self.data_base_env],
        )

    def _create_engine(self) -> Engine:
        params = self._get_connection_params()
        return create_engine(
            'mssql+pyodbc://' + params.user + ':' + params.password + '@'
            + params.server + '/' + params.data_base
            + '?driver=ODBC Driver 17 for SQL Server',
        )

    def execute(
        self,
        sql_query: SqlQuery,
        kargs: Dict[str, Any] = {},
    ) -> DataFrame:
        engine = self._create_engine()
        query_result = self._execute_sql_query(
            sql_query=sql_query,
            connection=engine,
            kargs=kargs,
        )
        engine.dispose()
        return query_result


class SQLiteQueryExecutor(SqlQueryExecutor):

    def __init__(
        self,
        data_base: str = None,
    ):
        self.data_base = data_base or os.environ['SQLITE_DATABASE']
        self.__connection: sqlite3.Connection = None
        self.__auto_close_connection: bool = False

    def connect(self):
        self.disconnect()
        self.__connection = sqlite3.connect(database=self.data_base)

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None

    def __try_disconnect(self):
        if self.__auto_close_connection:
            self.disconnect()
            self.__auto_close_connection = False

    def __try_connect(self):
        if not self.__connection:
            self.__auto_close_connection = True
            self.connect()

    def execute(
        self,
        sql_query: SqlQuery,
        source_tables: Dict[str, DataFrame],
        kargs: Dict[str, Any] = {},
    ) -> DataFrame:
        self.__try_connect()

        if source_tables is not None:
            for k, v in source_tables.items():
                v.to_sql(name=k, con=self.__connection)

        query_result = self._execute_sql_query(
            sql_query=sql_query,
            connection=self.__connection,
            kargs=kargs,
        )

        self.__try_disconnect()
        return query_result

    def execute_many(
        self,
        sql_queries: List[SqlQuery],
        kargs: Dict[str, Any] = {},
    ) -> DataFrame:
        self.__try_connect()
        cursor = self.__connection.cursor()

        for sql_query in sql_queries[:-1]:
            params = sql_query.get_params()
            query = sql_query.get_query()
            if params is None:
                cursor = cursor.execute(query)
            else:
                for param in params:
                    cursor = cursor.execute(
                        query,
                        param,
                    )

        query_result = self._execute_sql_query(
            sql_query=sql_queries[-1],
            connection=self.__connection,
            kargs=kargs,
        )
        self.__try_disconnect()
        return query_result
