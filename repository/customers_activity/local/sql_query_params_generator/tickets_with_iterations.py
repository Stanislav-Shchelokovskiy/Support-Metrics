from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.sql_query_params_generator.sql_filter_clause_generator import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGenerator,
)


class TicketsWithIterationsSqlFilterClauseGenerator:

    @staticmethod
    def generate_customer_groups_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.user_groups,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_ticket_types_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.ticket_tags,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
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
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.platforms,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_products_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_like_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.products,
            values=params.values,
            filter_prefix='AND',
        )

    @staticmethod
    def generate_positions_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.emp_position_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_emp_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.emp_tribe_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_employees_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.emp_crmid,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )
