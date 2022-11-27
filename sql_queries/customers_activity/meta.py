from toolbox.sql.meta_data import MetaData


class CustomersActivityMeta(MetaData):
    user_id = 'user_id'
    tribe_id = 'tribe_id'
    tribe_name = 'tribe_name'
    scid = 'scid'
    ticket_type = 'ticket_type'
    creation_date = 'creation_date'
    iterations = 'iterations'
    user_groups = 'user_groups'
    ticket_tags = 'ticket_tags'


class CustomersGroupsMeta(MetaData):
    id = 'id'
    name = 'name'


class TicketsTypesMeta(MetaData):
    id = 'id'
    name = 'name'


class TicketsTagsMeta(MetaData):
    id = 'id'
    name = 'name'


class TicketsWithIterationsPeriodMeta(MetaData):
    period_start = 'period_start'
    period_end = 'period_end'


class TicketsWithIterationsAggregates(MetaData):
    creation_date = CustomersActivityMeta.creation_date
    scid = CustomersActivityMeta.scid
    iterations = CustomersActivityMeta.iterations
    period = 'period'
    tickets = 'tickets'
