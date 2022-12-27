from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import ComponentsFeaturesMeta


class CATSqlFilterClauseGenerator:

    @staticmethod
    def generate_components_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=tribe_ids,
            col=ComponentsFeaturesMeta.tribe_id,
            filter_prefix='WHERE',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(
        tribe_ids: list[str],
        component_ids: list[str],
    ) -> str:
        tribes_fitler = CATSqlFilterClauseGenerator.generate_components_filter(
            tribe_ids=tribe_ids
        )
        components_filter = SqlFilterClauseGenerator().generate_in_filter(
            values=component_ids,
            col=ComponentsFeaturesMeta.component_id,
            filter_prefix=' AND' if tribes_fitler else 'WHERE',
            values_converter=lambda val: f"'{val}'",
        )
        return tribes_fitler + components_filter
