from pandas import DataFrame
from toolbox.sql import KnotMeta
from sql_queries.meta import ConversionStatusesMeta


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
                ConversionStatusesMeta.license_status_id.name: [0, 1, 11, 11],
                ConversionStatusesMeta.id.name: [0, 1, 0, 1],
                ConversionStatusesMeta.name.name:
                    [
                        'Paid',
                        'Free',
                        'Paid',
                        'Free',
                    ]
            }
        )
