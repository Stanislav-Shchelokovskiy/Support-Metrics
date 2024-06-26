from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
import sql_queries.meta.aggs as aggs
import sql_queries.index.path.remote as RemotePathIndex


class CSI(RepositoryAlchemyQueries):
    """
    Query to calculate CSI.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return RemotePathIndex.csi

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return aggs.CSI.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return aggs.CSI.get_values()
