from pandas import DataFrame
from toolbox.sql.repository import SqlServerRepository
from sql_queries.customers_activity.meta import (
    TicketsTypesMeta,
    ConversionStatusesMeta,
)


class LicenseStatusesRepository(SqlServerRepository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                TicketsTypesMeta.id: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                TicketsTypesMeta.name:
                    [
                        'Licensed',
                        'Free',
                        'Expired',
                        'Revoked',
                        'Assigned to someone',
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


class ConversionStatusesRepository(SqlServerRepository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                ConversionStatusesMeta.license_status_id: [0, 1, 11, 11],
                ConversionStatusesMeta.id: [0, 1, 0, 1],
                ConversionStatusesMeta.name: [
                    'Paid',
                    'Free',
                    'Paid',
                    'Free',
                ]
            }
        )
