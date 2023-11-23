from collections.abc import Sequence, Callable
from typing import Any
from toolbox.sql.meta_data import MetaData, KnotMeta, IntKnotMeta
from toolbox.sql.field import Field, TEXT, INTEGER
import toolbox.sql.generators.sqlite.statements as sqlite_index
from sql_queries.meta.aggs import Tickets


class Customers(KnotMeta):
    pass


class CustomersGroups(MetaData):
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


class TrackedCustomersGroups(MetaData):
    user_crmid = Tickets.user_crmid
    id = KnotMeta.id
    name = KnotMeta.name
    assignment_date = Field(TEXT)
    removal_date = Field(TEXT)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field | str | Any]:
        return MetaData.get_key_fields(
            projector,
            cls.user_crmid,
            cls.id,
        )

    @classmethod
    def get_indices(cls) -> Sequence[str]:
        tbl = cls.get_name()
        return (
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.assignment_date,
                    cls.id,
                    cls.user_crmid,
                    cls.removal_date,
                ),
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.user_crmid,
                    cls.assignment_date,
                    cls.id,
                ),
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.id,
                    cls.name,
                ),
            ),
        )


class TrackedGroups(KnotMeta):
    id = TrackedCustomersGroups.id
    name = TrackedCustomersGroups.name

    @classmethod
    def get_name(cls) -> str:
        return TrackedCustomersGroups.get_name()


class BaselineAlignedMode(TrackedCustomersGroups):
    days_since_baseline = Field(INTEGER)


class LicenseStatuses(IntKnotMeta):
    pass


class ConversionStatuses(MetaData):
    id = KnotMeta.id
    name = KnotMeta.name
    license_status_id = Field(INTEGER)
