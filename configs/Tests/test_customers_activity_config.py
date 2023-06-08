from configs.config import Config
from datetime import date, datetime


def test_get_tickets_period():
    end = date.today()
    start = datetime(end.year - 5, 7, 1)
    assert Config.get_tickets_period() == {
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date': end.strftime('%Y-%m-%d'),
    }


def test_get_rank_period_offset():
    assert Config.get_rank_period_offset() == '6 MONTHS'
