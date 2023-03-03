import pytest
from os import getcwd


def prepare_env(monkeypatch: pytest.MonkeyPatch):
    with open(getcwd() + '/.env', 'r') as env:
        for line in env:
            name, value = line.strip().split('=')
            monkeypatch.setenv(name, value)
    monkeypatch.setenv('SQLITE_DATABASE', f'{getcwd()}/Tests/test_db')
    monkeypatch.setenv('QUERY_SERVICE', 'localhost:11005')
    monkeypatch.setenv('customers_activity_start_date', '2022-01-01')
    monkeypatch.setenv('customers_activity_end_date', '2023-01-01')
