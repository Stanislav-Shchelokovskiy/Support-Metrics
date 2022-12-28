from datetime import date, datetime
from toolbox.utils.converters import DateTimeToSqlString


class CustomersActivityTasksConfig:

    @staticmethod
    def get_tickets_with_licenses_period() -> dict[str, str]:
        end = date.today()
        start = datetime(end.year - 4, 1, 1)
        return {
            'start_date': DateTimeToSqlString.convert(start, separator='-'),
            'end_date': DateTimeToSqlString.convert(end, separator='-'),
        }
