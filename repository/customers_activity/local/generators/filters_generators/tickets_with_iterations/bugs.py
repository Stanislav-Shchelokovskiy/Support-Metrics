from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)
import repository.customers_activity.local.generators.filters_generators.tickets_with_iterations.tickets as TicketsSqlFilterClauseGenerator


@params_guard
def generate_severity_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.severity,
        values=params.values,
        filter_prefix='AND',
        values_converter=lambda val: f"'{val}'",
    )


@params_guard
def generate_ticket_status_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.ticket_status,
        values=params.values,
        filter_prefix='AND',
        values_converter=lambda val: f"'{val}'",
    )


@params_guard
def generate_fixed_in_builds_filter(params: FilterParametersNode, ) -> str:
    return TicketsSqlFilterClauseGenerator.generate_builds_filter(
        params=params,
        col=TicketsWithIterationsMeta.fixed_in_builds,
    )


@params_guard
def generate_assigned_to_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.assigned_to,
        values=params.values,
        filter_prefix='AND',
        values_converter=lambda val: f"'{val}'",
    )
