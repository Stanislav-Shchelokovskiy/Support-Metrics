from typing import Protocol
from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator


class FilterParametersNode(Protocol):
    include: bool
    values: list


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
