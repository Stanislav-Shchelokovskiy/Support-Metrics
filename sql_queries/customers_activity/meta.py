from toolbox.sql.meta_data import MetaData


class TicketsWithIterationsMeta(MetaData):
    user_id = 'user_id'
    tribe_id = 'tribe_id'
    scid = 'scid'
    ticket_type = 'ticket_type'
    creation_date = 'creation_date'
    iterations = 'iterations'
    user_groups = 'user_groups'
    ticket_tags = 'ticket_tags'
    reply_id = 'reply_id'
    control_id = 'control_id'
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


class ControlsFeaturesMeta(MetaData):
    tribe_id = 'tribe_id'
    control_id = 'control_id'
    feature_id = 'feature_id'
    control_name = 'control_name'
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
