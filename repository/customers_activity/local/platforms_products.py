from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import PlatformsProductsMeta
from repository.customers_activity.local.sql_query_params_generator.platforms_products import PlatformsProductsSqlFilterClauseGenerator


#yapf: disable
class PlatformsRepository(SqliteRepository):
    """
    Interface to a local table storing available platforms.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        cols = ', '.join(self.get_must_have_columns(kwargs))
        return {
            'columns': cols,
            'table_name': CustomersActivityDBIndex.get_platforms_products_name(),
            'filter_clause': PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
                    tribe_ids=kwargs['tribe_ids']
                ),
            'group_by_clause': f'GROUP BY {cols}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
            PlatformsProductsMeta.platform_id,
            PlatformsProductsMeta.platform_name,
        ]


class ProductsRepository(SqliteRepository):
    """
    Interface to a local table storing products
    available for specified platforms.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_platforms_products_name(),
            'filter_clause': PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
                    tribe_ids=kwargs['tribe_ids'],
                    platform_ids=kwargs['platform_ids'],
                ),
            'group_by_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [
                PlatformsProductsMeta.product_id,
                PlatformsProductsMeta.product_name,
        ]
