from toolbox.sql.repository import SqliteRepository
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    LicenseStatusesMeta,
    ConversionStatusesMeta,
)
from repository.customers_activity.local.sql_query_params_generator.conversion_statuses import ConversionStatusesSqlFilterClauseGenerator


#yapf: disable
class LicenseStatusesRepository(SqliteRepository):
    """
    Interface to a local table storing license statuses.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_license_statuses_name(),
            'filter_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return LicenseStatusesMeta.get_values()


class ConversionStatusesRepository(SqliteRepository):
    """
    Interface to a local table storing conversion statuses.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'DISTINCT': '',
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_conversion_statuses_name(),
            'filter_clause': ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter(
                    license_status_ids=kwargs['license_status_ids']
                ),
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ConversionStatusesMeta.get_values()
