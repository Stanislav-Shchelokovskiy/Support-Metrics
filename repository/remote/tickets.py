from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.index.path.remote as RemotePathIndex


class TicketsTags(RepositoryAlchemyQueries):
    """
    Query to load tags we use to filter customers by.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.ticket_tags


class TicketsTypes(RepositoryAlchemyQueries):
    """
    Query to load tickets types.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.tickets_types


class Frameworks(RepositoryAlchemyQueries):
    """
    Query to load frameworks/specifics.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.frameworks


class OperatingSystems(RepositoryAlchemyQueries):
    """
    Query to load operating systems.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.operating_systems


class Builds(RepositoryAlchemyQueries):
    """
    Query to load builds.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.builds


class Severity(RepositoryAlchemyQueries):
    """
    Query to load bug severity values.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.severity


class TicketStatuses(RepositoryAlchemyQueries):
    """
    Query to load ticket statuses.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.ticket_statuses


class IDEs(RepositoryAlchemyQueries):
    """
    Query to load ticket ides.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.ides
