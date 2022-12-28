from pandas import DataFrame
from toolbox.sql.repository import Repository
from sql_queries.customers_activity.meta import (
    TicketsTypesMeta,
    ConversionStatusesMeta,
)


class LicenseStatusesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                TicketsTypesMeta.id: [0, 1, 2, 3, 4],
                TicketsTypesMeta.name:
                    [
                        'Licensed',
                        'Expired',
                        'Revoked',
                        'Free',
                        'Trial',
                    ]
            }
        )


class ConversionStatusesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                ConversionStatusesMeta.license_status_id: [0, 3, 4, 4],
                ConversionStatusesMeta.id: [5, 6, 5, 6],
                ConversionStatusesMeta.name: [
                    'Paid',
                    'Free',
                    'Paid',
                    'Free',
                ]
            }
        )
