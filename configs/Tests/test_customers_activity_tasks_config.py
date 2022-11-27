from configs.customers_activity_tasks_config import CustomersActivityTasksConfig
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def test_get_tickets_with_iterations_period():
    end = date.today() + relativedelta(day=1)
    start = datetime(end.year - 2, 1, 1)
    assert CustomersActivityTasksConfig.get_tickets_with_iterations_period() == {
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date': end.strftime('%Y-%m-%d'),
    }
