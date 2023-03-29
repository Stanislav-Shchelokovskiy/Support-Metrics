from typing import Iterable
from toolbox.sql.repository_queries import RepositoryQueries
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    LicenseStatusesMeta,
    ConversionStatusesMeta,
)
import repository.customers_activity.local.generators.filters_generators.conversion_statuses as ConversionStatusesSqlFilterClauseGenerator


# yapf: disable
class LicenseStatuses(RepositoryQueries):
    """
    Query to a local table storing license statuses.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_license_statuses_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return LicenseStatusesMeta.get_values()


class ConversionStatuses(RepositoryQueries):
    """
    Query to a local table storing conversion statuses.
    """

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_conversion_statuses_name(),
            'filter_group_limit_clause': ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter(
                    license_status_ids=kwargs['license_status_ids']
                ),
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return ConversionStatusesMeta.get_values()
