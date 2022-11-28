import pytest
from repository.customers_activity.local.sql_query_params_generator import TicketsWithIterationsAggregatesSqlParamsGenerator
from sql_queries.customers_activity.meta import CustomersActivityMeta


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        (
            ['p1', 'p2'],
            f"AND ({CustomersActivityMeta.user_groups} LIKE '%p1%' OR {CustomersActivityMeta.user_groups} LIKE '%p2%')"
        ),
        (
            ['p1'],
            f"AND ({CustomersActivityMeta.user_groups} LIKE '%p1%')"
        ),
    ]
)
def test_generate_customer_groups_filter(input: list[str], output: str):
    assert TicketsWithIterationsAggregatesSqlParamsGenerator.generate_customer_groups_filter(
        customer_groups=input
    ) == output
