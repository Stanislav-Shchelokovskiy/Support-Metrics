import pytest
from pandas import DataFrame
from repository.customers_activity.local.generators.filters_generators.display_filter import DisplayFilterGenerator
from sql_queries.index import CustomersActivityDBIndex
from sql_queries.customers_activity.meta import (
    TicketsTypesMeta,
    LicenseStatusesMeta,
    TribesMeta,
)

from server_models import (
    FilterParametersNode,
    FilterParameterNode,
    TicketsWithIterationsParams,
    Percentile,
)


class MockSqliteRepository:

    def execute_query(self, **kwargs):
        table_name = kwargs['query_format_params']['table_name']
        return {
            CustomersActivityDBIndex.get_tribes_name():
                DataFrame(data={TribesMeta.name: ['XAML United Team']}),
            CustomersActivityDBIndex.get_tickets_types_name():
                DataFrame(data={TicketsTypesMeta.name: ['Question']}),
            CustomersActivityDBIndex.get_license_statuses_name():
                DataFrame(
                    data={LicenseStatusesMeta.name: ['Licensed', 'Free']}
                ),
        }[table_name]


# yapf: disable
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
        )
    ]
)
def test_generate_conversion_filter(
    node: TicketsWithIterationsParams,
    output: list[str | int],
):
    assert DisplayFilterGenerator.generate_display_filter(
        node=node,
        repository=MockSqliteRepository(),
    ) == output
