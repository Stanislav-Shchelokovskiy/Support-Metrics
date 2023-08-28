from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.meta import KnotMeta
import sql_queries.index.path.extract as ExtractPathIndex


class Tents(RepositoryAlchemyQueries):
    """
    Query to load tents.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.tents

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return KnotMeta.get_attrs()
