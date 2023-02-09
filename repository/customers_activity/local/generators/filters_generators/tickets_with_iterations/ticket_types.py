from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
class TicketsTypesSqlFilterClauseGenerator:

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
