import pytest
from pandas import DataFrame
from repository.customers_activity.local.generators.filters_generators.display_filter import DisplayFilterGenerator
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.Tests.mocks import (
    MockFilterParametersNode,
    MockFilterParameterNode,
    MockPercentile,
    MockFilterNode,
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
                DataFrame(data={LicenseStatusesMeta.name: ['Licensed', 'Free']}),
        }[table_name]


class TestFilterNode(MockFilterNode):

    def __init__(self, **kwargs) -> None:
        empty = MockFilterParametersNode(
            include=True,
            values=[],
        )
        self.percentile = kwargs.get('percentile', empty)
        self.tribe_ids = kwargs.get('tribe_ids', empty)
        self.platforms_ids = kwargs.get('platforms_ids', empty)
        self.products_ids = kwargs.get('products_ids', empty)
        self.tickets_tags = kwargs.get('tickets_tags', empty)
        self.tickets_types = kwargs.get('tickets_types', empty)
        self.customers_groups = kwargs.get('customers_groups', empty)
        self.license_statuses = kwargs.get('license_statuses', empty)
        self.conversion_statuses = kwargs.get('conversion_statuses', empty)
        self.positions_ids = kwargs.get('positions_ids', empty)
        self.emp_tribe_ids = kwargs.get('emp_tribe_ids', empty)
        self.emp_ids = kwargs.get('emp_ids', empty)
        self.reply_ids = kwargs.get('reply_ids', empty)
        self.components_ids = kwargs.get('components_ids', empty)
        self.feature_ids = kwargs.get('feature_ids', empty)
        self.customers_crmids = kwargs.get('customers_crmids', empty)

    def get_field_aliases(self) -> dict[str, str]:

        return {
            'percentile': 'Percentile',
            'tribe_ids': 'Tribes',
            'platforms_ids': 'Platforms',
            'products_ids': 'Products',
            'tickets_tags': 'Ticket tags',
            'customers_groups': 'User groups',
            'license_statuses': 'User types',
            'conversion_statuses': 'User conversion types',
            'positions_ids': 'Employees positions',
            'emp_tribe_ids': 'Employees tribes',
            'emp_ids': 'Employees',
            'reply_ids': 'CAT replies types',
            'components_ids': 'CAT components',
            'feature_ids': 'CAT features',
            'customers_crmids': 'Customers',
            'tickets_types': 'Ticket types',
        }


TestFilterNode(
    percentile=MockPercentile(
        metric='tickets',
        value=MockFilterParameterNode(include=True, value=40),
    ),
    tribe_ids=MockFilterParametersNode(
        include=True,
        values=['CE832BA0-1D68-421D-8DD5-5E2522462A2F'],
    ),
    tickets_tags=MockFilterParametersNode(
        include=False,
        values=[],
    ),
    license_statuses=MockFilterParametersNode(
        include=True,
        values=[0, 1],
    ),
    tickets_types=MockFilterParametersNode(
        include=False,
        values=[1],
    ),
)


# yapf: disable
@pytest.mark.parametrize(
    'node, output', [
        (
            TestFilterNode(
                percentile=MockPercentile(
                    metric='tickets',
                    value=MockFilterParameterNode(include=True, value=40),
                ),
                tribe_ids=MockFilterParametersNode(
                    include=True,
                    values=['CE832BA0-1D68-421D-8DD5-5E2522462A2F'],
                ),
                tickets_types=MockFilterParametersNode(
                    include=False,
                    values=[1],
                ),
                license_statuses=MockFilterParametersNode(
                    include=True,
                    values=[0, 1],
                ),
                tickets_tags=MockFilterParametersNode(
                    include=False,
                    values=[],
                )
            ),
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
    ]
)
def test_generate_conversion_filter(
    node: TestFilterNode,
    output: list[str | int],
):
    assert DisplayFilterGenerator.generate_display_filter(
        raw_values=node,
        repository=MockSqliteRepository(),
    ) == output
