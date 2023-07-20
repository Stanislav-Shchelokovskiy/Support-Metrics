from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.meta import (
    LicenseStatusesMeta,
    ConversionStatusesMeta,
)
import repository.local.generators.filters_generators.conversion_statuses as ConversionStatusesSqlFilterClauseGenerator
import sql_queries.index.db as DbIndex


# yapf: disable
class LicenseStatuses(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return LicenseStatusesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.license_statuses,
            'where_group_limit': '',
        }


class ConversionStatuses(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return ConversionStatusesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.conversion_statuses,
            'where_group_limit': ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter(
                    license_status_ids=kwargs['license_status_ids']
                ),
        }
