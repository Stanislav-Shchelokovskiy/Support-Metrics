from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
)
from repository.customers_activity.local.filters_generators.cat import CATSqlFilterClauseGenerator


# yapf: disable
class ReplyTypesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_replies_types_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ReplyTypesMeta.get_values()


class ComponentsRepository(SqliteRepository):
    """
    Interface to a local table storing CAT components.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': f"DISTINCT {', '.join(self.get_must_have_columns(kwargs))}",
            'table_name': CustomersActivityDBIndex.get_components_features_name(),
            'filter_group_limit_clause': CATSqlFilterClauseGenerator.generate_components_filter(
                    tribe_ids=kwargs['tribe_ids']
                ),
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            ComponentsFeaturesMeta.component_id,
            ComponentsFeaturesMeta.component_name,
        ]


class FeaturesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT features
    available for the specified components.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_components_features_name(),
            'filter_group_limit_clause': CATSqlFilterClauseGenerator.generate_features_filter(
                    tribe_ids=kwargs['tribe_ids'],
                    component_ids=kwargs['component_ids'],
                ),
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            ComponentsFeaturesMeta.feature_id,
            ComponentsFeaturesMeta.feature_name,
        ]
# yapf: enable
