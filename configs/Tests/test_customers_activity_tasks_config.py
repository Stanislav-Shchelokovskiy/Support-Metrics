from configs.customers_activity_tasks_config import CustomersActivityTasksConfig
from datetime import date, datetime


def test_get_tickets_with_iterations_period():
    end = date.today()
    start = datetime(end.year - 4, 1, 1)
    assert CustomersActivityTasksConfig.get_tickets_with_iterations_period() == {
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date': end.strftime('%Y-%m-%d'),
    }
