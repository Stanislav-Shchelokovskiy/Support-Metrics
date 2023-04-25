from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    PlatformsMeta,
    ProductsMeta,
)
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import FilterParametersNode
import repository.customers_activity.local.generators.filters_generators.platforms_products as PlatformsProductsSqlFilterClauseGenerator


# yapf: disable
class Platforms(AsyncQueryDescriptor):
    """
    Query to a local table storing available platforms.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return PlatformsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        cols = ', '.join(self.get_fields(kwargs))
        filter = self.get_filter(tent_ids=kwargs['tent_ids'])
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_platforms_products_name(),
            'filter_group_limit_clause': f'{filter}\nGROUP BY {cols}\nORDER BY {self.get_order_by_column()}',
        }

    def get_filter(self, tent_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(tent_ids=tent_ids)

    def get_order_by_column(self) -> str:
        return PlatformsMeta.platform_name


class Products(Platforms):
    """
    Query to a local table storing products
    available for specified tribes.
    """
    def get_filter(self, tent_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(tent_ids=tent_ids)

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return ProductsMeta

    def get_order_by_column(self) -> str:
        return ProductsMeta.product_name
