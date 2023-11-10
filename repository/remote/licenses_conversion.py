from pandas import DataFrame
from toolbox.sql import KnotMeta
import sql_queries.meta.customers as customers


class LicenseStatusesRepository:

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                KnotMeta.id.name: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                KnotMeta.name.name:
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


class ConversionStatusesRepository:

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                customers.ConversionStatuses.license_status_id.name: [0, 1, 11, 11],
                customers.ConversionStatuses.id.name: [0, 1, 0, 1],
                customers.ConversionStatuses.name.name:
                    [
                        'Paid',
                        'Free',
                        'Paid',
                        'Free',
                    ]
            }
        )
