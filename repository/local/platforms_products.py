from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from toolbox.sql.generators.filter_clause_generator_factory import FilterParametersNode
import repository.local.generators.filters_generators.platforms_products as PlatformsProductsSqlFilterClauseGenerator
import sql_queries.meta.platforms_products as platforms_products


# yapf: disable
class Platforms(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return platforms_products.Platforms

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        cols = ', '.join(self.get_fields(kwargs))
        filter = self.get_filter(tent_ids=kwargs['tent_ids'])
        return {
            'select': cols,
            'from': platforms_products.PlatformsProducts.get_name(),
            'where_group_limit': f'{filter}\nGROUP BY {cols}\nORDER BY {self.get_order_by_column()}',
        }

    def get_filter(self, tent_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(tent_ids=tent_ids)

    def get_order_by_column(self) -> str:
        return platforms_products.Platforms.platform_name


class Products(Platforms):
    def get_filter(self, tent_ids: FilterParametersNode) -> str:
        return PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(tent_ids=tent_ids)

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return platforms_products.Products

    def get_order_by_column(self) -> str:
        return platforms_products.Products.product_name
