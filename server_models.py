from typing import Literal, Any
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo 


class ServerModel(BaseModel):

    def get_field_values(self) -> dict[str, Any]:
        return self.__dict__

    def get_field_alias(self, field_name) -> str:
        return self.__fields__[field_name].alias

    def get_append_operator(self) -> str:
        return 'and'

    def get_filter_op(self, field_name) -> str:
        val = self.__dict__[field_name]
        if hasattr(val, 'include'):
            fi: FieldInfo = self.__fields__[field_name].field_info
            if val.include:
                return fi.extra.get('positive_filter_op', 'in')
            return fi.extra.get('negative_filter_op', 'notin')
        raise NotImplementedError


class FilterNode(ServerModel):
    include: bool


class FilterParameterNode(FilterNode):
    value: int | str


class FilterParametersNode(FilterNode):
    values: list[int | str]


class TribeParams(ServerModel):
    tribes: FilterParametersNode


class FeatureParams(TribeParams):
    components: FilterParametersNode


class EmployeeParams(ServerModel):
    tribes: FilterParametersNode
    positions: FilterParametersNode


class ConversionStatusParams(ServerModel):
    license_statuses: FilterParametersNode


class CustomersParams(ServerModel):
    customers: list[str]


class Percentile(ServerModel):
    metric: Literal['tickets', 'iterations']
    value: FilterParameterNode


# yapf: disable
class TicketsWithIterationsParams(ServerModel):
    percentile: Percentile = Field(alias='Percentile')
    is_private: FilterParameterNode | None = Field(alias='Privacy')
    tribe_ids: FilterParametersNode | None = Field(alias='Tribes')
    platforms_ids: FilterParametersNode | None = Field(alias='Platforms')
    products_ids: FilterParametersNode | None = Field(alias='Products')
    tickets_tags: FilterParametersNode | None = Field(alias='Ticket tags')
    tickets_types: FilterParametersNode | None = Field(alias='Ticket types')
    duplicated_to_tickets_types: FilterParametersNode | None = Field(alias='Duplicated to ticket types')
    builds: FilterParametersNode | None = Field(alias='Versions')
    fixed_in_builds: FilterParametersNode | None = Field(alias='Fixed In')
    severity: FilterParametersNode | None = Field(alias='Severity')
    ticket_status: FilterParametersNode | None = Field(alias='Ticket statuses')
    closed_between: FilterParametersNode | None = Field(alias='Closed', positive_filter_op='between', negative_filter_op='notbetween')
    operating_system_id: FilterParametersNode | None = Field(alias='Operating systems')
    frameworks: FilterParametersNode | None = Field(alias='Frameworks/Specifics')
    ide_id: FilterParametersNode | None = Field(alias='IDE')
    customers_groups: FilterParametersNode | None = Field(alias='User groups')
    license_statuses: FilterParametersNode | None = Field(alias='User types')
    conversion_statuses: FilterParametersNode | None = Field(alias='User conversion types')
    positions_ids: FilterParametersNode | None = Field(alias='Employees positions')
    emp_tribe_ids: FilterParametersNode | None = Field(alias='Employees tribes')
    emp_ids: FilterParametersNode | None = Field(alias='Employees')
    assigned_to_ids: FilterParametersNode | None = Field(alias='Assigned to')
    closed_by_ids: FilterParametersNode | None = Field(alias='Closed by')
    fixed_by_ids: FilterParametersNode | None = Field(alias='Fixed by')
    reply_ids: FilterParametersNode | None = Field(alias='CAT replies types')
    components_ids: FilterParametersNode | None = Field(alias='CAT components')
    feature_ids: FilterParametersNode | None = Field(alias='CAT features')
    customers_crmids: FilterParametersNode | None = Field(alias='Customers')
# yapf: enable


class StatAppState(ServerModel):
    state: str
