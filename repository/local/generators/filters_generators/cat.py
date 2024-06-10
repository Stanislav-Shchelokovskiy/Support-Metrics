from sql_queries.meta.cat import CatComponentsFeatures
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_components_filter(tent_ids: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(tent_ids)
    return generate_filter(
        col=CatComponentsFeatures.tent_id,
        values=tent_ids.values,
        filter_prefix='WHERE',
    )


@params_guard
def generate_features_filter(
    tent_ids: FilterParametersNode,
    component_ids: FilterParametersNode,
) -> str:
    components_fitler = generate_components_filter(tent_ids=tent_ids)
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(component_ids)
    features_filter = generate_filter(
        col=CatComponentsFeatures.component_id,
        values=component_ids.values,
        filter_prefix=' AND' if components_fitler else 'WHERE',
    )

    return components_fitler + features_filter
