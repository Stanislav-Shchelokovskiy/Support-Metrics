from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import PositionsMeta


# yapf: disable
class PositionsRepository(SqliteRepository):
    """
    Interface to a local table storing available positions.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_positions_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return PositionsMeta.get_values()
