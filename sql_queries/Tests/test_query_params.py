import pytest
from typing import Callable
from os import getcwd
from toolbox.sql.index import RootPath
from sql_queries.index import (
    CustomersActivityIndex,
)
from toolbox.sql.sql_query import SqlQuery
from sql_queries.meta import (
    CustomersActivityMeta,
    CustomersGroupsMeta,
    CustomersTagsMeta,
)


@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            CustomersActivityIndex.get_tickets_with_iterations_path,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
                **CustomersActivityMeta.get_attrs(),
            },
        ),
        (
            CustomersActivityIndex.get_groups_path,
            {
                **CustomersGroupsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivityIndex.get_tags_path, {
                **CustomersTagsMeta.get_attrs(),
            }
        ),
    ],
)
def test_query_params(
    get_query_file_path: Callable[[], str],
    format_params: dict,
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        SqlQuery(
            query_file_path=get_query_file_path(),
            format_params=format_params,
        ).get_query()


def prepare_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        target=RootPath,
        name='get_cwd',
        value=lambda: getcwd() + '/sql_queries',
    )
