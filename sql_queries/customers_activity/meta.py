from toolbox.sql.meta_data import MetaData


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


class LicenseStatusesMeta(KnotMeta):
    pass


class ConversionStatusesMeta(KnotMeta):
    license_status_id = 'license_status_id'


class TribeAwaredMeta(MetaData):
    tribe_id = 'tribe_id'


class ComponentsFeaturesMeta(TribeAwaredMeta):
    component_id = 'component_id'
    feature_id = 'feature_id'
    component_name = 'component_name'
    feature_name = 'feature_name'


class PlatformsProductsMeta(TribeAwaredMeta):
    platform_id = 'platform_id'
    product_id = 'product_id'
    platform_name = 'platform_name'
    product_name = 'product_name'


class TicketsWithIterationsPeriodMeta(MetaData):
    period_start = 'period_start'
    period_end = 'period_end'


class TicketsWithIterationsMainMeta(MetaData):
    user_id = 'user_id'
    tribe_name = 'tribe_name'
    ticket_scid = 'ticket_scid'
    creation_date = 'creation_date'
    iterations = 'iterations'
    license_status = 'license_status'
    conversion_status = 'conversion_status'


class EmployeesIterations(MetaData):
    ticket_id = 'ticket_id'
    post_id = 'post_id'
    scid = 'scid'
    crmid = 'crmid'
    tribe_id = 'tribe_id'
    pos_id = 'pos_id'
    name = 'name'
    pos_name = 'pos_name'
    tribe_name = 'tribe_name'


class TicketsWithIterationsMeta(TicketsWithIterationsMainMeta):
    tribe_id = TribeAwaredMeta.tribe_id
    ticket_id = EmployeesIterations.ticket_id
    ticket_type = 'ticket_type'
    user_groups = 'user_groups'
    ticket_tags = 'ticket_tags'
    platforms = 'platforms'
    products = 'products'
    reply_id = 'reply_id'
    component_id = 'component_id'
    feature_id = 'feature_id'


class TicketsWithIterationsAggregatesMeta(MetaData):
    creation_date = TicketsWithIterationsMeta.creation_date
    ticket_scid = TicketsWithIterationsMeta.ticket_scid
    iterations = TicketsWithIterationsMeta.iterations
    user_id = TicketsWithIterationsMeta.user_id
    period = 'period'
    tickets = 'tickets'
    people = 'people'


class TicketsWithIterationsRawMeta(TicketsWithIterationsMainMeta):
    reply = 'reply'
    component = 'component'
    feature = 'feature'
