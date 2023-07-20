from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.meta import (
    CATRepliesTypesMeta,
    CATComponentsMeta,
    CATFeaturesMeta,
)
import repository.local.generators.filters_generators.cat as CATSqlFilterClauseGenerator
import sql_queries.index.db as DbIndex


class CATRepliesTypes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CATRepliesTypesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.cat_replies_types,
            'where_group_limit': f'ORDER BY {CATRepliesTypesMeta.name}',
        }


class CATComponents(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CATComponentsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_components_filter(tent_ids=kwargs['tent_ids'])
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'select': cols,
            'from': DbIndex.cat_components_features,
            'where_group_limit': f'{filter}\nGROUP BY {cols}\nORDER BY {CATComponentsMeta.component_name}',
        }


class CATFeatures(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return CATFeaturesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_features_filter(
                    tent_ids=kwargs['tent_ids'],
                    component_ids=kwargs['component_ids'],
                )
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.cat_components_features,
            'where_group_limit': f'{filter}\nORDER BY {CATFeaturesMeta.feature_name}',
        }
