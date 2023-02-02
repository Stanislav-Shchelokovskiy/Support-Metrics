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
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.generators.periods import PeriodsGenerator
from repository.customers_activity.local.core.tickets_with_iterations_table import get_tickets_with_iterations_table
from repository.customers_activity.local.core.filters import get_creation_date_and_tickets_filters
from configs.customers_activity_config import CustomersActivityConfig


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
                    'table_name': CustomersActivityDBIndex.get_customers_tickets_name(),
                    **TicketsWithIterationsPeriodMeta.get_attrs(),
                    'rank_period_offset': CustomersActivityConfig.get_rank_period_offset(),
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
            'tickets_with_iterations_table': get_tickets_with_iterations_table(kwargs=kwargs, filter_generator=generator),
            'tickets_filter': get_creation_date_and_tickets_filters(kwargs=kwargs, filter_generator=generator),
        }


    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'replies_types_table': CustomersActivityDBIndex.get_cat_replies_types_name(),
            'components_features_table': CustomersActivityDBIndex.get_cat_components_features_name(),
            'license_statuses_table': CustomersActivityDBIndex.get_license_statuses_name(),
            'conversion_statuses_table': CustomersActivityDBIndex.get_conversion_statuses_name(),
            **TicketsWithIterationsRawMeta.get_attrs(),
            'tracked_customer_groups_mode_fields': f', t.original_{TicketsWithIterationsMeta.creation_date}' if kwargs['use_baseline_aligned_mode'] else '',
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
        group_by_period = PeriodsGenerator.generate_group_by_period(
            format=kwargs['group_by_period'],
            field=TicketsWithIterationsMeta.creation_date,
        )
        return {
            **TicketsWithIterationsAggregatesMeta.get_attrs(),
            'group_by_period': group_by_period,
            **TicketsWithIterationsRawRepository.get_general_format_params(self, kwargs)
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            TicketsWithIterationsAggregatesMeta.period,
            TicketsWithIterationsAggregatesMeta.tickets,
            TicketsWithIterationsAggregatesMeta.iterations,
        ]
