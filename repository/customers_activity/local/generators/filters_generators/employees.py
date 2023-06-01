from sql_queries.customers_activity.meta import EmployeesMeta
from toolbox.sql.generators.filter_clause_generator_factory import (
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
    )


@params_guard
def generate_positions_tribes_tents_filter(
    position_ids: FilterParametersNode,
    tribe_ids: FilterParametersNode,
    tent_ids: FilterParametersNode,
) -> str:
    positions_fitler = generate_positions_filter(position_ids=position_ids)
    generate_tribes_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=tribe_ids
    )
    generate_tents_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params=tent_ids
    )

    tribes_filter = generate_tribes_filter(
        col=EmployeesMeta.tribe_id,
        values=tribe_ids.values,
        filter_prefix=' AND' if positions_fitler else 'WHERE',
    )

    positions_tribes_filter = positions_fitler + tribes_filter

    tents_filter = generate_tents_filter(
        col=EmployeesMeta.tent_id,
        values=tent_ids.values,
        filter_prefix=' AND' if positions_tribes_filter else 'WHERE',
    )
    return positions_tribes_filter + tents_filter
