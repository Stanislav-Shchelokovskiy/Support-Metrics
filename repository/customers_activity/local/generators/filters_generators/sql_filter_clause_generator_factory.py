from typing import Protocol, Any, runtime_checkable
from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator


class BaseNode(Protocol):

    def get_field_aliases(self) -> dict[str, str]:
        ...

    def get_field_values(self) -> dict[str, Any]:
        ...

    def get_append_operator(self) -> str:
        ...


@runtime_checkable
class FilterParametersNode(BaseNode, Protocol):
    include: bool
    values: list


class FilterParameterNode(BaseNode, Protocol):
    include: bool
    value: int


def params_guard(cls):

    def decorate(func):

        def guard(**kwargs):
            if any(arg is None for arg in kwargs.values()):
                return ''
            return func(**kwargs)

        return guard

    for attr in cls.__dict__:
        if callable(getattr(cls, attr)):
            setattr(cls, attr, decorate(getattr(cls, attr)))
    return cls


class SqlFilterClauseFromFilterParametersGeneratorFactory:

    def get_like_filter_generator(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_like_filter if params.include else generator.generate_not_like_filter
        return generate_filter

    def get_in_filter_generator(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_in_filter if params.include else generator.generate_not_in_filter
        return generate_filter
