from toolbox.sql.repository import Repository
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


class FrameworksRepository(Repository):
    """
    Loads frameworks/specifics.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_frameworks_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return FrameworksMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return FrameworksMeta.get_values()


class OperatingSystemsRepository(Repository):
    """
    Loads operating systems.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_operating_systems_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return OperatingSystemsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return OperatingSystemsMeta.get_values()


class BuildsRepository(Repository):
    """
    Loads builds.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_builds_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return BuildsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return BuildsMeta.get_values()


class SeverityRepository(Repository):
    """
    Loads bug severity values.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_severity_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return SeverityMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return SeverityMeta.get_values()


class TicketStatusesRepository(Repository):
    """
    Loads ticket statuses.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_ticket_statuses_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketStatusesMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketStatusesMeta.get_values()


class IDEsRepository(Repository):
    """
    Loads ticket ides.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_ides_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return IDEsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return IDEsMeta.get_values()
