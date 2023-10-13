from collections.abc import Sequence, Callable
from typing import Any
from toolbox.sql.meta_data import MetaData, KnotMeta
from toolbox.sql.field import Field, TEXT, INTEGER


class CustomersGroupsMeta(MetaData):
    id = KnotMeta.id
    name = KnotMeta.name
    creation_date = Field(TEXT)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[str]:
        return MetaData.get_key_fields(
            projector,
            cls.id,
        )


class ConversionStatusesMeta(MetaData):
    id = KnotMeta.id
    name = KnotMeta.name
    license_status_id = Field(INTEGER)


class TribesMeta(MetaData):
    tribe_id = Field(TEXT)
    tribe_name = Field(TEXT)


class TentsMeta(MetaData):
    tent_id = Field(TEXT)
    tent_name = Field(TEXT)


class CATComponentsMeta(MetaData):
    component_id = Field(TEXT)
    component_name = Field(TEXT)


class CATFeaturesMeta(MetaData):
    feature_id = Field(TEXT)
    feature_name = Field(TEXT)


class CATComponentsFeaturesMeta(MetaData):
    tent_id = TentsMeta.tent_id
    component_id = CATComponentsMeta.component_id
    feature_id = CATFeaturesMeta.feature_id
    component_name = CATComponentsMeta.component_name
    feature_name = CATFeaturesMeta.feature_name


class PlatformsMeta(MetaData):
    platform_id = Field(TEXT)
    platform_name = Field(TEXT)


class ProductsMeta(MetaData):
    product_id = Field(TEXT)
    product_name = Field(TEXT)


class PlatformsProductsMeta(MetaData):
    platform_tent_id = Field(TEXT)
    platform_id = PlatformsMeta.platform_id
    product_tent_id = Field(TEXT)
    product_id = ProductsMeta.product_id
    platform_tent_name = Field(TEXT)
    platform_name = PlatformsMeta.platform_name
    product_tent_name = Field(TEXT)
    product_name = ProductsMeta.product_name


class TicketTribeMeta(MetaData):
    ticket_id = Field(TEXT)
    tribe_id = TribesMeta.tribe_id
    tribe_name = TribesMeta.tribe_name


class TicketsWithPropertiesMeta(MetaData):
    user_crmid = Field(TEXT)
    user_id = Field(TEXT)
    user_register_date = Field(TEXT)
    ticket_id = Field(TEXT)
    ticket_scid = Field(TEXT)
    ticket_type = Field(INTEGER)
    tribes_ids = Field(TEXT)
    tribes_names = Field(TEXT)
    tent_id = TentsMeta.tent_id
    tent_name = TentsMeta.tent_name
    creation_date = Field(TEXT)
    is_private = Field(INTEGER)
    user_groups = Field(TEXT)
    ticket_tags = Field(TEXT)
    platforms = Field(TEXT)
    products = Field(TEXT)
    frameworks = Field(TEXT)
    builds = Field(TEXT)
    fixed_in_builds = Field(TEXT)
    fixed_by = Field(TEXT)
    fixed_on = Field(TEXT)
    ticket_status = Field(TEXT)
    closed_by = Field(TEXT)
    closed_on = Field(TEXT)
    severity = Field(TEXT)
    converted_to_bug_on = Field(TEXT)
    duplicated_to_ticket_type = Field(INTEGER)
    duplicated_to_ticket_scid = Field(TEXT)
    assigned_to = Field(TEXT)
    operating_system_id = Field(TEXT)
    ide_id = Field(TEXT)
    reply_id = Field(TEXT)
    component_id = CATComponentsMeta.component_id
    feature_id = CATFeaturesMeta.feature_id
    license_name = Field(TEXT)
    parent_license_name = Field(TEXT)
    subscription_start = Field(TEXT)
    expiration_date = Field(TEXT)
    license_status = Field(INTEGER)
    conversion_status = Field(INTEGER)


class EmployeesIterationsMeta(MetaData):
    ticket_id = TicketTribeMeta.ticket_id
    post_id = Field(TEXT)
    crmid = Field(TEXT)
    scid = Field(TEXT)
    tribe_id = TicketTribeMeta.tribe_id
    tent_id = TentsMeta.tent_id
    position_id = Field(TEXT)
    name = Field(TEXT)
    position_name = Field(TEXT)
    tribe_name = TicketTribeMeta.tribe_name
    tent_name = TentsMeta.tent_name


