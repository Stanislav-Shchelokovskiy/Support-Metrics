from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.index.path.extract as RemotePathIndex


class Tribes(RepositoryAlchemyQueries):
    """
    Query to load tribes.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.tribes
