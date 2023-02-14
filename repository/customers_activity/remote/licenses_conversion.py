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
                TicketsTypesMeta.id: [0, 1, 2, 3, 4, 5, 6, 7, 8],
                TicketsTypesMeta.name:
                    [
                        'Licensed',
                        'Free',
                        'Expired',
                        'Revoked',
                        'No license, Licensed',
                        'No license, Expired',
                        'No license, Free',
                        'No license, Expired Free',
                        'Trial',
                    ]
            }
        )


class ConversionStatusesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                ConversionStatusesMeta.license_status_id: [0, 1, 8, 8],
                ConversionStatusesMeta.id: [9, 10, 9, 10],
                ConversionStatusesMeta.name: [
                    'Paid',
                    'Free',
                    'Paid',
                    'Free',
                ]
            }
        )
