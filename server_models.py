from typing import Literal
from pydantic import BaseModel, Field


class FilterNode(BaseModel):
    include: bool


class FilterParameterNode(FilterNode):
    value: int | str


class FilterParametersNode(FilterNode):
    values: list[int | str]


class TribeParams(BaseModel):
    tribes: FilterParametersNode


class FeatureParams(TribeParams):
    components: FilterParametersNode


class ProductParams(TribeParams):
    platforms: FilterParametersNode


class EmployeeParams(BaseModel):
    tribes: FilterParametersNode
    positions: FilterParametersNode


class ConversionStatusParams(BaseModel):
    license_statuses: FilterParametersNode


class CustomersParams(BaseModel):
    customers: list[str]


class Percentile(BaseModel):
    metric: Literal['tickets', 'iterations']
    value: FilterParameterNode


# yapf: disable
class TicketsWithIterationsParams(BaseModel):
    percentile: Percentile = Field(alias='Percentile')
    tribe_ids: FilterParametersNode = Field(alias='Tribes')
    platforms_ids: FilterParametersNode = Field(alias='Platforms')
    products_ids: FilterParametersNode = Field(alias='Products')
    tickets_tags: FilterParametersNode = Field(alias='Ticket tags')
    tickets_types: FilterParametersNode = Field(alias='Ticket types')
    reffered_ticket_types: FilterParametersNode = Field(alias='Reffered ticket types')
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


class StatAppState(BaseModel):
    state: str
