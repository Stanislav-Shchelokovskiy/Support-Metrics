from sql_queries.meta.employees import Employees
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory as filter_factory,
    params_guard,
)


@params_guard
def generate_positions_filter(position_ids: FilterParametersNode) -> str:
    generate_filter = filter_factory.get_in_filter_generator(position_ids)
    return generate_filter(
        col=Employees.position_id,
        values=position_ids.values,
        filter_prefix='WHERE',
    )


@params_guard
def generate_positions_tribes_tents_roles_filter(
    position_ids: FilterParametersNode,
    tribe_ids: FilterParametersNode,
    tent_ids: FilterParametersNode,
    roles: FilterParametersNode,
) -> str:
    generate_tribes_filter = filter_factory.get_in_filter_generator(tribe_ids)
    generate_tents_filter = filter_factory.get_in_filter_generator(tent_ids)
    generate_roles_filter = filter_factory.get_like_filter_generator(roles)

    positions_fitler = generate_positions_filter(position_ids=position_ids)
    tribes_filter = generate_tribes_filter(
        col=Employees.tribe_id,
        values=tribe_ids.values,
        filter_prefix=' AND' if positions_fitler else 'WHERE',
    )

    positions_tribes_filter = positions_fitler + tribes_filter

    tents_filter = generate_tents_filter(
        col=Employees.tent_id,
        values=tent_ids.values,
        filter_prefix=' AND' if positions_tribes_filter else 'WHERE',
    )

    positions_tribes_tents_filter = positions_tribes_filter + tents_filter

    roles_filter = generate_roles_filter(
        col=Employees.roles,
        values=roles.values,
        filter_prefix=' AND' if positions_tribes_tents_filter else 'WHERE',
    )
    return positions_tribes_tents_filter + roles_filter
