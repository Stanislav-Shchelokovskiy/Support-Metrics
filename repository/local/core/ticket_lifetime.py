from collections.abc import Mapping
from sql_queries.meta.aggs import TicketsWithIterations
from toolbox.sql.generators.sqlite.statements import with_median


def get_ticket_lifetime_query(tbl: str, kwargs: Mapping) -> str:
    return with_median(
        tbl=tbl,
        group_by=kwargs.get('groupby_period', TicketsWithIterations.creation_date),
        group_by_fld=TicketsWithIterations.creation_date,
        fld=TicketsWithIterations.lifetime_in_hours,
    )
