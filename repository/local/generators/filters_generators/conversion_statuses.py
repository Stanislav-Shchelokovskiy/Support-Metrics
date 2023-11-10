from sql_queries.meta.customers import ConversionStatuses
from toolbox.sql.generators.filter_clause_generator_factory import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGeneratorFactory,
    params_guard,
)


@params_guard
def generate_conversion_filter(
    license_status_ids: FilterParametersNode
) -> str:
    generate_filter = SqlFilterClauseFromFilterParametersGeneratorFactory.get_in_filter_generator(license_status_ids)
    return generate_filter(
        col=ConversionStatuses.license_status_id,
        values=license_status_ids.values,
        filter_prefix='WHERE',
        values_converter=str,
    )
