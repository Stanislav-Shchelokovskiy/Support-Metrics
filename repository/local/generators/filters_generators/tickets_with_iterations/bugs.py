from sql_queries.meta.aggs import TicketsWithIterations
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)
from repository.local.generators.filters_generators.tickets_with_iterations.tickets import generate_builds_filter
from repository.local.generators.filters_generators.tickets_with_iterations.employees import generate_employees_filter


@params_guard
def generate_severity_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterations.severity,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_ticket_status_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterations.ticket_status,
        values=params.values,
        filter_prefix='AND',
    )


def generate_fixed_in_builds_filter(params: FilterParametersNode, ) -> str:
    return generate_builds_filter(
        params=params,
        col=TicketsWithIterations.fixed_in_builds,
    )


def generate_assigned_to_filter(params: FilterParametersNode) -> str:
    return generate_employees_filter(
        params=params,
        col=TicketsWithIterations.assigned_to,
    )


def generate_closed_by_filter(params: FilterParametersNode) -> str:
    return generate_employees_filter(
        params=params,
        col=TicketsWithIterations.closed_by,
    )


def generate_fixed_by_filter(params: FilterParametersNode) -> str:
    return generate_employees_filter(
        params=params,
        col=TicketsWithIterations.fixed_by,
    )


@params_guard
def generate_closed_on_filter(
    params: FilterParametersNode,
    col: str = TicketsWithIterations.closed_on,
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_between_filter_generator(
        params
    )
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
    )


def generate_fixed_on_filter(params: FilterParametersNode) -> str:
    return generate_closed_on_filter(
        params=params,
        col=TicketsWithIterations.fixed_on,
    )
