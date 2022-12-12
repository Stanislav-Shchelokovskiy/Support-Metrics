from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from toolbox.utils.converters import DF_to_JSON
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    TicketsTagsMeta,
    TicketsWithIterationsPeriodMeta,
    TicketsTypesMeta,
    TicketsWithIterationsMeta,
    TicketsWithIterationsAggregatesMeta,
    ReplyTypesMeta,
    ControlsFeaturesMeta,
)
from repository.customers_activity.local.sql_query_params_generator import (
    CATSqlFilterClauseGenerator,
    TicketsWithIterationsAggregatesSqlFilterClauseGenerator,
)


class TicketsWithIterationsRepository(SqliteRepository):
    """
    Interface to a local table storing customers with their tickets and iterations.
    """

    def get_period_json(self) -> str:
        # yapf: disable
        df = self.execute_query(
                query_file_path=CustomersActivitySqlPathIndex.get_tickets_with_iterations_period_path(),
                query_format_params={
                    'table_name': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
                    **TicketsWithIterationsPeriodMeta.get_attrs(),
                }
            ).reset_index(drop=True)
        # yapf: enable
        return DF_to_JSON.convert(df.iloc[0], orient='index')


class CustomersGroupsRepository(SqliteRepository):
    """
    Interface to a local table storing customers groups.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(CustomersGroupsMeta.get_values()),
            'table_name': CustomersActivityDBIndex.get_customers_groups_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TicketsTypesRepository(SqliteRepository):
    """
    Interface to a local table storing tickets types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(TicketsTypesMeta.get_values()),
            'table_name': CustomersActivityDBIndex.get_tickets_types_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTypesMeta.get_values()


class TicketsTagsRepository(SqliteRepository):
    """
    Interface to a local table storing tickets tags.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(TicketsTagsMeta.get_values()),
            'table_name': CustomersActivityDBIndex.get_tickets_tags_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTagsMeta.get_values()


class ReplyTypesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(ReplyTypesMeta.get_values()),
            'table_name': CustomersActivityDBIndex.get_replies_types_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ReplyTypesMeta.get_values()


class ControlsRepository(SqliteRepository):
    """
    Interface to a local table storing CAT controls.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns':
                ', '.join(
                    [
                        ControlsFeaturesMeta.tribe_id,
                        ControlsFeaturesMeta.control_id,
                        ControlsFeaturesMeta.control_name,
                    ]
                ),
            'table_name':
                CustomersActivityDBIndex.get_controls_features_name(),
            'filter_clause':
                CATSqlFilterClauseGenerator.generate_controls_filter(
                    tribe_ids=kwargs['tribe_ids']
                )
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            ControlsFeaturesMeta.tribe_id,
            ControlsFeaturesMeta.control_id,
            ControlsFeaturesMeta.control_name,
        ]


class FeaturesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT features.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns':
                ', '.join(
                    [
                        ControlsFeaturesMeta.tribe_id,
                        ControlsFeaturesMeta.control_id,
                        ControlsFeaturesMeta.feature_id,
                        ControlsFeaturesMeta.feature_name,
                    ]
                ),
            'table_name':
                CustomersActivityDBIndex.get_controls_features_name(),
            'filter_clause':
                CATSqlFilterClauseGenerator.generate_features_filter(
                    tribe_ids=kwargs['tribe_ids'],
                    control_ids=kwargs['control_ids'],
                )
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            ControlsFeaturesMeta.tribe_id,
            ControlsFeaturesMeta.control_id,
            ControlsFeaturesMeta.feature_id,
            ControlsFeaturesMeta.feature_name,
        ]


class TicketsWithIterationsRawRepository(SqliteRepository):

    def get_main_query_path(self, kwargs: dict) -> str:
        # yapf: disable
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        generator = TicketsWithIterationsAggregatesSqlFilterClauseGenerator
        return {
            'table_name': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
            TicketsWithIterationsMeta.creation_date: TicketsWithIterationsMeta.creation_date,
            'range_start': kwargs['range_start'],
            'range_end': kwargs['range_end'],
            'customer_groups_filter': generator.generate_customer_groups_filter(params=kwargs['customers_groups']),
            'ticket_types_filter': generator.generate_ticket_types_filter(params=kwargs['tickets_types']),
            'ticket_tags_filter': generator.generate_ticket_tags_filter(params=kwargs['tickets_tags']),
            'tribes_fitler': generator.generate_tribes_filter(params=kwargs['tribe_ids']),
            'reply_types_filter': generator.generate_reply_types_filter(params=kwargs['reply_ids']),
            'controls_filter': generator.generate_controls_filter(params=kwargs['control_ids']),
            'features_filter': generator.generate_features_filter(params=kwargs['feature_ids'])
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsWithIterationsMeta.get_values()


class TicketsWithIterationsAggregatesRepository(TicketsWithIterationsRawRepository):

    def get_main_query_path(self, kwargs: dict) -> str:
        # yapf: disable
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_aggregates_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            **TicketsWithIterationsAggregatesMeta.get_attrs(),
            'group_by_period': kwargs['group_by_period'],
            **TicketsWithIterationsRawRepository.get_main_query_format_params(self, kwargs)
        }
    #yapf: enable

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            TicketsWithIterationsAggregatesMeta.period,
            TicketsWithIterationsAggregatesMeta.tickets,
            TicketsWithIterationsAggregatesMeta.iterations,
        ]
