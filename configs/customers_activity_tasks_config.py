from datetime import date
from dateutil.relativedelta import relativedelta
from toolbox.utils.converters import DateTimeToSqlString


class CustomersActivityTasksConfig:

    @staticmethod
    def get_tickets_with_iterations_period() -> dict[str, str]:
        end = date.today() + relativedelta(day=1)
        start = end - relativedelta(months=36, day=1)
        return {
            'start_date': DateTimeToSqlString.convert(start),
            'end_date': DateTimeToSqlString.convert(end),
        }
