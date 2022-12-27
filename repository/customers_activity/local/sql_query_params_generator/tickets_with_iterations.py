from typing import Protocol
from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import (
    TicketsWithLicensesMeta,
    EmployeesIterations,
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
            col=TicketsWithLicensesMeta.user_groups,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_ticket_types_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithLicensesMeta.ticket_type,
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
            col=TicketsWithLicensesMeta.ticket_tags,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithLicensesMeta.tribe_id,
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
            col=TicketsWithLicensesMeta.reply_id,
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
            col=TicketsWithLicensesMeta.component_id,
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
            col=TicketsWithLicensesMeta.feature_id,
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
            col=TicketsWithLicensesMeta.license_status,
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
            col=TicketsWithLicensesMeta.conversion_status,
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
            col=TicketsWithLicensesMeta.platforms,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_products_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithLicensesMeta.products,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_positions_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsSqlFilterClauseGenerator._generate_in_filter(
            params
        )
        return generate_filter(
            col=EmployeesIterations.pos_id,
            values=params.values,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )
