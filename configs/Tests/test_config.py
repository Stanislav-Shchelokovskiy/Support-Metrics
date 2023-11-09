import pytest
import configs.config as config
from datetime import date
from dateutil.relativedelta import relativedelta


five_years_in_days = 365 * 5


@pytest.mark.parametrize(
    'envs, delta',
    (
        (
            (
                ('RECALCULATE_FOR_LAST_DAYS', 36),
                ('RECALCULATE_FROM_THE_BEGINNING', 0)
            ),
            36,
        ),
        (
            (
                ('RECALCULATE_FOR_LAST_DAYS', 36),
                ('RECALCULATE_FROM_THE_BEGINNING', 1)
            ),
            five_years_in_days,
        ),
    ),
)
def test_get_tickets_period(envs, delta):
    with pytest.MonkeyPatch.context() as monkeypatch:
        for env in envs:
            monkeypatch.setenv(*env)
        end = date.today()
        start = end - relativedelta(days=delta)
        assert config.get_tickets_period() == {
            'start_date': start.strftime('%Y-%m-%d'),
            'end_date': end.strftime('%Y-%m-%d'),
        }


def test_get_rank_period_offset():
    assert config.get_rank_period_offset() == '6 MONTHS'


def test_years_of_history():
    assert config.years_of_history(config.SQLITE) == '5 YEARS'
    assert config.years_of_history(config.TSQL) == 'YEAR, -5'


def test_get_emp_start():
    assert config.get_emp_start() == (date.today() - relativedelta(days=five_years_in_days)).strftime('%Y-%m-%d')
