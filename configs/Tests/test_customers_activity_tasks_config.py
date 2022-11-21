from configs.customers_activity_tasks_config import CustomersActivityTasksConfig
from datetime import date
from dateutil.relativedelta import relativedelta


def test_get_future_working_hours_period():
    end = date.today() + relativedelta(day=1)
    start = end - relativedelta(months=24, day=1)
    assert CustomersActivityTasksConfig.get_tickets_with_iterations_period() == {
        'start_date': start.strftime('%Y%m%d'),
        'end_date': end.strftime('%Y%m%d'),
    }
