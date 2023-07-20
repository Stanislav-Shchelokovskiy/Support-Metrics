from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.meta import (
    TicketsTagsMeta,
    TicketsTypesMeta,
    FrameworksMeta,
    OperatingSystemsMeta,
    BuildsMeta,
    SeverityMeta,
    TicketStatusesMeta,
    IDEsMeta,
)
import sql_queries.index.path.extract as ExtractPathIndex


class TicketsTags(RepositoryAlchemyQueries):
    """
    Query to load tags we use to filter customers by.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.ticket_tags

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketsTagsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsTagsMeta.get_values()


class TicketsTypes(RepositoryAlchemyQueries):
    """
    Query to load tickets types.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.tickets_types

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketsTypesMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsTypesMeta.get_values()


class Frameworks(RepositoryAlchemyQueries):
    """
    Query to load frameworks/specifics.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.frameworks

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return FrameworksMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return FrameworksMeta.get_values()


class OperatingSystems(RepositoryAlchemyQueries):
    """
    Query to load operating systems.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.operating_systems

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return OperatingSystemsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return OperatingSystemsMeta.get_values()


class Builds(RepositoryAlchemyQueries):
    """
    Query to load builds.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.builds

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return BuildsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return BuildsMeta.get_values()


class Severity(RepositoryAlchemyQueries):
    """
    Query to load bug severity values.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.severity

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return SeverityMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return SeverityMeta.get_values()


class TicketStatuses(RepositoryAlchemyQueries):
    """
    Query to load ticket statuses.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.ticket_statuses

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return TicketStatusesMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketStatusesMeta.get_values()


class IDEs(RepositoryAlchemyQueries):
    """
    Query to load ticket ides.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.ides

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return IDEsMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return IDEsMeta.get_values()
