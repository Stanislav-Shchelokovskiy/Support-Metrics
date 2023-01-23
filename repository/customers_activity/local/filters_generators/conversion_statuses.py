from sql_queries.customers_activity.meta import ConversionStatusesMeta
from repository.customers_activity.local.filters_generators.sql_filter_clause_generator import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGenerator,
)


class ConversionStatusesSqlFilterClauseGenerator:

    @staticmethod
    def generate_conversion_filter(
        license_status_ids: FilterParametersNode
    ) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params=license_status_ids
        )
        return generate_filter(
            col=ConversionStatusesMeta.license_status_id,
            values=license_status_ids.values,
            filter_prefix='WHERE',
            values_converter=str,
        )
