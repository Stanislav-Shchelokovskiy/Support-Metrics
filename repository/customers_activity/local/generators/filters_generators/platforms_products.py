from sql_queries.customers_activity.meta import PlatformsProductsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard
)

@params_guard
class PlatformsProductsSqlFilterClauseGenerator:

    @staticmethod
    def generate_platforms_filter(tribe_ids: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params=tribe_ids
        )
        return generate_filter(
            col=PlatformsProductsMeta.tribe_id,
            values=tribe_ids.values,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_products_filter(
        tribe_ids: FilterParametersNode,
        platform_ids: FilterParametersNode,
    ) -> str:
        platforms_filter = PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
            tribe_ids=tribe_ids
        )
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params=platform_ids
        )
        products_filter = generate_filter(
            col=PlatformsProductsMeta.platform_id,
            values=platform_ids.values,
            filter_prefix=' AND' if platforms_filter else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )
        platform_products_filter = platforms_filter + products_filter
        return  platform_products_filter + f"{' AND' if platform_products_filter else 'WHERE'} {PlatformsProductsMeta.product_id} IS NOT NULL"
