from typing import Iterable
from toolbox.sql.repository import SqlServerRepository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    TicketsTagsMeta,
    TicketsTypesMeta,
    FrameworksMeta,
    OperatingSystemsMeta,
    BuildsMeta,
    SeverityMeta,
    TicketStatusesMeta,
    IDEsMeta,
)


class TicketsTagsRepository(SqlServerRepository):
    """
    Loads tags we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_ticket_tags_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsTagsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return TicketsTagsMeta.get_values()


class TicketsTypesRepository(SqlServerRepository):
    """
    Loads tickets types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_types_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsTypesMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return TicketsTypesMeta.get_values()


class FrameworksRepository(SqlServerRepository):
    """
    Loads frameworks/specifics.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_frameworks_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return FrameworksMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return FrameworksMeta.get_values()


class OperatingSystemsRepository(SqlServerRepository):
    """
    Loads operating systems.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_operating_systems_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return OperatingSystemsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return OperatingSystemsMeta.get_values()


class BuildsRepository(SqlServerRepository):
    """
    Loads builds.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_builds_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return BuildsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return BuildsMeta.get_values()


class SeverityRepository(SqlServerRepository):
    """
    Loads bug severity values.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_severity_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return SeverityMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return SeverityMeta.get_values()


class TicketStatusesRepository(SqlServerRepository):
    """
    Loads ticket statuses.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_ticket_statuses_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketStatusesMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return TicketStatusesMeta.get_values()


class IDEsRepository(SqlServerRepository):
    """
    Loads ticket ides.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_ides_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return IDEsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> Iterable[str]:
        return IDEsMeta.get_values()
