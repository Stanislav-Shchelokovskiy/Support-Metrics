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

    import tasks.employees as employees
    import tasks.tasks as tasks
    start_date = os.environ['start_date']
    end_date = os.environ['end_date']
    emps_json = employees.get_employees(start_date)
    tasks.load_tickets_types()
    tasks.load_license_statuses()
    tasks.load_conversion_statuses()
    tasks.load_tribes()
    tasks.load_tents()
    tasks.load_employees(start_date=start_date, employees_json=emps_json)
    tasks.load_roles(employees_json=emps_json)
    tasks.load_operating_systems()
    tasks.load_frameworks(),
    tasks.load_severity()
    tasks.load_ticket_statuses()
    tasks.load_replies_types()
    tasks.load_platforms_products()
    tasks.load_ides()
    tasks.load_tags()
    tasks.load_groups()
    tasks.load_tracked_groups(
        start_date=start_date,
        end_date=end_date,
    )
    tasks.load_builds()
    tasks.load_components_features()
    tasks.load_tickets(
        start_date=start_date,
        end_date=end_date,
    )
    tasks.load_employees_iterations(
        start_date=start_date,
        end_date=end_date,
        employees_json=emps_json,
    )
    tasks.load_csi()
    tasks.load_resolution_time(years_of_history='YEAR, -2', employees_json=emps_json)
    tasks.process_staged_data(rank_period_offset='6 MONTHS', years_of_history='2 YEARS')
