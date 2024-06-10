from sql_queries.meta.aggs import TicketsWithIterations
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    FilterParameterNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory as filter_factory,
    params_guard,
)


@params_guard
def generate_privacy_filter(
    params: FilterParameterNode,
    col: str = TicketsWithIterations.is_private,
) -> str:
    generate_filter = filter_factory.get_equals_filter_generator(params)
    return generate_filter(
        col=col,
        value=params.value,
        filter_prefix='AND',
        value_converter=int,
    )


@params_guard
def generate_is_employee_filter(
    params: FilterParameterNode,
    col: str = TicketsWithIterations.is_employee,
) -> str:
    generate_filter = filter_factory.get_equals_filter_generator(params)
    return generate_filter(
        col=col,
        value=params.value,
        filter_prefix='AND',
        value_converter=int,
    )


@params_guard
def generate_tribes_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_like_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.tribes_ids,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_tents_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_in_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.tent_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_builds_filter(
    params: FilterParametersNode,
    col: str = TicketsWithIterations.builds
) -> str:
    generate_filter = filter_factory.get_like_filter_generator(params)
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_operating_systems_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_in_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.operating_system_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_frameworks_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_like_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.frameworks,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_ides_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_in_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.ide_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_ticket_tags_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_like_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.ticket_tags,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_closed_for_n_days(
    params: FilterParameterNode,
    col: str = TicketsWithIterations.closed_on,
) -> str:
    generate_filter = filter_factory.get_less_equals_filter_generator(params)
    return generate_filter(
        col=col,
        value=params.value,
        filter_prefix='AND',
        value_converter=lambda x: f"DATE('now', '-{x} DAYS')",
    )


@params_guard
def generate_resolution_in_hours(
    params: FilterParametersNode,
    col: str = TicketsWithIterations.resolution_in_hours,
) -> str:
    generate_filter = filter_factory.get_right_halfopen_interval_filter_generator(params)
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
        values_converter=int,
    )
