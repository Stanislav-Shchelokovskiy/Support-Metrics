import pytest
import os
from pathlib import Path
from Tests.env import prepare_env
import tasks.customers_activity_tasks as customers_activity


def pytest_configure(config: pytest.Config):
    if 'e2e' in config.invocation_params.args:
        build_test_db()


def build_test_db():
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        if Path(os.environ['SQLITE_DATABASE']).exists():
            return
        start_date = os.environ['customers_activity_start_date']
        end_date = os.environ['customers_activity_end_date']
        customers_activity.load_tribes()
        customers_activity.load_tickets_types()
        customers_activity.load_license_statuses()
        customers_activity.load_conversion_statuses()
        customers_activity.load_tags()
        customers_activity.load_groups()
        customers_activity.load_tracked_groups(
            start_date=start_date,
            end_date=end_date,
        )
        customers_activity.load_replies_types()
        customers_activity.load_components_features()
        customers_activity.load_platforms_products()
        customers_activity.load_customers_tickets(
            start_date=start_date,
            end_date=end_date,
        )
        customers_activity.load_employees_iterations(
            start_date=start_date,
            end_date=end_date,
        )
        customers_activity.process_staged_data(rank_period_offset='6 MONTHS')
