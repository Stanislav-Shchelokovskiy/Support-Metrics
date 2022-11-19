from toolbox.sql.meta_data import MetaData


class CustomersActivityMeta(MetaData):
    friendly_id = 'friendly_id'
    tribe_id = 'tribe_id'
    tribe_name = 'tribe_name'
    ticket_scid = 'ticket_scid'
    ticket_type = 'ticket_type'
    creation_date = 'creation_date'
    iterations = 'iterations'


class CustomersGroupsMeta(MetaData):
    id = 'id'
    name = 'name'
    note = 'note'


class CustomersTagsMeta(MetaData):
    id = 'id'
    name = 'name'
    description = 'description'
