from collections.abc import Sequence, Callable
from typing import Any
from toolbox.sql.meta_data import MetaData, KnotMeta
from toolbox.sql.field import Field, TEXT
import toolbox.sql.generators.sqlite.statements as sqlite_index


class Positions(KnotMeta):
    pass


class EmpTribes(KnotMeta):
    pass


class EmpTents(KnotMeta):
    pass


class EmployeesIterations(MetaData):
    ticket_id = Field(TEXT)
    post_id = Field(TEXT)
    crmid = Field(TEXT)
    scid = Field(TEXT)
    tribe_id = Field(TEXT)
    tent_id = Field(TEXT)
    position_id = Field(TEXT)
    name = Field(TEXT)
    position_name = Field(TEXT)
    tribe_name = Field(TEXT)
    tent_name = Field(TEXT)

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field | str | Any]:
        return MetaData.get_key_fields(
            projector,
            cls.ticket_id,
            cls.post_id,
        )


class Employee(MetaData):
    scid = EmployeesIterations.scid
    name = EmployeesIterations.name

    @classmethod
    def get_name(cls) -> str:
        return Employees.get_name()


class Employees(MetaData):
    tribe_id = EmployeesIterations.tribe_id
    tent_id = EmployeesIterations.tent_id
    position_id = EmployeesIterations.position_id
    crmid = EmployeesIterations.crmid
    scid = Employee.scid
    name = Employee.name
    tribe_name = EmployeesIterations.tribe_name
    tent_name = EmployeesIterations.tent_name
    position_name = EmployeesIterations.position_name

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
                    cls.position_id,
                    cls.tribe_id,
                    cls.tent_id,
                ),
            ),
        )
