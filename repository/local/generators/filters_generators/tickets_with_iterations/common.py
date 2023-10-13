from sql_queries.meta import TicketsWithIterationsMeta
from toolbox.sql.generators import filter_clause_generator
import configs.config as config


def generate_creation_date_with_rank_offset_start_filter(
    range_start: str,
    range_end: str,
) -> str:
    return filter_clause_generator.generate_between_filter(
        col=TicketsWithIterationsMeta.creation_date,
        values=(f"DATE('{range_start}', '-{config.get_rank_period_offset()}')", f"'{range_end}'"),
        filter_prefix='',
        values_converter=str,
    )


def generate_creation_date_filter(
    range_start: str,
    range_end: str,
    filter_prefix: str = 'WHERE',
) -> str:
    return filter_clause_generator.generate_between_filter(
        col=TicketsWithIterationsMeta.creation_date,
        values=(range_start, range_end),
        filter_prefix=filter_prefix,
    )
