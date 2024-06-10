from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.index.path.remote as RemotePathIndex


class Tents(RepositoryAlchemyQueries):
    """
    Query to load tents.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.tents
