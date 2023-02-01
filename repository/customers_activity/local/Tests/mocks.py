from typing import Any


class MockFilterNode:

    def get_field_aliases(self) -> dict[str, str]:
        ...

    def get_field_values(self) -> dict[str, Any]:
        return self.__dict__


class MockFilterParametersNode:

    def __init__(self, include: bool, values: list) -> None:
        self.include = include
        self.values = values


class MockTicketTypes:

    def __init__(
        self,
        tickets_types: MockFilterParametersNode,
        reffered_tickets_types: MockFilterParametersNode | None = None
    ) -> None:
        self.tickets_types = tickets_types
        self.reffered_tickets_types = reffered_tickets_types


class MockFilterParameterNode:

    def __init__(self, include: bool, value: str | int) -> None:
        self.include = include
        self.value = value


class MockPercentile:

    def __init__(self, metric: str, value: MockFilterParameterNode) -> None:
        self.metric = metric
        self.value = value
