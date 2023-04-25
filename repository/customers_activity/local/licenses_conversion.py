from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import MetaData
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
class LicenseStatuses(AsyncQueryDescriptor):
    """
    Query to a local table storing license statuses.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return LicenseStatusesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_license_statuses_name(),
            'filter_group_limit_clause': '',
        }




class ConversionStatuses(AsyncQueryDescriptor):
    """
    Query to a local table storing conversion statuses.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return ConversionStatusesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_conversion_statuses_name(),
            'filter_group_limit_clause': ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter(
                    license_status_ids=kwargs['license_status_ids']
                ),
        }
