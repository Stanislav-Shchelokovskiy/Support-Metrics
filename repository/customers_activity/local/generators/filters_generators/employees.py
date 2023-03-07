from sql_queries.customers_activity.meta import EmployeesMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_positions_filter(position_ids: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=position_ids
    )
    return generate_filter(
        col=EmployeesMeta.position_id,
        values=position_ids.values,
        filter_prefix='WHERE',
        values_converter=lambda val: f"'{val}'",
    )


@params_guard
def generate_positions_tribes_filter(
    position_ids: FilterParametersNode,
    tribe_ids: FilterParametersNode,
) -> str:
    positions_fitler = generate_positions_filter(position_ids=position_ids)
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=tribe_ids
    )
    tribes_filter = generate_filter(
        col=EmployeesMeta.tribe_id,
        values=tribe_ids.values,
        filter_prefix=' AND' if positions_fitler else 'WHERE',
        values_converter=lambda val: f"'{val}'",
    )
    return positions_fitler + tribes_filter
