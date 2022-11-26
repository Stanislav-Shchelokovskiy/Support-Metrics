from toolbox.sql.repository import SqliteRepository
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


class TicketsWithIterationsRepository(SqliteRepository):
    """
    An interface to local table storing customers with their tickets and iterations.
    """

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
        return DF_to_JSON.convert(df.iloc[0], orient='index')


class CustomersGroupsRepository(SqliteRepository):
    """
    An interface to local table storing customers groups.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_select_all()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'table_name': CustomersActivityDBIndex.get_customers_groups_name(),
            'columns': ', '.join(CustomersGroupsMeta.get_values())
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()
