from typing import Iterable
from toolbox.sql.repository_queries import RepositoryAlchemyQueries
from sql_queries.meta import CSIMeta
import sql_queries.index.path.extract as ExtractPathIndex


class CSI(RepositoryAlchemyQueries):
    """
    Query to calculate CSI.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return ExtractPathIndex.csi

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return CSIMeta.get_attrs()

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return CSIMeta.get_values()
