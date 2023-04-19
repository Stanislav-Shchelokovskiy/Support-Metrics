from toolbox.sql.meta_data import MetaData, KnotMeta


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

class TentIdMeta(MetaData):
    tent_id = 'tent_id'


class CATComponentsFeaturesMeta(TribeIdMeta):
    component_id = 'component_id'
    feature_id = 'feature_id'
    component_name = 'component_name'
    feature_name = 'feature_name'


class PlatformsProductsMeta(MetaData):
    platform_tribe_id = 'platform_tribe_id'
    platform_id = 'platform_id'
    product_tribe_id = 'product_tribe_id'
    product_id = 'product_id'
    platform_tribe_name = 'platform_tribe_name'
    platform_name = 'platform_name'
    product_tribe_name = 'product_tribe_name'
    product_name = 'product_name'


class TribeMeta(TribeIdMeta):
    tribe_name = 'tribe_name'

class TentMeta(TentIdMeta):
    tent_name = 'tent_name'

class TicketTribeMeta(TribeMeta):
    ticket_id = 'ticket_id'


class TicketsWithPropertiesMeta(MetaData):
    user_crmid = 'user_crmid'
    user_id = 'user_id'
    ticket_id = 'ticket_id'
    ticket_scid = 'ticket_scid'
    ticket_type = 'ticket_type'
    tribes_ids = 'tribes_ids'
    tribes_names = 'tribes_names'
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
    duplicated_to_ticket_type = 'duplicated_to_ticket_type'
    duplicated_to_ticket_scid = 'duplicated_to_ticket_scid'
    assigned_to = 'assigned_to'
    operating_system_id = 'operating_system_id'
    ide_id = 'ide_id'
    reply_id = 'reply_id'
    component_id = 'component_id'
    feature_id = 'feature_id'
    license_name = 'license_name'
    subscription_start = 'subscription_start'
    expiration_date = 'expiration_date'
    license_status = 'license_status'
    conversion_status = 'conversion_status'


class EmployeesIterationsMeta(TicketTribeMeta):
    post_id = 'post_id'
    crmid = 'crmid'
    position_id = 'position_id'
    name = 'name'
    position_name = 'position_name'


class EmployeesMeta(MetaData):
    tribe_id = EmployeesIterationsMeta.tribe_id
    tent_id = TentIdMeta.tent_id
    position_id = EmployeesIterationsMeta.position_id
    crmid = EmployeesIterationsMeta.crmid
    name = EmployeesIterationsMeta.name
    tribe_name = TribeMeta.tribe_name
    tent_name = TentMeta.tent_name
    position_name = 'position_name'


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
    ticket_type = TicketsWithIterationsMeta.ticket_type
    tribes_names = TicketsWithIterationsMeta.tribes_names
    platforms = TicketsWithIterationsMeta.platforms
    products = TicketsWithIterationsMeta.products
    is_private = TicketsWithIterationsMeta.is_private
    creation_date = TicketsWithIterationsMeta.creation_date
    license_name = 'most_appropriate_license'
    subscription_start = TicketsWithIterationsMeta.subscription_start
    expiration_date = TicketsWithIterationsMeta.expiration_date
    license_status = TicketsWithIterationsMeta.license_status
    conversion_status = TicketsWithIterationsMeta.conversion_status
    reply = 'reply'
    component = 'component'
    feature = 'feature'
    builds = TicketsWithIterationsMeta.builds
    fixed_in_builds = TicketsWithIterationsMeta.fixed_in_builds
    fixed_by = TicketsWithIterationsMeta.fixed_by
    fixed_on = TicketsWithIterationsMeta.fixed_on
    ticket_status = TicketsWithIterationsMeta.ticket_status
    closed_by = TicketsWithIterationsMeta.closed_by
    closed_on = TicketsWithIterationsMeta.closed_on
    severity = TicketsWithIterationsMeta.severity
    duplicated_to_ticket_type = TicketsWithIterationsMeta.duplicated_to_ticket_type
    duplicated_to_ticket_scid = TicketsWithIterationsMeta.duplicated_to_ticket_scid
    assigned_to = TicketsWithIterationsMeta.assigned_to
    operating_system = 'operating_system'
    ide = 'ide'
    emp_post_id = TicketsWithIterationsMeta.emp_post_id
    emp_name = TicketsWithIterationsMeta.emp_name
    emp_position_name = TicketsWithIterationsMeta.emp_position_name
    emp_tribe_name = TicketsWithIterationsMeta.emp_tribe_name


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
