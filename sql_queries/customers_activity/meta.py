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


class CustomersTagsMeta(MetaData):
    id = 'id'
    name = 'name'
    description = 'description'


class TicketsWithIterationsPeriodMeta(MetaData):
    period_start = 'period_start'
    period_end = 'period_end'
