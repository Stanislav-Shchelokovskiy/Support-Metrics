from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    CATRepliesTypesMeta,
    CATComponentsFeaturesMeta,
)
from repository.customers_activity.local.generators.filters_generators.cat import CATSqlFilterClauseGenerator


# yapf: disable
class CATRepliesTypesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_cat_replies_types_name(),
            'filter_group_limit_clause': f'ORDER BY {CATRepliesTypesMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CATRepliesTypesMeta.get_values()


class CATComponentsRepository(SqliteRepository):
    """
    Interface to a local table storing CAT components.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_components_filter(tribe_ids=kwargs['tribe_ids'])
        cols = ', '.join(self.get_must_have_columns(kwargs))
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_cat_components_features_name(),
            'filter_group_limit_clause': f'{filter}\nGROUP BY {cols}\nORDER BY {CATComponentsFeaturesMeta.component_name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            CATComponentsFeaturesMeta.component_id,
            CATComponentsFeaturesMeta.component_name,
        ]


class CATFeaturesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT features
    available for the specified components.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_features_filter(
                    tribe_ids=kwargs['tribe_ids'],
                    component_ids=kwargs['component_ids'],
                )
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_cat_components_features_name(),
            'filter_group_limit_clause': f'{filter}\nORDER BY {CATComponentsFeaturesMeta.feature_name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            CATComponentsFeaturesMeta.feature_id,
            CATComponentsFeaturesMeta.feature_name,
        ]
