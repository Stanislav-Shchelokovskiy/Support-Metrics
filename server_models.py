from pydantic import BaseModel


class TribeParams(BaseModel):
    tribes: list[str]


class ControlParams(TribeParams):
    controls: list[str]


class FilterParametersNode(BaseModel):
    include: bool
    values: list[int | str]


class TicketsWithIterationsParams(BaseModel):
    tribes: FilterParametersNode
    customers_groups: FilterParametersNode
    tickets_types: FilterParametersNode
    tickets_tags: FilterParametersNode
    replies_types: FilterParametersNode
    controls: FilterParametersNode
    features: FilterParametersNode
