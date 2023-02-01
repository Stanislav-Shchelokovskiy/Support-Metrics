class MockFilterParametersNode:

    def __init__(self, include: bool, values: list) -> None:
        self.include = include
        self.values = values


class MockTicketTypes:

    def __init__(
        self,
        tickets_types: MockFilterParametersNode,
        referred_tickets_types: MockFilterParametersNode | None = None
    ) -> None:
        self.tickets_types = tickets_types
        self.referred_tickets_types = referred_tickets_types


class MockFilterParameterNode:

    def __init__(self, include: bool, value: str | int) -> None:
        self.include = include
        self.value = value


class MockPercentile:

    def __init__(self, metric: str, value: MockFilterParameterNode) -> None:
        self.metric = metric
        self.value = value
