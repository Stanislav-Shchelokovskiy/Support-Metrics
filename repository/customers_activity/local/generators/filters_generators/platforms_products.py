from sql_queries.customers_activity.meta import PlatformsProductsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
class PlatformsProductsSqlFilterClauseGenerator:

    def generate_tribes_filter(
        tribe_ids: FilterParametersNode,
        col: str,
    ) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params=tribe_ids
        )
        return generate_filter(
            col=col,
            values=tribe_ids.values,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    def generate_platforms_filter(tribe_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_tribes_filter(
            tribe_ids=tribe_ids,
            col=PlatformsProductsMeta.platform_tribe_id,
        )

    def generate_products_filter(tribe_ids: FilterParametersNode, ) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_tribes_filter(
            tribe_ids=tribe_ids,
            col=PlatformsProductsMeta.product_tribe_id,
        )
