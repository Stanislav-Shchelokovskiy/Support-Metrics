from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    CATRepliesTypesMeta,
    CATComponentsMeta,
    CATFeaturesMeta,
)
import repository.customers_activity.local.generators.filters_generators.cat as CATSqlFilterClauseGenerator


class CATRepliesTypes(AsyncQueryDescriptor):
    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CATRepliesTypesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
        'columns': ', '.join(self.get_fields(kwargs)),
        'table_name': CustomersActivityDBIndex.get_cat_replies_types_name(),
        'filter_group_limit_clause': f'ORDER BY {CATRepliesTypesMeta.name}',
    }


class CATComponents(AsyncQueryDescriptor):
    """
    Query to a local table storing CAT components.
    """
    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CATComponentsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_components_filter(tent_ids=kwargs['tent_ids'])
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_cat_components_features_name(),
            'filter_group_limit_clause': f'{filter}\nGROUP BY {cols}\nORDER BY {CATComponentsMeta.component_name}',
        }


class CATFeatures(AsyncQueryDescriptor):
    """
    Query to a local table storing CAT features
    available for the specified components.
    """

    def get_path(self,kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CATFeaturesMeta

    def get_format_params(self, kwargs) -> Mapping[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_features_filter(
                    tent_ids=kwargs['tent_ids'],
                    component_ids=kwargs['component_ids'],
                )
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_cat_components_features_name(),
            'filter_group_limit_clause': f'{filter}\nORDER BY {CATFeaturesMeta.feature_name}',
        }
