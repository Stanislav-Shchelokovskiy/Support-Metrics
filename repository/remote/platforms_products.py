from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.meta.platforms_products as platforms_products
import sql_queries.index.path.remote as RemotePathIndex


class PlatformsProducts(RepositoryAlchemyQueries):
    """
    Query to load available platforms and products.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.platforms_products

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **platforms_products.PlatformsProducts.get_attrs()}
