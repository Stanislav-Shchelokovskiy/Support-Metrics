from typing import Protocol
from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    ComponentsFeaturesMeta,
    ConversionStatusesMeta,
    PlatformsProductsMeta,
)


class FilterParametersNode(Protocol):
    include: bool
    values: list


class TicketsWithIterationsSqlFilterClauseGenerator:

    @staticmethod
    def _generate_like_filter(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_like_filter if params.include else generator.generate_not_like_filter
        return generate_filter

    @staticmethod
    def _generate_in_filter(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_in_filter if params.include else generator.generate_not_in_filter
        return generate_filter

    @staticmethod
    def generate_customer_groups_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.user_groups,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_ticket_types_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.ticket_type,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    @staticmethod
    def generate_ticket_tags_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.ticket_tags,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.tribe_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_reply_types_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.reply_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_components_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.component_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.feature_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_license_status_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.license_status,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    @staticmethod
    def generate_conversion_status_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.conversion_status,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    @staticmethod
    def generate_platforms_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.platforms,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_products_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.products,
            values=params.values,
            filter_prefix='AND',
        )


class CATSqlFilterClauseGenerator:

    @staticmethod
    def generate_components_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=tribe_ids,
            col=ComponentsFeaturesMeta.tribe_id,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(
        tribe_ids: list[str],
        component_ids: list[str],
    ) -> str:
        tribes_fitler = CATSqlFilterClauseGenerator.generate_components_filter(
            tribe_ids=tribe_ids
        )
        components_filter = SqlFilterClauseGenerator().generate_in_filter(
            values=component_ids,
            col=ComponentsFeaturesMeta.component_id,
            filter_prefix=' AND' if tribes_fitler else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )
        return tribes_fitler + components_filter


class ConversionStatusesSqlFilterClauseGenerator:

    @staticmethod
    def generate_filter(license_status_ids: list[int]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=license_status_ids,
            col=ConversionStatusesMeta.license_status_id,
            filter_prefix='WHERE',
            values_converter=str,
        )


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
            filter_prefix=' AND' if products_filter or platforms_filter else 'WHERE',
            col=PlatformsProductsMeta.product_id,
        )
        return platforms_filter + products_filter
