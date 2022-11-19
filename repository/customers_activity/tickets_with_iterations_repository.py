from pandas import DataFrame
from toolbox.sql.base_repository import BaseRepository
from sql_queries.index import CustomersActivityIndex
from sql_queries.meta import CustomersActivityMeta


class TicketsWithIterationsRepository(BaseRepository):
    """
    Loads customers with their tickets and iterations.
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
        return CustomersActivityIndex.get_tickets_with_iterations_path

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersActivityMeta.get_attrs()
