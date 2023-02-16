from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    FilterParameterNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
class TicketsSqlFilterClauseGenerator:

    def generate_privacy_filter(
        params: FilterParameterNode,
        col: str = TicketsWithIterationsMeta.is_private,
    ) -> str:
        return f'AND {col} = {params.value}'

    def generate_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.tribes_ids,
            values=params.values,
            filter_prefix='AND',
        )

    def generate_builds_filter(
        params: FilterParametersNode,
        col: str = TicketsWithIterationsMeta.builds
    ) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=col,
            values=params.values,
            filter_prefix='AND',
        )

    def generate_operating_systems_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.operating_system_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
        )

    def generate_frameworks_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.frameworks,
            values=params.values,
            filter_prefix='AND',
        )

    def generate_ides_filter(params: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
            params
        )
        return generate_filter(
            col=TicketsWithIterationsMeta.ide_id,
            values=params.values,
            filter_prefix='AND',
            values_converter=lambda val: f"'{val}'",
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
