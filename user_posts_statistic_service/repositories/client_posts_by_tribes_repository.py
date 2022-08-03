import os
from pandas import DataFrame

from sql.base_repository import BaseRepository
from utils.param_metas import ClientPoststByTribesMetaData


class ClientPoststByTribesRepository(BaseRepository):

    def get_data(self, **kargs) -> DataFrame:
        return BaseRepository.get_data(
            self,
            query_file_path=os.environ['CLIENT_POSTS_SQL'],
            query_format_params=ClientPoststByTribesMetaData.get_attrs(),
            must_have_columns=ClientPoststByTribesMetaData.get_values(),
        )
