import pytest
from typing import Callable
from os import getcwd
from toolbox.sql.index import RootPath
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
)
from toolbox.sql.sql_query import SqlQuery
from sql_queries.customers_activity.meta import (
    TicketsWithIterationsMeta,
    CustomersGroupsMeta,
    TicketsTagsMeta,
    TicketsWithIterationsPeriodMeta,
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
    TicketsWithIterationsAggregatesMeta,
    TicketsWithIterationsRawMeta,
)


tickets_with_iterations_common_params = {
    'table_name': 'table_name',
    'range_start': 'range_start',
    'range_end': 'range_end',
    'tribes_fitler': 'tribes_fitler',
    'customer_groups_filter': 'customer_groups_filter',
    'ticket_types_filter': 'ticket_types_filter',
    'ticket_tags_filter': 'ticket_tags_filter',
    'reply_types_filter': 'reply_types_filter',
    'components_filter': 'components_filter',
    'features_filter': 'features_filter',
    'license_status_filter': 'license_status_filter',
    'conversion_status_filter': 'conversion_status_filter',
}


@pytest.mark.parametrize(
    'get_query_file_path, format_params',
    [
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_path,
            {
                **TicketsWithIterationsMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path,
            {
                **TicketsWithIterationsRawMeta.get_attrs(),
                **tickets_with_iterations_common_params,
                'components_features_table':'components_features_table',
                'replies_types_table':'replies_types_table',
                'license_statuses_table':'license_statuses_table',
                'conversion_statuses_table':'conversion_statuses_table',
            },
        ),
        (
            CustomersActivitySqlPathIndex.
            get_tickets_with_iterations_aggregates_path,
            {
                **TicketsWithIterationsAggregatesMeta.get_attrs(),
                **tickets_with_iterations_common_params,
                'group_by_period':'group_by_period',
            },
        ),
        (
            CustomersActivitySqlPathIndex.
            get_fill_tickets_with_iterations_path,
            {
                'start_date': 'qwe',
                'end_date': 'asd',
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
            CustomersActivitySqlPathIndex.get_replies_types_path,
            {
                **ReplyTypesMeta.get_attrs(),
            },
        ),
        (
            CustomersActivitySqlPathIndex.get_components_features_path,
            {
                **ComponentsFeaturesMeta.get_attrs(),
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
            CustomersActivitySqlPathIndex.get_general_select_path,
            {
                'columns': 'qwe, asd',
                'table_name': 'test',
                'filter_clause': '',
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
