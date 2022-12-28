from toolbox.sql.repository import Repository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
)


class RepliesTypesRepository(Repository):
    """
    Loads CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_replies_types_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **ReplyTypesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ReplyTypesMeta.get_values()


class ComponentsFeaturesRepository(Repository):
    """
    Loads CAT components and features.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_components_features_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **ComponentsFeaturesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ComponentsFeaturesMeta.get_values()
