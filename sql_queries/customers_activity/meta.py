from toolbox.sql.meta_data import MetaData


class TicketsWithIterationsMainMeta(MetaData):
    user_id = 'user_id'
    tribe_name = 'tribe_name'
    scid = 'scid'
    creation_date = 'creation_date'
    iterations = 'iterations'


class TicketsWithIterationsMeta(TicketsWithIterationsMainMeta):
    tribe_id = 'tribe_id'
    ticket_type = 'ticket_type'
    user_groups = 'user_groups'
    ticket_tags = 'ticket_tags'
    reply_id = 'reply_id'
    component_id = 'component_id'
    feature_id = 'feature_id'


class KnotMeta(MetaData):
    id = 'id'
    name = 'name'


class CustomersGroupsMeta(KnotMeta):
    pass


class TicketsTypesMeta(KnotMeta):
    pass


class TicketsTagsMeta(KnotMeta):
    pass


class ReplyTypesMeta(KnotMeta):
    pass


class ComponentsFeaturesMeta(MetaData):
    tribe_id = 'tribe_id'
    component_id = 'component_id'
    feature_id = 'feature_id'
    component_name = 'component_name'
    feature_name = 'feature_name'


class TicketsWithIterationsPeriodMeta(MetaData):
    period_start = 'period_start'
    period_end = 'period_end'


class TicketsWithIterationsAggregatesMeta(MetaData):
    creation_date = TicketsWithIterationsMeta.creation_date
    scid = TicketsWithIterationsMeta.scid
    iterations = TicketsWithIterationsMeta.iterations
    period = 'period'
    tickets = 'tickets'


class TicketsWithIterationsRawMeta(TicketsWithIterationsMainMeta):
    reply = 'reply'
    component = 'component'
    feature = 'feature'
