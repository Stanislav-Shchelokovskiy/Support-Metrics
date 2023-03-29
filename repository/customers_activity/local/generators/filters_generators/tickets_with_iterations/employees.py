from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode, SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard
)


@params_guard
def generate_emp_positions_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.emp_position_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_emp_tribes_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.emp_tribe_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_employees_filter(params: FilterParametersNode, col: str = TicketsWithIterationsMeta.emp_crmid) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
    )
