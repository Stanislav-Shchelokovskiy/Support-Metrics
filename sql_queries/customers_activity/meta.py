from toolbox.sql.meta_data import MetaData


class KnotMeta(MetaData):
    id = 'id'
    name = 'name'


class TribesMeta(KnotMeta):
    pass


class PositionsMeta(KnotMeta):
    pass


class CustomersGroupsMeta(KnotMeta):
    pass


class TicketsTagsMeta(KnotMeta):
    pass


class LicenseStatusesMeta(KnotMeta):
    pass


class ConversionStatusesMeta(KnotMeta):
    license_status_id = 'license_status_id'


class TicketsTypesMeta(KnotMeta):
    pass


class ReplyTypesMeta(KnotMeta):
    pass


class TicketsWithIterationsPeriodMeta(MetaData):
    period_start = 'period_start'
    period_end = 'period_end'


class TribeIdMeta(MetaData):
    tribe_id = 'tribe_id'


class ComponentsFeaturesMeta(TribeIdMeta):
    component_id = 'component_id'
    feature_id = 'feature_id'
    component_name = 'component_name'
    feature_name = 'feature_name'


class PlatformsProductsMeta(TribeIdMeta):
    platform_id = 'platform_id'
    product_id = 'product_id'
    platform_name = 'platform_name'
    product_name = 'product_name'


class TribeMeta(TribeIdMeta):
    tribe_name = 'tribe_name'


class TicketTribeMeta(TribeMeta):
    ticket_id = 'ticket_id'


class TicketsWithLicensesMeta(TicketTribeMeta):
    user_id = 'user_id'
    ticket_scid = 'ticket_scid'
    creation_date = 'creation_date'
    license_status = 'license_status'
    conversion_status = 'conversion_status'
    ticket_type = 'ticket_type'
    user_groups = 'user_groups'
    ticket_tags = 'ticket_tags'
    platforms = 'platforms'
    products = 'products'
    reply_id = 'reply_id'
    component_id = 'component_id'
    feature_id = 'feature_id'


class EmployeesIterationsMeta(TicketTribeMeta):
    post_id = 'post_id'
    crmid = 'crmid'
    position_id = 'position_id'
    name = 'name'
    position_name = 'position_name'


class EmployeesMeta(MetaData):
    tribe_id = EmployeesIterationsMeta.tribe_id
    position_id = EmployeesIterationsMeta.position_id
    crmid = EmployeesIterationsMeta.crmid
    name = EmployeesIterationsMeta.name


class TicketsWithIterationsMeta(TicketsWithLicensesMeta):
    emp_post_id = 'emp_post_id'
    emp_crmid = 'emp_crmid'
    emp_tribe_id = 'emp_tribe_id'
    emp_position_id = 'emp_position_id'
    emp_name = 'emp_name'
    emp_position_name = 'emp_position_name'
    emp_tribe_name = 'emp_tribe_name'


class TicketsWithIterationsAggregatesMeta(MetaData):
    period = 'period'
    user_id = TicketsWithIterationsMeta.user_id
    people = 'people'
    ticket_scid = TicketsWithIterationsMeta.ticket_scid
    tickets = 'tickets'
    emp_post_id = TicketsWithIterationsMeta.emp_post_id
    iterations = 'iterations'


class TicketsWithIterationsRawMeta(MetaData):
    user_id = TicketsWithIterationsMeta.user_id
    ticket_scid = TicketsWithIterationsMeta.ticket_scid
    tribe_name = TicketsWithIterationsMeta.tribe_name
    license_status = TicketsWithIterationsMeta.license_status
    conversion_status = TicketsWithIterationsMeta.conversion_status
    reply = 'reply'
    component = 'component'
    feature = 'feature'
    emp_post_id = TicketsWithIterationsMeta.emp_post_id
    emp_name = TicketsWithIterationsMeta.emp_name
    emp_position_name = TicketsWithIterationsMeta.emp_position_name
    emp_tribe_name = TicketsWithIterationsMeta.emp_tribe_name
