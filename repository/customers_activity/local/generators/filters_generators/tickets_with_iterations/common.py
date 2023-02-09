from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import params_guard
from configs.customers_activity_config import CustomersActivityConfig


@params_guard
class CommonSqlFilterClauseGenerator:

    def generate_creation_date_with_rank_offset_start_filter(
        range_start: str,
        range_end: str,
    ) -> str:
        return f"{TicketsWithIterationsMeta.creation_date} BETWEEN DATE('{range_start}', '-{CustomersActivityConfig.get_rank_period_offset()}') AND '{range_end}'"

    def generate_creation_date_filter(
        range_start: str,
        range_end: str,
        filter_prefix: str = 'WHERE',
    ) -> str:
        return f"{filter_prefix} {TicketsWithIterationsMeta.creation_date} BETWEEN '{range_start}' AND '{range_end}'"
