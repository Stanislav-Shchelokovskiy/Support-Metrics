from typing import Protocol
from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    ComponentsFeaturesMeta,
)


class FilterParametersNode(Protocol):
    include: bool
    values: list


class TicketsWithIterationsAggregatesSqlFilterClauseGenerator:

    @staticmethod
    def _generate_like_filter(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_like_filter if params.include else generator.generate_not_like_filter
        return generate_filter
    
    @staticmethod
    def _generate_in_filter(params: FilterParametersNode):
        generator = SqlFilterClauseGenerator()
        generate_filter = generator.generate_in_filter if params.include else generator.generate_not_in_filter
        return generate_filter

    @staticmethod
    def generate_customer_groups_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_like_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.user_groups,
            values=params.values,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_ticket_types_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_in_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.ticket_type,
            values=params.values,
            filter_prefix='AND ',
            values_converter=str,
        )

    @staticmethod
    def generate_ticket_tags_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_like_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.ticket_tags,
            values=params.values,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_tribes_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_in_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.tribe_id,
            values=params.values,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_reply_types_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_in_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.reply_id,
            values=params.values,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_components_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_in_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.component_id,
            values=params.values,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(params: FilterParametersNode) -> str:
        generate_filter = TicketsWithIterationsAggregatesSqlFilterClauseGenerator._generate_in_filter(params)
        return generate_filter(
            col=TicketsWithIterationsMeta.feature_id,
            values=params.values,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )


class CATSqlFilterClauseGenerator:

    @staticmethod
    def generate_components_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=tribe_ids,
            col=ComponentsFeaturesMeta.tribe_id,
            filter_prefix='WHERE ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(
        tribe_ids: list[str],
        component_ids: list[str],
    ) -> str:
        return CATSqlFilterClauseGenerator.generate_components_filter(
            tribe_ids=tribe_ids
        ) + SqlFilterClauseGenerator().generate_in_filter(
            values=component_ids,
            col=ComponentsFeaturesMeta.component_id,
            filter_prefix=' AND ',
            values_converter=lambda val: f"'{val}'",
        )
