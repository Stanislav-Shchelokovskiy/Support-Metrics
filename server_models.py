from pydantic import BaseModel


class TicketsWithIterationsParams(BaseModel):
    customers_groups: list[str]
    tickets_types: list[int]
    tickets_tags: list[int]
    tribes: list[str]