class EmployeeMeta(MetaData):
    scid = EmployeesIterationsMeta.scid
    name = EmployeesIterationsMeta.name


class EmployeesMeta(MetaData):
    tribe_id = EmployeesIterationsMeta.tribe_id
    tent_id = TentsMeta.tent_id
    position_id = EmployeesIterationsMeta.position_id
    crmid = EmployeesIterationsMeta.crmid
    scid = EmployeeMeta.scid
    name = EmployeeMeta.name
    tribe_name = TribesMeta.tribe_name
    tent_name = TentsMeta.tent_name
    position_name = EmployeesIterationsMeta.position_name


class TicketsWithIterationsMeta(TicketsWithPropertiesMeta):
    emp_post_id = Field(TEXT)
    emp_crmid = Field(TEXT)
    emp_scid = Field(TEXT)
    emp_tribe_id = Field(TEXT)
    emp_tent_id = Field(TEXT)
    emp_position_id = Field(TEXT)
    emp_name = Field(TEXT)
    emp_position_name = Field(TEXT)
    emp_tribe_name = Field(TEXT)
    emp_tent_name = Field(TEXT)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[str]:
        return MetaData.get_key_fields(
            projector,
            cls.user_crmid,
            cls.ticket_scid,
            cls.emp_post_id,
        )


class TicketsWithIterationsRawMeta(MetaData):
    user_id = TicketsWithIterationsMeta.user_id
    ticket_scid = TicketsWithIterationsMeta.ticket_scid
    csi = Field(TEXT)
    ticket_type = TicketsWithIterationsMeta.ticket_type
    tribes_names = TicketsWithIterationsMeta.tribes_names
    tent_name = TicketsWithIterationsMeta.tent_name
    platforms = TicketsWithIterationsMeta.platforms
    products = TicketsWithIterationsMeta.products
    ticket_tags = TicketsWithIterationsMeta.ticket_tags
    is_private = TicketsWithIterationsMeta.is_private
    creation_date = TicketsWithIterationsMeta.creation_date
    license_name = Field(TEXT, alias='most_appropriate_license')
    parent_license_name = Field(TEXT, alias='parent_license')
    subscription_start = TicketsWithIterationsMeta.subscription_start
    expiration_date = TicketsWithIterationsMeta.expiration_date
    license_status = TicketsWithIterationsMeta.license_status
    conversion_status = TicketsWithIterationsMeta.conversion_status
    reply = Field(TEXT)
    component = Field(TEXT)
    feature = Field(TEXT)
    builds = TicketsWithIterationsMeta.builds
    fixed_in_builds = TicketsWithIterationsMeta.fixed_in_builds
    fixed_by = TicketsWithIterationsMeta.fixed_by
    fixed_on = TicketsWithIterationsMeta.fixed_on
    ticket_status = TicketsWithIterationsMeta.ticket_status
    closed_by = TicketsWithIterationsMeta.closed_by
    closed_on = TicketsWithIterationsMeta.closed_on
    severity = TicketsWithIterationsMeta.severity
    converted_to_bug_on = TicketsWithIterationsMeta.converted_to_bug_on
    duplicated_to_ticket_type = TicketsWithIterationsMeta.duplicated_to_ticket_type
    duplicated_to_ticket_scid = TicketsWithIterationsMeta.duplicated_to_ticket_scid
    assigned_to = TicketsWithIterationsMeta.assigned_to
    operating_system = Field(TEXT)
    ide = Field(TEXT)
    emp_post_id = TicketsWithIterationsMeta.emp_post_id
    emp_name = TicketsWithIterationsMeta.emp_name
    emp_position_name = TicketsWithIterationsMeta.emp_position_name
    emp_tribe_name = TicketsWithIterationsMeta.emp_tribe_name
    emp_tent_name = TicketsWithIterationsMeta.emp_tent_name


class BaselineAlignedCustomersGroupsMeta(MetaData):
    user_crmid = TicketsWithPropertiesMeta.user_crmid
    id = KnotMeta.id
    name = KnotMeta.name
    assignment_date = Field(TEXT)
    removal_date = Field(TEXT)


class BaselineAlignedModeMeta(BaselineAlignedCustomersGroupsMeta):
    days_since_baseline = Field(INTEGER)


class CSIMeta(MetaData):
    ticket_scid = TicketsWithIterationsMeta.ticket_scid
    date = Field(TEXT)
    rating = Field(INTEGER)
