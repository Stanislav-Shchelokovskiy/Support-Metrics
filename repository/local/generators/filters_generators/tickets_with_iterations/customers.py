from sql_queries.meta import TicketsWithIterationsMeta, BaselineAlignedModeMeta
from sql_queries.index import CustomersActivityDBIndex
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_customer_groups_filter(
    params: FilterParametersNode | None,
    col: str = TicketsWithIterationsMeta.user_groups,
    filter_prefix: str = 'AND'
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_like_filter_generator(
        params
    )
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix=filter_prefix,
    )


@params_guard
def generate_tracked_customer_groups_filter(
    params: FilterParametersNode | None,
    col: str = BaselineAlignedModeMeta.id,
    filter_prefix: str = 'AND'
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=col,
        values=params.values,
        filter_prefix=filter_prefix,
    )


@params_guard
def generate_license_status_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.license_status,
        values=params.values,
        filter_prefix='AND',
        values_converter=str,
    )


@params_guard
def generate_conversion_status_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=TicketsWithIterationsMeta.conversion_status,
        values=params.values,
        filter_prefix='AND',
        values_converter=str,
    )


@params_guard
def generate_customers_filter(params: FilterParametersNode) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(
        params
    )
    return generate_filter(
        col=f'{CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid}',
        values=params.values,
        filter_prefix='AND',
    )
