from typing import Literal, Optional, Any
from pydantic import BaseModel, Field


class ServerModel(BaseModel):

    def get_field_aliases(self) -> dict[str, str]:
        return {k: v.alias for k, v in self.__fields__.items()}

    def get_field_values(self) -> dict[str, Any]:
        return self.__dict__

    def get_append_operator(self) -> str:
        return 'and'


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


class ProductParams(TribeParams):
    platforms: FilterParametersNode


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


class TicketsTypes(ServerModel):
    tickets_types: FilterParametersNode = Field(alias='Ticket types')
    referred_tickets_types: Optional[FilterParametersNode] = Field(alias='Referred ticket types')

    def get_append_operator(self) -> str:
        return 'or' if self.referred_tickets_types.include else 'and'


# yapf: disable
class TicketsWithIterationsParams(ServerModel):
    percentile: Percentile = Field(alias='Percentile')
    tribe_ids: FilterParametersNode = Field(alias='Tribes')
    platforms_ids: FilterParametersNode = Field(alias='Platforms')
    products_ids: FilterParametersNode = Field(alias='Products')
    tickets_tags: FilterParametersNode = Field(alias='Ticket tags')
    tickets_types: TicketsTypes = Field(alias='Ticket types')
    customers_groups: FilterParametersNode = Field(alias='User groups')
    license_statuses: FilterParametersNode = Field(alias='User types')
    conversion_statuses: FilterParametersNode = Field(alias='User conversion types')
    positions_ids: FilterParametersNode = Field(alias='Employees positions')
    emp_tribe_ids: FilterParametersNode = Field(alias='Employees tribes')
    emp_ids: FilterParametersNode = Field(alias='Employees')
    reply_ids: FilterParametersNode = Field(alias='CAT replies types')
    components_ids: FilterParametersNode = Field(alias='CAT components')
    feature_ids: FilterParametersNode = Field(alias='CAT features')
    customers_crmids: FilterParametersNode = Field(alias='Customers')
# yapf: enable


class StatAppState(ServerModel):
    state: str
