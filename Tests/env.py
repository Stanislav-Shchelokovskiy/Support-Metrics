import pytest
from os import getcwd
from wrapt import decorator
from collections.abc import Callable, Iterable


def __prepare_env(monkeypatch: pytest.MonkeyPatch):
    with open(getcwd() + '/.env', 'r') as env:
        for line in env:
            line = line.strip()
            if line[0] == '#':
                continue
            name, value = line.split('=')
            monkeypatch.setenv(name, value)
    monkeypatch.setenv('SQLITE_DATABASE', f'{getcwd()}/Tests/test_db')
    monkeypatch.setenv('QUERY_SERVICE', 'localhost:11005')
    monkeypatch.setenv('start_date', '2022-01-01')
    monkeypatch.setenv('end_date', '2023-01-01')


@decorator
def with_env(
    callable: Callable[..., None],
    instance,
    args: Iterable,
    kwargs: dict,
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        __prepare_env(monkeypatch)
        return callable(**kwargs)
