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
    TicketsWithIterationsAggregates,
)
from repository.customers_activity.local.sql_query_params_generator import TicketsWithIterationsAggregatesSqlParamsGenerator


class TicketsWithIterationsRepository(SqliteRepository):
    """
    An interface to local table storing customers with their tickets and iterations.
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
    An interface to local table storing customers groups.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_select_all_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'table_name': CustomersActivityDBIndex.get_customers_groups_name(),
            'columns': ', '.join(CustomersGroupsMeta.get_values())
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TicketsTypesRepository(SqliteRepository):
    """
    An interface to local table storing tickets types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_select_all_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'table_name': CustomersActivityDBIndex.get_tickets_types_name(),
            'columns': ', '.join(TicketsTypesMeta.get_values())
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTypesMeta.get_values()


class TicketsTagsRepository(SqliteRepository):
    """
    An interface to local table storing tickets tags.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_select_all_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'table_name': CustomersActivityDBIndex.get_tickets_tags_name(),
            'columns': ', '.join(TicketsTagsMeta.get_values())
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTagsMeta.get_values()


class TicketsWithIterationsAggregatesRepository(SqliteRepository):
    # yapf: disable
    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_aggregates_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            **TicketsWithIterationsAggregates.get_attrs(),
            'table_name': CustomersActivityDBIndex.get_tickets_with_iterations_name(),
            'group_by_period': kwargs['group_by_period'],
            'range_start': kwargs['range_start'],
            'range_end': kwargs['range_end'],
            'customer_groups_filter': TicketsWithIterationsAggregatesSqlParamsGenerator.generate_customer_groups_filter(kwargs['customers_groups'])
        }
    # yapf: enable

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            TicketsWithIterationsAggregates.period,
            TicketsWithIterationsAggregates.tickets,
            TicketsWithIterationsAggregates.iterations,
        ]
