from pydantic import BaseModel


class TribeParams(BaseModel):
    tribes: list[str]


class FeatureParams(TribeParams):
    components: list[str]


class ProductParams(TribeParams):
    platforms: list[str]


class FilterParametersNode(BaseModel):
    include: bool
    values: list[int | str]


class EmployeeParams(BaseModel):
    tribes: FilterParametersNode
    positions: FilterParametersNode


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


class StatAppState(BaseModel):
    state: str


class ConversionStatusParams(BaseModel):
    license_statuses: list[int]
