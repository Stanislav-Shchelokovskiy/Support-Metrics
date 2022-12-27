from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import PlatformsProductsMeta


class PlatformsProductsSqlFilterClauseGenerator:

    @staticmethod
    def generate_platforms_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=tribe_ids,
            col=PlatformsProductsMeta.tribe_id,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_products_filter(
        tribe_ids: list[str],
        platform_ids: list[str],
    ) -> str:
        platforms_filter = PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
            tribe_ids=tribe_ids
        )
        generator = SqlFilterClauseGenerator()
        products_filter = generator.generate_in_filter(
            values=platform_ids,
            col=PlatformsProductsMeta.platform_id,
            filter_prefix=' AND' if platforms_filter else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )
        products_filter += generator.generate_is_not_null_filter(
            filter_prefix=' AND'
            if products_filter or platforms_filter else 'WHERE',
            col=PlatformsProductsMeta.product_id,
        )
        return platforms_filter + products_filter
