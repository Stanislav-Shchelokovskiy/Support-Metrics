class MockFilterParametersNode:

    def __init__(self, include: bool, values: list) -> None:
        self.include = include
        self.values = values


class FilterParameterNode:

    def __init__(self, include: bool, value: str | int) -> None:
        self.include = include
        self.value = value


class Percentile:

    def __init__(self, metric: str, value: FilterParameterNode) -> None:
        self.metric = metric
        self.value = value
