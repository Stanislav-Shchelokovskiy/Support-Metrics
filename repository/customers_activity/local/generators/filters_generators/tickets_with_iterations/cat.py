from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_reply_types_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.reply_id,
        values=params.values,
        filter_prefix='AND',
        values_converter=lambda val: f"'{val}'",
    )


@params_guard
def generate_components_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.component_id,
        values=params.values,
        filter_prefix='AND',
        values_converter=lambda val: f"'{val}'",
    )


@params_guard
def generate_features_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.feature_id,
        values=params.values,
        filter_prefix='AND',
        values_converter=lambda val: f"'{val}'",
    )
