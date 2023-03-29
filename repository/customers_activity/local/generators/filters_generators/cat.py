from sql_queries.customers_activity.meta import CATComponentsFeaturesMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_components_filter(tribe_ids: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=tribe_ids
    )
    return generate_filter(
        col=CATComponentsFeaturesMeta.tribe_id,
        values=tribe_ids.values,
        filter_prefix='WHERE',
    )


@params_guard
def generate_features_filter(
    tribe_ids: FilterParametersNode,
    component_ids: FilterParametersNode,
) -> str:
    components_fitler = generate_components_filter(tribe_ids=tribe_ids)
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=component_ids
    )
    features_filter = generate_filter(
        col=CATComponentsFeaturesMeta.component_id,
        values=component_ids.values,
        filter_prefix=' AND' if components_fitler else 'WHERE',
    )

    return components_fitler + features_filter
