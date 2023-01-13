from datetime import date, datetime
from toolbox.utils.converters import DateTimeToSqlString


class CustomersActivityConfig:

    @staticmethod
    def get_tickets_with_licenses_period() -> dict[str, str]:
        end = date.today()
        start = datetime(end.year - 5, 7, 1)
        return {
            'start_date': DateTimeToSqlString.convert(start, separator='-'),
            'end_date': DateTimeToSqlString.convert(end, separator='-'),
        }

    @staticmethod
    def get_rank_period_offset() -> str:
        return '6 MONTHS'
