from datetime import date
from dateutil.relativedelta import relativedelta
from toolbox.utils.converters import DateTimeToSqlString
from toolbox.utils.env import recalculate_for_last_n_days, recalculate_from_beginning


def get_tickets_period() -> dict[str, str]:
    end = _get_end()
    start = _get_start()
    return {
        'start_date': DateTimeToSqlString.convert(start, separator='-'),
        'end_date': DateTimeToSqlString.convert(end, separator='-'),
    }


def get_rank_period_offset() -> str:
    return '6 MONTHS'


def years_of_history():
    return '5 YEARS'


def _get_end():
    return date.today()


def _get_start():
    return _get_end() - _offset_in_days()


def _offset_in_days():
    days = recalculate_for_last_n_days()
    if recalculate_from_beginning():
        days = 365 * 5
    return relativedelta(days=days)
