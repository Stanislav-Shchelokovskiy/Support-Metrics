from sql_queries.meta import CSIMeta, TicketsWithIterationsMeta
import sql_queries.index.name as name_index


def get_csi_query(tbl: str, **kwargs) -> str:
    return (
        f"""(SELECT DISTINCT {TicketsWithIterationsMeta.ticket_scid}
    FROM {tbl}) AS tickets
    INNER JOIN {name_index.csi} AS ratings ON ratings.{CSIMeta.ticket_scid} = tickets.{TicketsWithIterationsMeta.ticket_scid}"""
    )
