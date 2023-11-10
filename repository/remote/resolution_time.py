from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.meta.aggs as aggs
import sql_queries.index.path.extract as RemotePathIndex


class ResolutionTime(RepositoryAlchemyQueries):
    """
    Query to calculate ticket resolution time.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.resolution_time

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {**kwargs, **aggs.ResolutionTime.get_attrs()}
