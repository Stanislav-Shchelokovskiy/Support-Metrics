from toolbox.sql.repository import Repository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    TicketsTagsMeta,
    TicketsTypesMeta,
)


class TicketsTagsRepository(Repository):
    """
    Loads tags we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_ticket_tags_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsTagsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTagsMeta.get_values()


class TicketsTypesRepository(Repository):
    """
    Loads tickets types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_types_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsTypesMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTypesMeta.get_values()
