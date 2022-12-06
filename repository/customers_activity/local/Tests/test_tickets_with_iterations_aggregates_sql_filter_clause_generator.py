import pytest
from repository.customers_activity.local.sql_query_params_generator import TicketsWithIterationsAggregatesSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        (
            ['p1', 'p2'],
            f"AND ({TicketsWithIterationsMeta.user_groups} LIKE '%p1%' OR {TicketsWithIterationsMeta.user_groups} LIKE '%p2%')"
        ),
        (['p1'], f"AND ({TicketsWithIterationsMeta.user_groups} LIKE '%p1%')"),
    ]
)
def test_generate_customer_groups_filter(input: list[str], output: str):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_customer_groups_filter(
        customer_groups=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        ([1, 2], f'AND {TicketsWithIterationsMeta.ticket_type} IN (1,2)'),
        ([1], f'AND {TicketsWithIterationsMeta.ticket_type} IN (1)'),
    ]
)
def test_generate_ticket_types_filter(input: list[int], output: str):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_ticket_types_filter(
        tickets_types=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        (
            [1, 2],
            f"AND ({TicketsWithIterationsMeta.ticket_tags} LIKE '%1%' OR {TicketsWithIterationsMeta.ticket_tags} LIKE '%2%')"
        ),
        ([1], f"AND ({TicketsWithIterationsMeta.ticket_tags} LIKE '%1%')"),
    ]
)
def test_generate_ticket_tags_filter(input: list[int], output: str):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_ticket_tags_filter(
        tickets_tags=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        (
            [
                'qwe',
                'asd',
            ],
            f"AND {TicketsWithIterationsMeta.tribe_id} IN ('qwe','asd')",
        ),
        (
            ['qwe'],
            f"AND {TicketsWithIterationsMeta.tribe_id} IN ('qwe')",
        ),
    ]
)
def test_generate_tribes_filter(input: list[str], output: str):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_tribes_filter(
        tribe_ids=input
    ) == output
