from typing import Iterable
from toolbox.sql.repository_queries import RepositoryQueries
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import PlatformsProductsMeta
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import FilterParametersNode
import repository.customers_activity.local.generators.filters_generators.platforms_products as PlatformsProductsSqlFilterClauseGenerator


# yapf: disable
class Platforms(RepositoryQueries):
    """
    Query to a local table storing available platforms.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        cols = ', '.join(self.get_must_have_columns(**kwargs))
        filter = self.get_filter(tribe_ids=kwargs['tribe_ids'])
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_platforms_products_name(),
            'filter_group_limit_clause': f'{filter}\nGROUP BY {cols}\nORDER BY {self.get_order_by_column()}',
        }

    def get_filter(self, tribe_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(tribe_ids=tribe_ids)

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return (
            PlatformsProductsMeta.platform_id,
            PlatformsProductsMeta.platform_name,
        )

    def get_order_by_column(self) -> str:
        return PlatformsProductsMeta.platform_name


class Products(Platforms):
    """
    Query to a local table storing products
    available for specified tribes.
    """
    def get_filter(self, tribe_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(tribe_ids=tribe_ids)

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return (
            PlatformsProductsMeta.product_id,
            PlatformsProductsMeta.product_name,
        )

    def get_order_by_column(self) -> str:
        return PlatformsProductsMeta.product_name
