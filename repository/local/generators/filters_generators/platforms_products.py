from sql_queries.meta import PlatformsProductsMeta
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_tents_filter(
    tents_ids: FilterParametersNode,
    col: str,
    filter_prefix: str,
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(tents_ids)
    return generate_filter(
        col=col,
        values=tents_ids.values,
        filter_prefix=filter_prefix,
    )


def generate_platforms_filter(
    tent_ids: FilterParametersNode,
    filter_prefix='WHERE',
) -> str:
    return generate_tents_filter(
        tents_ids=tent_ids,
        col=PlatformsProductsMeta.platform_tent_id,
        filter_prefix=filter_prefix,
    )


def generate_products_filter(tent_ids: FilterParametersNode, ) -> str:
    products_filter = generate_tents_filter(
        tents_ids=tent_ids,
        col=PlatformsProductsMeta.product_tent_id,
        filter_prefix='WHERE',
    )

    platforms_filter = generate_platforms_filter(
        tent_ids=tent_ids,
        filter_prefix='',
    ) if tent_ids and tent_ids.include and len(tent_ids.values) > 0 else ''

    logical_operator = ' OR ' if platforms_filter else ''

    return products_filter + logical_operator + platforms_filter
