from sql_queries.customers_activity.meta import CATComponentsFeaturesMeta
from repository.customers_activity.local.filters_generators.sql_filter_clause_generator import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGenerator,
)


class CATSqlFilterClauseGenerator:

    @staticmethod
    def generate_components_filter(tribe_ids: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params=tribe_ids
        )
        return generate_filter(
            col=CATComponentsFeaturesMeta.tribe_id,
            values=tribe_ids.values,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(
        tribe_ids: FilterParametersNode,
        component_ids: FilterParametersNode,
    ) -> str:
        components_fitler = CATSqlFilterClauseGenerator.generate_components_filter(
            tribe_ids=tribe_ids
        )
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params=component_ids
        )
        features_filter = generate_filter(
            col=CATComponentsFeaturesMeta.component_id,
            values=component_ids.values,
            filter_prefix=' AND' if components_fitler else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )

        return components_fitler + features_filter