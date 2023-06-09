import pytest
from pandas import DataFrame
from toolbox.sql.query_executors.sql_query_executor import SqlQueryExecutor
from toolbox.sql.generators import NULL_FILTER_VALUE
import repository.local.generators.filters_generators.display_filter as DisplayFilterGenerator
from sql_queries.index import CustomersActivityDBIndex
from sql_queries.meta import (
    TicketsTypesMeta,
    LicenseStatusesMeta,
    TribesMeta,
    PlatformsProductsMeta,
)

from server_models import (
    FilterParametersNode,
    FilterParameterNode,
    TicketsWithIterationsParams,
    Percentile,
)


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
            CustomersActivityDBIndex.get_tribes_name(): DataFrame(data={TribesMeta.name: ['XAML United Team']}),
            CustomersActivityDBIndex.get_tickets_types_name(): DataFrame(data={TicketsTypesMeta.name: ['Question']}),
            CustomersActivityDBIndex.get_license_statuses_name(): DataFrame(data={LicenseStatusesMeta.name: ['Licensed', 'Free']}),
            CustomersActivityDBIndex.get_platforms_products_name(): DataFrame(data={PlatformsProductsMeta.platform_name: []}),
        }[table_name]


@pytest.mark.parametrize(
    'node, output', [
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=40)),
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
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Ticket types': FilterParametersNode(include=True, values=[2]),
            }
            ),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Ticket types', 'in', ['Question']]
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Ticket types': FilterParametersNode(include=True, values=[2]),
                'Duplicated to ticket types': FilterParametersNode(include=True, values=[2]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Ticket types', 'in', ['Question']],
                'and',
                ['Duplicated to ticket types', 'in', ['Question']]
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Ticket types': FilterParametersNode(include=True, values=[2]),
                'Duplicated to ticket types': FilterParametersNode(include=False, values=[2]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Ticket types', 'in', ['Question']],
                'and',
                [
                    ['Duplicated to ticket types', '=', 'NULL'], 'or',
                    ['Duplicated to ticket types', 'notin', ['Question']]
                ]
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Ticket types': FilterParametersNode(include=False, values=[2]),
                'Duplicated to ticket types': FilterParametersNode(include=False, values=[2]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                [
                    ['Ticket types', '=', 'NULL'], 'or',
                    ['Ticket types', 'notin', ['Question']]
                ],
                'and',
                [
                    ['Duplicated to ticket types', '=', 'NULL'], 'or',
                    ['Duplicated to ticket types', 'notin', ['Question']]
                ]
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Ticket types': FilterParametersNode(include=False, values=[2, NULL_FILTER_VALUE]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                [
                    ['Ticket types', '!=', 'NULL'], 'and',
                    ['Ticket types', 'notin', ['Question']]
                ],
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Ticket types': FilterParametersNode(include=True, values=[2, NULL_FILTER_VALUE]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                [
                    ['Ticket types', '=', 'NULL'], 'or',
                    ['Ticket types', 'in', ['Question']]
                ],
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Platforms': FilterParametersNode(include=True, values=[NULL_FILTER_VALUE]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Platforms', '=', 'NULL'],
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Platforms': FilterParametersNode(include=False, values=[NULL_FILTER_VALUE]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Platforms', '!=', 'NULL'],
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Versions': FilterParametersNode(include=True, values=[NULL_FILTER_VALUE]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Versions', '=', 'NULL'],
            ]
        ),
        (
            TicketsWithIterationsParams(**{
                'Percentile': Percentile(metric='tickets', value=FilterParameterNode(include=True, value=100)),
                'Versions': FilterParametersNode(include=False, values=[NULL_FILTER_VALUE]),
            }),
            [
                ['Percentile', '<=', 100],
                'and',
                ['Versions', '!=', 'NULL'],
            ]
        )
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
        ) == output
