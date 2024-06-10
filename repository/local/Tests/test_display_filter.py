import pytest
import toolbox.sql.generators.display_filter as DisplayFilterGenerator
from pandas import DataFrame
from toolbox.sql import KnotMeta
from toolbox.sql.query_executors.sql_query_executor import SqlQueryExecutor
from server_models import (
    FilterParametersNode,
    FilterParameterNode,
    TicketsWithIterationsParams,
    Percentile,
)
from repository.local.aggs import tickets as tickets_metric
from repository.local.generators.filters_generators.display_filter import custom_display_filter, DisplayValuesStore
import sql_queries.meta.tribes_tents as tribes_tents
import sql_queries.meta.tickets as tickets
import sql_queries.meta.customers as customers

class Connection:

    def begin_transaction(self):
        return None


class MockSqlQueryExecutor(SqlQueryExecutor):

    def __init__(self) -> None:
        super().__init__(Connection())

    # yapf: disable
    def execute(self, **kwargs):
        query = kwargs['main_query']
        table_name = query.format_params['from']
        return {
            tribes_tents.Tribes.get_name(): DataFrame(data={KnotMeta.name.name: ['XAML United Team']}),
            tickets.TicketsTypes.get_name(): DataFrame(data={KnotMeta.name.name: ['Question']}),
            customers.LicenseStatuses.get_name(): DataFrame(data={KnotMeta.name.name: ['Licensed', 'Free']}),
        }[table_name]


@pytest.mark.parametrize(
    'node, output', [
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric=tickets_metric.name, value=FilterParameterNode(include=True, value=40)),
                'Tribes': FilterParametersNode(include=True, values=['CE832BA0-1D68-421D-8DD5-5E2522462A2F']),
                'Ticket tags': FilterParametersNode(include=False, values=[],),
                'Ticket types': FilterParametersNode(include=False, values=[2]),
                'User types': FilterParametersNode(include=True, values=[0, 1],),
            }),
            [
                ['Percentile', '<=', 40],
                'and',
                ['Tribes', 'in', ['XAML United Team']],
                'and',
                ['Ticket tags', '=', 'NULL'],
                'and',
                [
                    ['Ticket types', '=', 'NULL'], 'or',
                    ['Ticket types', 'notin', ['Question']]
                ],
                'and',
                ['User types', 'in', ['Licensed', 'Free']]
            ],
        ),
        (TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric=tickets_metric.name, value=FilterParameterNode(include=False, value=40)),
                'Tribes': FilterParametersNode(include=True, values=['CE832BA0-1D68-421D-8DD5-5E2522462A2F']),
                'Ticket tags': FilterParametersNode(include=False, values=[],),
            }),
            [
                ['Percentile', '>', 40],
                'and',
                ['Tribes', 'in', ['XAML United Team']],
                'and',
                ['Ticket tags', '=', 'NULL'],
            ],
        ),
    ]
)
def test_generate_conversion_filter(
    node: TicketsWithIterationsParams,
    output: list[str | int],
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(DisplayFilterGenerator, '__query_executor', MockSqlQueryExecutor)
        assert DisplayFilterGenerator.__generate_display_filter(
            node=node,
            custom_display_filter=custom_display_filter,
            display_values_store=DisplayValuesStore,
        ) == output
