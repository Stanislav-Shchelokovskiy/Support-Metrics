from datetime import date
from dateutil.relativedelta import relativedelta
from toolbox.utils.converters import DateTimeToSqlString
from toolbox.utils.env import recalculate_for_last_n_months


class Config:

    @staticmethod
    def get_tickets_period() -> dict[str, str]:
        end = date.today()
        start = end - offset_in_months()
        return {
            'start_date': DateTimeToSqlString.convert(start, separator='-'),
            'end_date': DateTimeToSqlString.convert(end, separator='-'),
        }

    @staticmethod
    def get_rank_period_offset() -> str:
        return '6 MONTHS'


def offset_in_months():
    months = recalculate_for_last_n_months()
    return relativedelta(day=1, months=months)
