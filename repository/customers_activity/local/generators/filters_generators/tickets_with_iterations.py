from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    FilterParameterNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard
)
from configs.customers_activity_config import CustomersActivityConfig

@params_guard
class TicketsWithIterationsSqlFilterClauseGenerator:

    def generate_creation_date_with_rank_offset_start_filter(
        range_start: str,
        range_end: str,
    ) -> str:
        return f"{TicketsWithIterationsMeta.creation_date} BETWEEN DATE('{range_start}', '-{CustomersActivityConfig.get_rank_period_offset()}') AND '{range_end}'"

    def generate_creation_date_filter(
        range_start: str,
        range_end: str,
        filter_prefix: str = 'WHERE'
    ) -> str:
        return f"{filter_prefix} {TicketsWithIterationsMeta.creation_date} BETWEEN '{range_start}' AND '{range_end}'"

    def generate_customer_groups_filter(
        params: FilterParametersNode | None,
        col: str = TicketsWithIterationsMeta.user_groups,
        filter_prefix: str = 'AND'
    ) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=col,
            values=params.values,
            filter_prefix=filter_prefix,
        )

    def generate_ticket_types_filter(params: FilterParametersNode) -> str:
        generate_ticket_types_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_ticket_types_filter(
            col=TicketsWithIterationsMeta.ticket_type,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    def generate_duplicated_to_ticket_types_filter(
        params: FilterParametersNode
    ) -> str:
        generate_ticket_types_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_ticket_types_filter(
            col=TicketsWithIterationsMeta.duplicated_to_ticket_type,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    def generate_ticket_tags_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.ticket_tags,
            values=params.values,
            filter_prefix='AND',
        )

    def generate_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.tribe_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

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

    def generate_license_status_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.license_status,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    def generate_conversion_status_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.conversion_status,
            values=params.values,
            filter_prefix='AND',
            values_converter=str,
        )

    def generate_platforms_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.platforms,
            values=params.values,
            filter_prefix='AND',
        )

    def generate_products_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.products,
            values=params.values,
            filter_prefix='AND',
        )

    def generate_emp_positions_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.emp_position_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    def generate_emp_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.emp_tribe_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    def generate_employees_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.emp_crmid,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    def generate_customers_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=f'{CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid}',
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    def get_percentile_filter(
        alias: str,
        percentile: FilterParameterNode,
    ) -> str:

        def validate_percentile(val: int | None):
            if val is not None:
                if val < 0:
                    val = 0
                if val > 100:
                    val = 100
            else:
                val = 100
            return val

        if percentile.include:
            return f'{alias} <= {validate_percentile(percentile.value)}'
        return f'{alias} > {validate_percentile(percentile.value)}'
