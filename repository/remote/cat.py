from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.meta import (
    CATRepliesTypesMeta,
    CATComponentsFeaturesMeta,
)


class CATRepliesTypes(RepositoryAlchemyQueries):
    """
    Query to load cat replies types.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_replies_types_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **CATRepliesTypesMeta.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return CATRepliesTypesMeta.get_values()


class CATComponentsFeatures(RepositoryAlchemyQueries):
    """
    Query to load cat components and features.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_components_features_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **CATComponentsFeaturesMeta.get_attrs()}

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return CATComponentsFeaturesMeta.get_values()
