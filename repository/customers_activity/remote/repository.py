from toolbox.sql.base_repository import BaseRepository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    CustomersTagsMeta,
    CustomersActivityMeta,
)


class GroupsRepository(BaseRepository):
    """
    Loads groups we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_groups_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersGroupsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TagsRepository(BaseRepository):
    """
    Loads tags we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tags_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersTagsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersTagsMeta.get_values()


class TicketsWithIterationsRepository(BaseRepository):
    """
    Loads customers with their tickets and iterations.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **CustomersActivityMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersActivityMeta.get_values()
