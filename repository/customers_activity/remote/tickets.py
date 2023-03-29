from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
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


class TicketsTags(RepositoryAlchemyQueries):
    """
    Query to load tags we use to filter customers by.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_ticket_tags_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketsTagsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsTagsMeta.get_values()


class TicketsTypes(RepositoryAlchemyQueries):
    """
    Query to load tickets types.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_types_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketsTypesMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsTypesMeta.get_values()


class Frameworks(RepositoryAlchemyQueries):
    """
    Query to load frameworks/specifics.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_frameworks_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return FrameworksMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return FrameworksMeta.get_values()


class OperatingSystems(RepositoryAlchemyQueries):
    """
    Query to load operating systems.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_operating_systems_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return OperatingSystemsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return OperatingSystemsMeta.get_values()


class Builds(RepositoryAlchemyQueries):
    """
    Query to load builds.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_builds_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return BuildsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return BuildsMeta.get_values()


class Severity(RepositoryAlchemyQueries):
    """
    Query to load bug severity values.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_severity_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return SeverityMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return SeverityMeta.get_values()


class TicketStatuses(RepositoryAlchemyQueries):
    """
    Query to load ticket statuses.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_ticket_statuses_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketStatusesMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketStatusesMeta.get_values()


class IDEs(RepositoryAlchemyQueries):
    """
    Query to load ticket ides.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_ides_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return IDEsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return IDEsMeta.get_values()
