from sql_queries.meta import TicketsWithIterationsMeta
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_platforms_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.platforms,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_products_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.products,
        values=params.values,
        filter_prefix='AND',
    )
