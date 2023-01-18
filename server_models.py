from pydantic import BaseModel


class FilterParametersNode(BaseModel):
    include: bool
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


class TicketsWithIterationsParams(BaseModel):
    tribes: FilterParametersNode
    customers_groups: FilterParametersNode
    tickets_types: FilterParametersNode
    tickets_tags: FilterParametersNode
    replies_types: FilterParametersNode
    components: FilterParametersNode
    features: FilterParametersNode
    license_statuses: FilterParametersNode
    conversion_statuses: FilterParametersNode
    platforms: FilterParametersNode
    products: FilterParametersNode
    positions: FilterParametersNode
    emp_tribes: FilterParametersNode
    employees: FilterParametersNode
    customers: FilterParametersNode


class StatAppState(BaseModel):
    state: str
