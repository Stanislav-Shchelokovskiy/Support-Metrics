from typing import Iterable
from toolbox.sql.repository import SqlServerRepository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import PlatformsProductsMeta


class PlatformsProductsRepository(SqlServerRepository):
    """
    Loads available platforms and products.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_platforms_products_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **PlatformsProductsMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return PlatformsProductsMeta.get_values()
