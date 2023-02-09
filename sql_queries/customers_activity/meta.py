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


class FrameworksMeta(KnotMeta):
    pass


class OperatingSystemsMeta(KnotMeta):
    pass


class BuildsMeta(KnotMeta):
    pass


class SeverityMeta(KnotMeta):
    pass


class TicketStatusesMeta(KnotMeta):
    pass

class IDEsMeta(KnotMeta):
    pass


class CATRepliesTypesMeta(KnotMeta):
    pass


class CustomersMeta(KnotMeta):
    pass


class TicketsWithIterationsPeriodMeta(MetaData):
    period_start = 'period_start'
    period_end = 'period_end'


class TribeIdMeta(MetaData):
    tribe_id = 'tribe_id'


class CATComponentsFeaturesMeta(TribeIdMeta):
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


class TicketsWithPropertiesMeta(TicketTribeMeta):
    user_crmid = 'user_crmid'
    user_id = 'user_id'
    ticket_scid = 'ticket_scid'
    ticket_type = 'ticket_type'
    creation_date = 'creation_date'
    is_private = 'is_private'
    user_groups = 'user_groups'
    ticket_tags = 'ticket_tags'
    platforms = 'platforms'
    products = 'products'
    frameworks = 'frameworks'
    builds = 'builds'
    fixed_in_builds = 'fixed_in_builds'
    fixed_by = 'fixed_by'
    fixed_on = 'fixed_on'
    ticket_status = 'ticket_status'
    closed_by = 'closed_by'
    closed_on = 'closed_on'
    severity = 'severity'
    license_status = 'license_status'
    conversion_status = 'conversion_status'
    duplicated_to_ticket_type = 'duplicated_to_ticket_type'
    duplicated_to_ticket_scid = 'duplicated_to_ticket_scid'
    assigned_to = 'assigned_to'
    operating_system_id = 'operating_system_id'
    ide_id = 'ide_id'
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


class TicketsWithIterationsMeta(TicketsWithPropertiesMeta):
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
    creation_date = TicketsWithIterationsMeta.creation_date


class BaselineAlignedCustomersGroupsMeta(MetaData):
    user_crmid = TicketsWithPropertiesMeta.user_crmid
    id = 'id'
    name = 'name'
    assignment_date = 'assignment_date'
    removal_date = 'removal_date'


class BaselineAlignedModeMeta(BaselineAlignedCustomersGroupsMeta):
    days_since_baseline = 'days_since_baseline'


class PeriodsMeta(MetaData):
    start = 'start'
    period = 'period'
