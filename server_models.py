from pydantic import BaseModel


class TribeParams(BaseModel):
    tribes: list[str]


class ControlParams(TribeParams):
    controls: list[str]


class TicketsWithIterationsParams(TribeParams):
    customers_groups: list[str]
    tickets_types: list[int]
    tickets_tags: list[int]
    replies_types: list[str]
    controls: list[str]
    features: list[str]
