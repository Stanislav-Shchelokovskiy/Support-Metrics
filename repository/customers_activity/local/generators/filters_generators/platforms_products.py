from sql_queries.customers_activity.meta import PlatformsProductsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_tribes_filter(
    tribe_ids: FilterParametersNode,
    col: str,
    filter_prefix: str,
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=tribe_ids
    )
    return generate_filter(
        col=col,
        values=tribe_ids.values,
        filter_prefix=filter_prefix,
        values_converter=lambda val: f"'{val}'",
    )


def generate_platforms_filter(
    tribe_ids: FilterParametersNode,
    filter_prefix='WHERE',
) -> str:
    return generate_tribes_filter(
        tribe_ids=tribe_ids,
        col=PlatformsProductsMeta.platform_tribe_id,
        filter_prefix=filter_prefix,
    )


def generate_products_filter(tribe_ids: FilterParametersNode, ) -> str:
    products_filter = generate_tribes_filter(
        tribe_ids=tribe_ids,
        col=PlatformsProductsMeta.product_tribe_id,
        filter_prefix='WHERE',
    )

    platforms_filter = generate_platforms_filter(
        tribe_ids=tribe_ids,
        filter_prefix='',
    ) if tribe_ids and tribe_ids.include and len(tribe_ids.values) > 0 else ''

    logical_operator = ' OR ' if platforms_filter else ''

    return products_filter + logical_operator + platforms_filter
