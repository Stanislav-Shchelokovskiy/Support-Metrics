from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_ticket_types_filter(
    params: FilterParametersNode,
    col: str = TicketsWithIterationsMeta.ticket_type
) -> str:
    generate_ticket_types_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_ticket_types_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
        values_converter=str,
    )


def generate_duplicated_to_ticket_types_filter(
    params: FilterParametersNode
) -> str:
    return generate_ticket_types_filter(
        params=params,
        col=TicketsWithIterationsMeta.duplicated_to_ticket_type,
    )
