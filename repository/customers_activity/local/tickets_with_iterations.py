from toolbox.sql.repository import SqliteRepository
from toolbox.utils.converters import DF_to_JSON
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    TicketsWithIterationsAggregatesMeta,
    TicketsWithIterationsRawMeta,
    TicketsWithIterationsMeta,
    TicketsWithIterationsPeriodMeta,
)
from repository.customers_activity.local.sql_query_params_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator


#yapf: disable
class TicketsPeriodRepository(SqliteRepository):
    """
    Interface to a local table storing min and max boundarise
    for tickets and iterations.
    """
    def get_period_json(self) -> str:

        df = self.execute_query(
                query_file_path=CustomersActivitySqlPathIndex.get_tickets_period_path(),
                query_format_params={
                    'table_name': CustomersActivityDBIndex.get_tickets_with_licenses_name(),
                    **TicketsWithIterationsPeriodMeta.get_attrs(),
                }
            ).reset_index(drop=True)
        return DF_to_JSON.convert(df.iloc[0], orient='index')


class TicketsWithIterationsRawRepository(SqliteRepository):
    """
    Interface to a local table storing raw tickets with iterations data.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path()

    def get_general_format_params(self, kwargs:dict)-> dict[str,str]:
        generator = TicketsWithIterationsSqlFilterClauseGenerator
        return {
            'tickets_with_iterations_table': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
            TicketsWithIterationsMeta.creation_date: TicketsWithIterationsMeta.creation_date,
            'range_start': kwargs['range_start'],
            'range_end': kwargs['range_end'],
            'customer_groups_filter': generator.generate_customer_groups_filter(params=kwargs['customers_groups']),
            'ticket_types_filter': generator.generate_ticket_types_filter(params=kwargs['tickets_types']),
            'ticket_tags_filter': generator.generate_ticket_tags_filter(params=kwargs['tickets_tags']),
            'tribes_filter': generator.generate_tribes_filter(params=kwargs['tribe_ids']),
            'reply_types_filter': generator.generate_reply_types_filter(params=kwargs['reply_ids']),
            'components_filter': generator.generate_components_filter(params=kwargs['components_ids']),
            'features_filter': generator.generate_features_filter(params=kwargs['feature_ids']),
            'license_status_filter' : generator.generate_license_status_filter(params=kwargs['license_statuses']),
            'conversion_status_filter' : generator.generate_conversion_status_filter(params=kwargs['conversion_statuses']),
            'platforms_filter': generator.generate_platforms_filter(params=kwargs['platforms_ids']),
            'products_filter': generator.generate_products_filter(params=kwargs['products_ids']),
            'positions_filter': generator.generate_positions_filter(params=kwargs['positions_ids']),
            'emp_tribes_filter': generator.generate_emp_tribes_filter(params=kwargs['emp_tribe_ids']),
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
