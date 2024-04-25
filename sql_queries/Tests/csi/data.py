from sql_queries.meta.aggs import CSI


only_existing_tickets = {
    CSI.ticket_scid.name: ['ticket1', 'ticket2'],
    CSI.date.name: ['2023-01-01', '2023-02-01'],
    CSI.rating.name: [0, -1],
}

rating_range = {
    CSI.ticket_scid.name: ['ticket1', 'ticket2', 'ticket3', 'ticket4'],
    CSI.date.name: ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
    CSI.rating.name: [0, -1, 1, 0],
}
