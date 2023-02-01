from typing import Protocol, Any
from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator


class BaseNode(Protocol):

    def get_field_aliases(self) -> dict[str, str]:
        ...

    def get_field_values(self) -> dict[str, Any]:
        ...

    def get_append_operator(self) -> str:
        ...


class FilterParametersNode(BaseNode, Protocol):
    include: bool
    values: list


class FilterParameterNode(BaseNode, Protocol):
    include: bool
    value: int


class SqlFilterClauseFromFilterParametersGenerator:

    @staticmethod
    def generate_like_filter(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_like_filter if params.include else generator.generate_not_like_filter
        return generate_filter

    @staticmethod
    def generate_in_filter(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_in_filter if params.include else generator.generate_not_in_filter
        return generate_filter
