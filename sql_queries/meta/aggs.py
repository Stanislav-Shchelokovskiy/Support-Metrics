import toolbox.sql.generators.sqlite.statements as sqlite_index
from collections.abc import Sequence, Callable
from typing import Any
from toolbox.sql.meta_data import MetaData
from toolbox.sql.field import Field, TEXT, INTEGER
from sql_queries.meta.employees import EmployeesIterations


class Tickets(MetaData):
    user_crmid = Field(TEXT)
    user_id = Field(TEXT)
    is_employee = Field(INTEGER)
    user_register_date = Field(TEXT)
    ticket_id = Field(TEXT)
    ticket_scid = Field(TEXT)
    ticket_type = Field(INTEGER)
    tribes_ids = Field(TEXT)
    tribes_names = Field(TEXT)
    tent_id = Field(TEXT)
    tent_name = Field(TEXT)
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
    component_id = Field(TEXT)
    feature_id = Field(TEXT)
    license_name = Field(TEXT)
    parent_license_name = Field(TEXT)
    subscription_start = Field(TEXT)
    expiration_date = Field(TEXT)
    license_status = Field(INTEGER)
    conversion_status = Field(INTEGER)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field | str | Any]:
        return tuple()

    @classmethod
    def get_indices(cls) -> Sequence[str]:
        return (
            sqlite_index.create_index(
                tbl=cls.get_name(),
                cols=(
                    cls.user_crmid,
                    cls.creation_date,
                ),
            ),
        )


class ResolutionTime(MetaData):
    ticket_scid = Tickets.ticket_scid
    resolution_in_hours = Field(INTEGER)
    lifetime_in_hours = Field(INTEGER)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field | str | Any]:
        return MetaData.get_key_fields(
            projector,
            cls.ticket_scid,
        )


class TicketsWithIterations(Tickets):
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
    roles = EmployeesIterations.roles
    post_timestamp = EmployeesIterations.post_timestamp
    post_tribe_id = EmployeesIterations.post_tribe_id
    post_tent_id = EmployeesIterations.post_tent_id
    post_reply_id = EmployeesIterations.post_reply_id
    post_component_id = EmployeesIterations.post_component_id
    post_feature_id = EmployeesIterations.post_feature_id
    resolution_in_hours = ResolutionTime.resolution_in_hours
    lifetime_in_hours = ResolutionTime.lifetime_in_hours

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field]:
        return tuple()

    @classmethod
    def get_index_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field]:
        return MetaData.get_key_fields(
            projector,
            cls.user_crmid,
            cls.ticket_scid,
            cls.emp_post_id,
        )

    @classmethod
    def get_alias(cls) -> str:
        return 't'

    @classmethod
    def get_indices(cls) -> Sequence[str]:
        tbl = cls.get_name()
        return (
            sqlite_index.create_index(
                tbl=tbl,
                cols=cls.get_index_fields(),
                name='unique_cols',
                unique=True,
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.user_crmid,
                    cls.ticket_scid,
                    cls.creation_date,
                    cls.ticket_type,
                    cls.license_status,
                    cls.emp_position_id,
                    cls.is_private,
                    cls.tribes_ids,
                    cls.tent_id,
                ),
                name='tickets_inner',
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.user_crmid,
                    cls.emp_post_id,
                    cls.creation_date,
                    cls.ticket_type,
                    cls.license_status,
                    cls.emp_position_id,
                    cls.is_private,
                    cls.tribes_ids,
                    cls.tent_id,
                ),
                name='iterations_inner',
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.user_crmid,
                    cls.creation_date,
                    cls.ticket_type,
                    cls.license_status,
                    cls.emp_position_id,
                    cls.is_private,
                    cls.tribes_ids,
                    cls.tent_id,
                    cls.user_id,
                    cls.ticket_scid,
                    cls.emp_post_id,
                ),
                name='outer',
            ),
        )


class TicketsWithIterationsRaw(MetaData):
    user_id = TicketsWithIterations.user_id
    is_employee = TicketsWithIterations.is_employee
    ticket_scid = TicketsWithIterations.ticket_scid
    csi = Field(TEXT)
    ticket_type = TicketsWithIterations.ticket_type
    tribes_names = TicketsWithIterations.tribes_names
    tent_name = TicketsWithIterations.tent_name
    platforms = TicketsWithIterations.platforms
    products = TicketsWithIterations.products
    ticket_tags = TicketsWithIterations.ticket_tags
    is_private = TicketsWithIterations.is_private
    creation_date = TicketsWithIterations.creation_date
    license_name = Field(TEXT, alias='most_appropriate_license')
    parent_license_name = Field(TEXT, alias='parent_license')
    subscription_start = TicketsWithIterations.subscription_start
    expiration_date = TicketsWithIterations.expiration_date
    license_status = TicketsWithIterations.license_status
    conversion_status = TicketsWithIterations.conversion_status
    reply = Field(TEXT)
    component = Field(TEXT)
    feature = Field(TEXT)
    builds = TicketsWithIterations.builds
    fixed_in_builds = TicketsWithIterations.fixed_in_builds
    fixed_by = TicketsWithIterations.fixed_by
    fixed_on = TicketsWithIterations.fixed_on
    ticket_status = TicketsWithIterations.ticket_status
    closed_by = TicketsWithIterations.closed_by
    closed_on = TicketsWithIterations.closed_on
    resolution_in_hours = TicketsWithIterations.resolution_in_hours
    lifetime_in_hours = TicketsWithIterations.lifetime_in_hours
    severity = TicketsWithIterations.severity
    converted_to_bug_on = TicketsWithIterations.converted_to_bug_on
    duplicated_to_ticket_type = TicketsWithIterations.duplicated_to_ticket_type
    duplicated_to_ticket_scid = TicketsWithIterations.duplicated_to_ticket_scid
    assigned_to = TicketsWithIterations.assigned_to
    operating_system = Field(TEXT)
    ide = Field(TEXT)
    emp_post_id = TicketsWithIterations.emp_post_id
    emp_name = TicketsWithIterations.emp_name
    emp_position_name = TicketsWithIterations.emp_position_name
    emp_tribe_name = TicketsWithIterations.emp_tribe_name
    emp_tent_name = TicketsWithIterations.emp_tent_name
    roles = TicketsWithIterations.roles
    post_timestamp = TicketsWithIterations.post_timestamp
    post_tribe_name = Field(TEXT)
    post_tent_name = Field(TEXT)
    post_reply = Field(TEXT)
    post_component = Field(TEXT)
    post_feature = Field(TEXT)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field | str | Any]:
        return tuple()

    @classmethod
    def get_alias(cls) -> str:
        return 't'


class CSI(MetaData):
    ticket_scid = TicketsWithIterations.ticket_scid
    date = Field(TEXT)
    rating = Field(INTEGER)
