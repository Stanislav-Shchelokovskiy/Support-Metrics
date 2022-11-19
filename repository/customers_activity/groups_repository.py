from pandas import DataFrame
from toolbox.sql.base_repository import BaseRepository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.meta import CustomersGroupsMeta


class GroupsRepository(BaseRepository):
    """
    Loads groups we use to filter customers by.
    """

    def get_data(self, **kwargs) -> DataFrame:
        return BaseRepository.get_data(
            self,
            query_file_path=self.get_main_query_path(),
            query_format_params={
                **self.get_main_query_format_params(kwargs),
            },
        )

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_groups_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersGroupsMeta.get_attrs()
