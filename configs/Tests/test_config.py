import pytest
from configs.config import Config
from datetime import date
from dateutil.relativedelta import relativedelta


def test_get_tickets_period():
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setenv('RECALCULATE_FOR_LAST_MONTHS', 36)
        end = date.today()
        start = end - relativedelta(day=1, months=36)
        assert Config.get_tickets_period() == {
            'start_date': start.strftime('%Y-%m-%d'),
            'end_date': end.strftime('%Y-%m-%d'),
        }


def test_get_rank_period_offset():
    assert Config.get_rank_period_offset() == '6 MONTHS'
