from typing import Iterable
from toolbox.sql.repository import SqlServerRepository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    CATRepliesTypesMeta,
    CATComponentsFeaturesMeta,
)


class CATRepliesTypesRepository(SqlServerRepository):
    """
    Loads CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_replies_types_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **CATRepliesTypesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return CATRepliesTypesMeta.get_values()


class CATComponentsFeaturesRepository(SqlServerRepository):
    """
    Loads CAT components and features.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_components_features_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **CATComponentsFeaturesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return CATComponentsFeaturesMeta.get_values()
