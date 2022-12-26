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
    ComponentsFeaturesMeta,
    TicketsWithIterationsRawMeta,
    LicenseStatusesMeta,
    ConversionStatusesMeta,
    PlatformsProductsMeta,
    PositionsMeta,
)
from repository.customers_activity.local.sql_query_params_generator import (
    CATSqlFilterClauseGenerator,
    TicketsWithIterationsSqlFilterClauseGenerator,
    ConversionStatusesSqlFilterClauseGenerator,
    PlatformsProductsSqlFilterClauseGenerator,
)


# yapf: disable
class TicketsWithIterationsPeriodRepository(SqliteRepository):
    """
    Interface to a local table storing min and max boundarise
    for tickets and iterations.
    """
    def get_period_json(self) -> str:

        df = self.execute_query(
                query_file_path=CustomersActivitySqlPathIndex.get_tickets_with_iterations_period_path(),
                query_format_params={
                    'table_name': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
                    **TicketsWithIterationsPeriodMeta.get_attrs(),
                }
            ).reset_index(drop=True)
        return DF_to_JSON.convert(df.iloc[0], orient='index')


class CustomersGroupsRepository(SqliteRepository):
    """
    Interface to a local table storing customers groups.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
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
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_types_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTypesMeta.get_values()


class LicenseStatusesRepository(SqliteRepository):
    """
    Interface to a local table storing license statuses.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_license_statuses_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return LicenseStatusesMeta.get_values()


class ConversionStatusesRepository(SqliteRepository):
    """
    Interface to a local table storing conversion statuses.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_conversion_statuses_name(),
            'filter_clause': ConversionStatusesSqlFilterClauseGenerator.generate_filter(
                    license_status_ids=kwargs['license_status_ids']
                ),
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ConversionStatusesMeta.get_values()


class PositionsRepository(SqliteRepository):
    """
    Interface to a local table storing available positions.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_positions_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return PositionsMeta.get_values()


class TicketsTagsRepository(SqliteRepository):
    """
    Interface to a local table storing tickets tags.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
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
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_replies_types_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ReplyTypesMeta.get_values()


class ComponentsRepository(SqliteRepository):
    """
    Interface to a local table storing CAT components.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': 'DISTINCT',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_components_features_name(),
            'filter_clause': CATSqlFilterClauseGenerator.generate_components_filter(
                    tribe_ids=kwargs['tribe_ids']
                )
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            ComponentsFeaturesMeta.component_id,
            ComponentsFeaturesMeta.component_name,
        ]


class FeaturesRepository(SqliteRepository):
    """
    Interface to a local table storing CAT features
    available for the specified components.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_components_features_name(),
            'filter_clause': CATSqlFilterClauseGenerator.generate_features_filter(
                    tribe_ids=kwargs['tribe_ids'],
                    component_ids=kwargs['component_ids'],
                )
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            ComponentsFeaturesMeta.feature_id,
            ComponentsFeaturesMeta.feature_name,
        ]


class PlatformsRepository(SqliteRepository):
    """
    Interface to a local table storing available platforms.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': 'DISTINCT',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_platforms_products_name(),
            'filter_clause': PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
                    tribe_ids=kwargs['tribe_ids']
                )
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            PlatformsProductsMeta.platform_id,
            PlatformsProductsMeta.platform_name,
        ]


class ProductsRepository(SqliteRepository):
    """
    Interface to a local table storing products
    available for specified platforms.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_platforms_products_name(),
            'filter_clause': PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
                    tribe_ids=kwargs['tribe_ids'],
                    platform_ids=kwargs['platform_ids'],
                )
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
                PlatformsProductsMeta.product_id,
                PlatformsProductsMeta.product_name,
        ]


class TicketsWithIterationsRawRepository(SqliteRepository):
    """
    Interface to a local table storing raw tickets with iterations data.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path()

    def get_general_format_params(self, kwargs:dict)-> dict[str,str]:
        generator = TicketsWithIterationsSqlFilterClauseGenerator
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
            'components_filter': generator.generate_components_filter(params=kwargs['components_ids']),
            'features_filter': generator.generate_features_filter(params=kwargs['feature_ids']),
            'license_status_filter' : generator.generate_license_status_filter(params=kwargs['license_statuses']),
            'conversion_status_filter' : generator.generate_conversion_status_filter(params=kwargs['conversion_statuses']),
            'platforms_filter': generator.generate_platforms_filter(params=kwargs['platforms_ids']),
            'products_filter': generator.generate_products_filter(params=kwargs['products_ids']),
        }

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'replies_types_table': CustomersActivityDBIndex.get_replies_types_name(),
            'components_features_table': CustomersActivityDBIndex.get_components_features_name(),
            'license_statuses_table': CustomersActivityDBIndex.get_license_statuses_name(),
            'conversion_statuses_table': CustomersActivityDBIndex.get_conversion_statuses_name(),
            **TicketsWithIterationsRawMeta.get_attrs(),
            **self.get_general_format_params(kwargs)
        }


    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsWithIterationsRawMeta.get_values()


class TicketsWithIterationsAggregatesRepository(TicketsWithIterationsRawRepository):
    """
    Interface to a local table storing aggregated tickets with iterations data.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_aggregates_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            **TicketsWithIterationsAggregatesMeta.get_attrs(),
            'group_by_period': kwargs['group_by_period'],
            **TicketsWithIterationsRawRepository.get_general_format_params(self, kwargs)
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            TicketsWithIterationsAggregatesMeta.period,
            TicketsWithIterationsAggregatesMeta.tickets,
            TicketsWithIterationsAggregatesMeta.iterations,
        ]
#yapf: enable