from typing import Iterable
from toolbox.sql import KnotMeta
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.meta.cat as cat
import sql_queries.index.path.remote as RemotePathIndex


class CATRepliesTypes(RepositoryAlchemyQueries):
    """
    Query to load cat replies types.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.replies_types

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **KnotMeta.get_attrs()}


class CATComponentsFeatures(RepositoryAlchemyQueries):
    """
    Query to load cat components and features.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.components_features

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **cat.CatComponentsFeatures.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return cat.CatComponentsFeatures.get_values()
