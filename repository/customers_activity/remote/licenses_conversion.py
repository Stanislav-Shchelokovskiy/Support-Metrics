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
                TicketsTypesMeta.id: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                TicketsTypesMeta.name:
                    [
                        'Licensed',
                        'Free',
                        'Expired',
                        'Revoked',
                        'No license, Licensed',
                        'No license, Licensed, Revoked',
                        'No license, Expired',
                        'No license, Expired, Revoked',
                        'No license, Free',
                        'No license, Free, Expired',
                        'Trial',
                    ]
            }
        )


class ConversionStatusesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                ConversionStatusesMeta.license_status_id: [0, 1, 10, 10],
                ConversionStatusesMeta.id: [11, 12, 11, 12],
                ConversionStatusesMeta.name: [
                    'Paid',
                    'Free',
                    'Paid',
                    'Free',
                ]
            }
        )
