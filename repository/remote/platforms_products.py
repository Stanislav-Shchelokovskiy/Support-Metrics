from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.meta import PlatformsProductsMeta


class PlatformsProducts(RepositoryAlchemyQueries):
    """
    Query to load available platforms and products.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_platforms_products_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **PlatformsProductsMeta.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return PlatformsProductsMeta.get_values()
