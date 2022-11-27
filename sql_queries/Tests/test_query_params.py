import pytest
from typing import Callable
from os import getcwd
from toolbox.sql.index import RootPath
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
)
from toolbox.sql.sql_query import SqlQuery
from sql_queries.customers_activity.meta import (
    CustomersActivityMeta,
    CustomersGroupsMeta,
    TicketsTagsMeta,
    TicketsWithIterationsPeriodMeta,
)


@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_path,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
                **CustomersActivityMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_customers_groups_path,
            {
                **CustomersGroupsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tags_path,
            {
                **TicketsTagsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.
            get_tickets_with_iterations_period_path,
            {
                'table_name': 'test',
                **TicketsWithIterationsPeriodMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_select_all_path,
            {
                'table_name': 'test',
                'columns': 'qwe, asd',
            },
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
