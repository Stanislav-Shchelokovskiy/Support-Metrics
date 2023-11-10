from sql_queries.meta.aggs import CSI, TicketsWithIterations


def get_csi_query(tbl: str, **kwargs) -> str:
    return (
        f"""(SELECT DISTINCT {TicketsWithIterations.ticket_scid}
    FROM {tbl}) AS tickets
    INNER JOIN {CSI.get_name()} AS ratings ON ratings.{CSI.ticket_scid} = tickets.{TicketsWithIterations.ticket_scid}"""
    )
