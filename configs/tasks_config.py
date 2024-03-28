import os
from datetime import date
from dateutil.relativedelta import relativedelta
from toolbox.utils.converters import DateTimeToSqlString
from toolbox.tasks_config import (
    recalculate_for_last_n_days,
    recalculate_from_beginning,
    recalculate_for_last_n_days_long,
)


SQLITE = 'sqlite'
TSQL = 'tsql'
LONG_PERIOD = 'long_period'
SHORT_PERIOD = 'short_period'


def get_tickets_period(period: str) -> dict[str, str]:
    end = _get_end()
    start = _get_start(period=period)
    return {
        'start_date': DateTimeToSqlString.convert(start, separator='-'),
        'end_date': DateTimeToSqlString.convert(end, separator='-'),
    }


def get_emp_start() -> str:
    return DateTimeToSqlString.convert(_get_start(for_emps=True), separator='-')


def get_rank_period_offset() -> str:
    return '6 MONTHS'


def years_of_history(format: str):
    return {
        SQLITE: '5 YEARS',
        TSQL: 'YEAR, -5',
    }[format]


def _get_end():
    return date.today()


def _get_start(period: str = SHORT_PERIOD, for_emps: bool = False):
    return _get_end() - _offset_in_days(period, for_emps)


def _offset_in_days(period: str, for_emps: bool):
    days = recalculate_for_last_n_days()
    if recalculate_from_beginning() or for_emps:
        days = 365 * 5
    elif period == LONG_PERIOD:
        days = recalculate_for_last_n_days_long()

    return relativedelta(days=days)

def update_on_startup()-> int:
    return int(os.environ['UPDATE_ON_STARTUP'])
