from sql_queries.customers_activity.meta import EmployeesMeta
from repository.customers_activity.local.sql_query_params_generator.sql_filter_clause_generator import (
    FilterParametersNode,
    SqlFilterClauseFromFilterParametersGenerator,
)


class EmployeesSqlFilterClauseGenerator:

    @staticmethod
    def _generate_positions_filter(position_ids: FilterParametersNode) -> str:
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params=position_ids
        )
        return generate_filter(
            col=EmployeesMeta.position_id,
            values=position_ids.values,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_positions_tribes_filter(
        position_ids: FilterParametersNode,
        tribe_ids: FilterParametersNode,
    ) -> str:
        positions_fitler = EmployeesSqlFilterClauseGenerator._generate_positions_filter(
            position_ids=position_ids
        )
        generate_filter = SqlFilterClauseFromFilterParametersGenerator.generate_in_filter(
            params=tribe_ids
        )
        tribes_filter = generate_filter(
            col=EmployeesMeta.tribe_id,
            values=tribe_ids.values,
            filter_prefix=' AND' if positions_fitler else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )
        return positions_fitler + tribes_filter
