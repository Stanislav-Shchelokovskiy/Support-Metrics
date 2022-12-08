import pytest
from repository.customers_activity.local.sql_query_params_generator import TicketsWithIterationsAggregatesSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta


class MockFilterParametersNode:

    def __init__(self, include: bool, values: list) -> None:
        self.include = include
        self.values = values


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.user_groups} LIKE '%p1%' OR {TicketsWithIterationsMeta.user_groups} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.user_groups} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.user_groups} NOT LIKE '%p1%' OR {TicketsWithIterationsMeta.user_groups} NOT LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.user_groups} NOT LIKE '%p1%')"
        ),
    ]
)
def test_generate_customer_groups_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_customer_groups_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithIterationsMeta.ticket_type} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithIterationsMeta.ticket_type} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND {TicketsWithIterationsMeta.ticket_type} NOT IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND {TicketsWithIterationsMeta.ticket_type} NOT IN (1)'
        ),
    ]
)
def test_generate_ticket_types_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_ticket_types_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f"AND ({TicketsWithIterationsMeta.ticket_tags} LIKE '%1%' OR {TicketsWithIterationsMeta.ticket_tags} LIKE '%2%')",
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f"AND ({TicketsWithIterationsMeta.ticket_tags} LIKE '%1%')",
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f"AND ({TicketsWithIterationsMeta.ticket_tags} NOT LIKE '%1%' OR {TicketsWithIterationsMeta.ticket_tags} NOT LIKE '%2%')",
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f"AND ({TicketsWithIterationsMeta.ticket_tags} NOT LIKE '%1%')",
        ),
    ]
)
def test_generate_ticket_tags_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_ticket_tags_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.tribe_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.tribe_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.tribe_id} NOT IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.tribe_id} NOT IN ('qwe')",
        ),
    ]
)
def test_generate_tribes_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_tribes_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.reply_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.reply_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.reply_id} NOT IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.reply_id} NOT IN ('qwe')",
        ),
    ]
)
def test_generate_reply_types_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_reply_types_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.control_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.control_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.control_id} NOT IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.control_id} NOT IN ('qwe')",
        ),
    ]
)
def test_generate_controls_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_controls_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.feature_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.feature_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithIterationsMeta.feature_id} NOT IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.feature_id} NOT IN ('qwe')",
        ),
    ]
)
def test_generate_features_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsAggregatesSqlFilterClauseGenerator.generate_features_filter(
        params=input
    ) == output
