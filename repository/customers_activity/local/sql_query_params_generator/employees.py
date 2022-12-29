from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import EmployeesMeta


class EmployeesSqlFilterClauseGenerator:

    @staticmethod
    def generate_positions_filter(position_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=position_ids,
            col=EmployeesMeta.position_id,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_filter(
        position_ids: list[str],
        tribe_ids: list[str],
    ) -> str:
        positions_fitler = EmployeesSqlFilterClauseGenerator.generate_positions_filter(
            position_ids=position_ids
        )
        tribes_filter = SqlFilterClauseGenerator().generate_in_filter(
            values=tribe_ids,
            col=EmployeesMeta.tribe_id,
            filter_prefix=' AND' if positions_fitler else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )
        return positions_fitler + tribes_filter
