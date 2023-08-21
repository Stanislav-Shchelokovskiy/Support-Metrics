from sql_queries.meta import TicketsWithIterationsMeta
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    FilterParameterNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_privacy_filter(
    params: FilterParameterNode,
    col: str = TicketsWithIterationsMeta.is_private,
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_equals_filter_generator(
        params
    )
    return generate_filter(
        col=col,
        value=params.value,
        filter_prefix='AND',
    )


@params_guard
def generate_tribes_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.tribes_ids,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_tents_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.tent_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_builds_filter(
    params: FilterParametersNode,
    col: str = TicketsWithIterationsMeta.builds
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_operating_systems_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.operating_system_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_frameworks_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.frameworks,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_ides_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.ide_id,
        values=params.values,
        filter_prefix='AND',
    )


@params_guard
def generate_ticket_tags_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.ticket_tags,
        values=params.values,
        filter_prefix='AND',
    )
