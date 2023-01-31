import pytest
from pandas import DataFrame
from repository.customers_activity.local.generators.filters_generators.display_filter import DisplayFilterGenerator
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.Tests.mocks import (
    MockFilterParametersNode,
    MockFilterParameterNode,
    MockPercentile,
)
from sql_queries.customers_activity.meta import (
    TicketsTypesMeta,
    LicenseStatusesMeta,
    TribesMeta,
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
    'aliases, kwargs, output', [
        (
            {
                'percentile': 'Percentile',
                'tribe_ids': 'Tribes',
                'platforms_ids': 'Platforms',
                'tickets_types': 'Ticket types',
                'license_statuses': 'User types',
                'tickets_tags': 'Ticket tags',
            },
            {
                'percentile': MockPercentile(
                        metric='tickets',
                        value=MockFilterParameterNode(include=True, value=40)
                    ),
                'tribe_ids': MockFilterParametersNode(
                        include=True,
                        values=['CE832BA0-1D68-421D-8DD5-5E2522462A2F']
                    ),
                'platforms_ids': MockFilterParametersNode(include=True, values=[]),
                'tickets_types': MockFilterParametersNode(include=False, values=[1]),
                'license_statuses': MockFilterParametersNode(include=True, values=[0, 1]),
                'tickets_tags' : MockFilterParametersNode(include=False, values=[]),
            },
            [
                ['Percentile', '<=', 40],
                'and',
                ['Tribes', 'in', ['XAML United Team']],
                'and',
                [
                    ['Ticket types', '=', 'NULL'], 'or',
                    ['Ticket types', 'notin', ['Question']]
                ],
                'and',
                ['User types', 'in', ['Licensed', 'Free']],
                'and',
                ['Ticket tags', '=', 'NULL']
            ],
        ),
    ]
)
def test_generate_conversion_filter(
    aliases: dict[str],
    kwargs: dict,
    output: list[str | int],
):
    assert DisplayFilterGenerator.generate_display_filter(
        aliases=aliases,
        repository=MockSqliteRepository(),
        **kwargs,
    ) == output
