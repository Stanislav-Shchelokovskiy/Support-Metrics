import os
from pandas import DataFrame

from sql.base_repository import BaseRepository
from utils.param_metas import UserPoststByTribesMetaData


class UserPoststByTribesRepository(BaseRepository):

    def get_data(self, **kargs) -> DataFrame:
        return BaseRepository.get_data(
            self,
            query_file_path=os.environ['USER_POSTS_SQL'],
            query_format_params=UserPoststByTribesMetaData.get_attrs(),
            must_have_columns=UserPoststByTribesMetaData.get_values(),
        )
