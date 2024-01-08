from collections.abc import Mapping
from sql_queries.meta.aggs import TicketsWithIterations


def get_ticket_lifetime_query(tbl: str, kwargs: Mapping) -> str:
    groupby_period = kwargs.get('groupby_period', TicketsWithIterations.creation_date)
    fld = TicketsWithIterations.lifetime_in_hours
    return f"""SELECT  *,
            NTH_VALUE({fld}, median) OVER (PARTITION BY {groupby_period} ORDER BY {fld}) AS median_{fld}
    FROM    (   SELECT  *,
                        ROUND(COUNT({fld}) OVER (PARTITION BY {groupby_period}) / 2.) AS median
                FROM    ({tbl}) AS tickets  ) AS tickets_with_median"""
