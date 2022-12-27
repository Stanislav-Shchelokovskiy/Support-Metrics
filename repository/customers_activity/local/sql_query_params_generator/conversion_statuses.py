from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import ConversionStatusesMeta


class ConversionStatusesSqlFilterClauseGenerator:

    @staticmethod
    def generate_filter(license_status_ids: list[int]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=license_status_ids,
            col=ConversionStatusesMeta.license_status_id,
            filter_prefix='WHERE',
            values_converter=str,
        )
