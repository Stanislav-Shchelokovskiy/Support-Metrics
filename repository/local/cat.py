from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
import sql_queries.meta.cat as cat
import repository.local.generators.filters_generators.cat as CATSqlFilterClauseGenerator


class CATRepliesTypes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return cat.CatRepliesTypes

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': cat.CatRepliesTypes.get_name(),
            'where_group_limit': f'ORDER BY {cat.CatRepliesTypes.name}',
        }


class CATComponents(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return cat.Components

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_components_filter(tent_ids=kwargs['tent_ids'])
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'select': cols,
            'from': cat.CatComponentsFeatures.get_name(),
            'where_group_limit': f'{filter}\nGROUP BY {cols}\nORDER BY {cat.Components.component_name}',
        }


class CATFeatures(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return cat.Features

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = CATSqlFilterClauseGenerator.generate_features_filter(
                    tent_ids=kwargs['tent_ids'],
                    component_ids=kwargs['component_ids'],
                )
        cols = ', '.join(self.get_fields(kwargs))
        return {
            'select': cols,
            'from': cat.CatComponentsFeatures.get_name(),
            'where_group_limit': f'{filter}\nGROUP BY {cols}\nORDER BY {cat.Features.feature_name}',
        }
