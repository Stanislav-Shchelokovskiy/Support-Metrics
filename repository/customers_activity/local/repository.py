from toolbox.sql.base_repository import BaseRepository
from toolbox.sql.query_executors.sqlite_query_executor import SQLiteQueryExecutor
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from toolbox.utils.converters import DF_to_JSON, DateTimeColumnsConverter, Object_to_JSON
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    CustomersTagsMeta,
    CustomersActivityMeta,
    TicketsWithIterationsPeriodMeta,
)


class TicketsWithIterationsRepository(BaseRepository):
    """
    An interface to local table storing customers with their tickets and iterations.
    """

    def __init__(self) -> None:
        BaseRepository.__init__(self, query_executor=SQLiteQueryExecutor())

    def get_period(self) -> str:
        # yapf: disable
        df = self.execute_query(
                query_file_path=CustomersActivitySqlPathIndex.get_tickets_with_iterations_period_path(),
                query_format_params={
                    'table_name': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
                    **TicketsWithIterationsPeriodMeta.get_attrs(),
                }
            ).reset_index(drop=True)
        # yapf: enable
        # DateTimeColumnsConverter.convert(
        #     df,
        #     cols=TicketsWithIterationsPeriodMeta.get_values(),
        # )
        return DF_to_JSON.convert(df.iloc[0], orient='index')
