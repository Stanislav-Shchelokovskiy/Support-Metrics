from sql_queries.meta.aggs import TicketsWithIterations
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory as filter_factory,
    params_guard,
)


@params_guard
def generate_emp_positions_filter(params: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_in_filter_generator(params)
    return generate_filter(
        col=TicketsWithIterations.emp_position_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_emp_tribes_filter(
    params: FilterParametersNode,
    col: str = TicketsWithIterations.emp_tribe_id
) -> str:
    generate_filter = filter_factory.get_in_filter_generator(params)
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
    )


def generate_emp_tents_filter(params: FilterParametersNode) -> str:
    return generate_emp_tribes_filter(
        params=params,
        col=TicketsWithIterations.emp_tent_id,
    )


@params_guard
def generate_roles_filter(
    params: FilterParametersNode | None,
    col: str = TicketsWithIterations.roles,
    filter_prefix: str = 'AND'
) -> str:
    generate_filter = filter_factory.get_like_filter_generator(params)
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix=filter_prefix,
    )


@params_guard
def generate_employees_filter(
    params: FilterParametersNode,
    col: str = TicketsWithIterations.emp_scid
) -> str:
    generate_filter = filter_factory.get_in_filter_generator(params)
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
    )
