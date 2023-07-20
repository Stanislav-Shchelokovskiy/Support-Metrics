from sql_queries.meta import CSIMeta, TicketsWithIterationsMeta
import sql_queries.index.db as DbIndex


def get_csi_query(tbl: str, **kwargs) -> str:
    return (
        f"""(SELECT DISTINCT {TicketsWithIterationsMeta.ticket_scid}
    FROM {tbl}) AS tickets
    INNER JOIN {DbIndex.csi} AS ratings ON ratings.{CSIMeta.ticket_scid} = tickets.{TicketsWithIterationsMeta.ticket_scid}"""
    )
