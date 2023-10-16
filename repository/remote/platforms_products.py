from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.meta import PlatformsProductsMeta
import sql_queries.index.path.extract as RemotePathIndex


class PlatformsProducts(RepositoryAlchemyQueries):
    """
    Query to load available platforms and products.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.platforms_products

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **PlatformsProductsMeta.get_attrs()}
