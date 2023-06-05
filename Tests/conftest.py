import pytest
import os
from pathlib import Path
from Tests.env import with_env
from fastapi.testclient import TestClient


client = None


@with_env
def create_client():
    global client
    from server import app
    client = TestClient(app=app)


@pytest.fixture
def test_client() -> TestClient:
    if not client:
        create_client()
    return client


def pytest_configure(config: pytest.Config):
    if 'e2e' in config.invocation_params.args:
        build_test_db()


@with_env
def build_test_db():
    if Path(os.environ['SQLITE_DATABASE']).exists():
        return

    import tasks.customers_activity_tasks as customers_activity
    start_date = os.environ['customers_activity_start_date']
    end_date = os.environ['customers_activity_end_date']
    customers_activity.load_tickets_types()
    customers_activity.load_license_statuses()
    customers_activity.load_conversion_statuses()
    customers_activity.load_tribes()
    customers_activity.load_tents()
    customers_activity.load_employees(start_date=start_date, )
    customers_activity.load_operating_systems()
    customers_activity.load_frameworks(),
    customers_activity.load_severity_values()
    customers_activity.load_ticket_statuses()
    customers_activity.load_replies_types()
    customers_activity.load_platforms_products()
    customers_activity.load_ides()
    customers_activity.load_tags()
    customers_activity.load_groups()
    customers_activity.load_tracked_groups(
        start_date=start_date,
        end_date=end_date,
    )
    customers_activity.load_builds()
    customers_activity.load_components_features()
    customers_activity.load_customers_tickets(
        start_date=start_date,
        end_date=end_date,
    )
    customers_activity.load_employees_iterations(
        start_date=start_date,
        end_date=end_date,
    )
    customers_activity.process_staged_data(rank_period_offset='6 MONTHS')
