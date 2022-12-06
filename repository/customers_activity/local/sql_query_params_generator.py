from toolbox.sql.generators.filter_clause_generator import SqlFilterClauseGenerator
from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    ControlsFeaturesMeta,
)


class TicketsWithIterationsAggregatesSqlFilterClauseGenerator:

    @staticmethod
    def generate_customer_groups_filter(customer_groups: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_like_filter(
            col=TicketsWithIterationsMeta.user_groups,
            values=customer_groups,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_ticket_types_filter(tickets_types: list[int]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.ticket_type,
            values=tickets_types,
            filter_prefix='AND ',
            values_converter=str,
        )

    @staticmethod
    def generate_ticket_tags_filter(tickets_tags: list[int]) -> str:
        return SqlFilterClauseGenerator().generate_like_filter(
            col=TicketsWithIterationsMeta.ticket_tags,
            values=tickets_tags,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_tribes_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.tribe_id,
            values=tribe_ids,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_reply_types_filter(reply_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.reply_id,
            values=reply_ids,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_controls_filter(control_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.control_id,
            values=control_ids,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(feature_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.feature_id,
            values=feature_ids,
            filter_prefix='AND ',
            values_converter=lambda val: f"'{val}'",
        )


class CATSqlFilterClauseGenerator:

    @staticmethod
    def generate_controls_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            values=tribe_ids,
            col=ControlsFeaturesMeta.tribe_id,
            filter_prefix='WHERE ',
            values_converter=lambda val: f"'{val}'",
        )

    @staticmethod
    def generate_features_filter(
        tribe_ids: list[str],
        control_ids: list[str],
    ) -> str:
        return CATSqlFilterClauseGenerator.generate_controls_filter(
            tribe_ids=tribe_ids
        ) + SqlFilterClauseGenerator().generate_in_filter(
            values=control_ids,
            col=ControlsFeaturesMeta.control_id,
            filter_prefix=' AND ',
            values_converter=lambda val: f"'{val}'",
        )
