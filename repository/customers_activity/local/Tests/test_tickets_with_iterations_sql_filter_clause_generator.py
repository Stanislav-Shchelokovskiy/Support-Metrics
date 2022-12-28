import pytest
from repository.customers_activity.local.sql_query_params_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import (
    TicketsWithLicensesMeta,
    EmployeesIterationsMeta,
)


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
            f'AND ({TicketsWithLicensesMeta.user_groups} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithLicensesMeta.user_groups} LIKE '%p1%' OR {TicketsWithLicensesMeta.user_groups} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithLicensesMeta.user_groups} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithLicensesMeta.user_groups} IS NULL OR NOT ({TicketsWithLicensesMeta.user_groups} LIKE '%p1%' OR {TicketsWithLicensesMeta.user_groups} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithLicensesMeta.user_groups} IS NULL OR NOT ({TicketsWithLicensesMeta.user_groups} LIKE '%p1%'))"
        ),
    ]
)
def test_generate_customer_groups_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_customer_groups_filter(
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
            f'AND ({TicketsWithLicensesMeta.ticket_type} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithLicensesMeta.ticket_type} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithLicensesMeta.ticket_type} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithLicensesMeta.ticket_type} IS NULL OR {TicketsWithLicensesMeta.ticket_type} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithLicensesMeta.ticket_type} IS NULL OR {TicketsWithLicensesMeta.ticket_type} NOT IN (1))'
        ),
    ]
)
def test_generate_ticket_types_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_ticket_types_filter(
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
            f'AND ({TicketsWithLicensesMeta.ticket_tags} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f"AND ({TicketsWithLicensesMeta.ticket_tags} LIKE '%1%' OR {TicketsWithLicensesMeta.ticket_tags} LIKE '%2%')",
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f"AND ({TicketsWithLicensesMeta.ticket_tags} LIKE '%1%')",
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f"AND ({TicketsWithLicensesMeta.ticket_tags} IS NULL OR NOT ({TicketsWithLicensesMeta.ticket_tags} LIKE '%1%' OR {TicketsWithLicensesMeta.ticket_tags} LIKE '%2%'))",
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f"AND ({TicketsWithLicensesMeta.ticket_tags} IS NULL OR NOT ({TicketsWithLicensesMeta.ticket_tags} LIKE '%1%'))",
        ),
    ]
)
def test_generate_ticket_tags_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_ticket_tags_filter(
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
            f'AND ({TicketsWithLicensesMeta.tribe_id} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithLicensesMeta.tribe_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithLicensesMeta.tribe_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND ({TicketsWithLicensesMeta.tribe_id} IS NULL OR {TicketsWithLicensesMeta.tribe_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithLicensesMeta.tribe_id} IS NULL OR {TicketsWithLicensesMeta.tribe_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_tribes_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_tribes_filter(
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
            f'AND ({TicketsWithLicensesMeta.reply_id} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithLicensesMeta.reply_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithLicensesMeta.reply_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND ({TicketsWithLicensesMeta.reply_id} IS NULL OR {TicketsWithLicensesMeta.reply_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithLicensesMeta.reply_id} IS NULL OR {TicketsWithLicensesMeta.reply_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_reply_types_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_reply_types_filter(
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
            f'AND ({TicketsWithLicensesMeta.component_id} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithLicensesMeta.component_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithLicensesMeta.component_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND ({TicketsWithLicensesMeta.component_id} IS NULL OR {TicketsWithLicensesMeta.component_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithLicensesMeta.component_id} IS NULL OR {TicketsWithLicensesMeta.component_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_components_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_components_filter(
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
            f'AND ({TicketsWithLicensesMeta.feature_id} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"AND {TicketsWithLicensesMeta.feature_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithLicensesMeta.feature_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"AND ({TicketsWithLicensesMeta.feature_id} IS NULL OR {TicketsWithLicensesMeta.feature_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithLicensesMeta.feature_id} IS NULL OR {TicketsWithLicensesMeta.feature_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_features_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_features_filter(
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
            f'AND ({TicketsWithLicensesMeta.license_status} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithLicensesMeta.license_status} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithLicensesMeta.license_status} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithLicensesMeta.license_status} IS NULL OR {TicketsWithLicensesMeta.license_status} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithLicensesMeta.license_status} IS NULL OR {TicketsWithLicensesMeta.license_status} NOT IN (1))'
        ),
    ]
)
def test_generate_license_status_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_license_status_filter(
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
            f'AND ({TicketsWithLicensesMeta.conversion_status} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithLicensesMeta.conversion_status} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithLicensesMeta.conversion_status} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithLicensesMeta.conversion_status} IS NULL OR {TicketsWithLicensesMeta.conversion_status} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithLicensesMeta.conversion_status} IS NULL OR {TicketsWithLicensesMeta.conversion_status} NOT IN (1))'
        ),
    ]
)
def test_generate_conversion_status_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_conversion_status_filter(
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
            f'AND ({TicketsWithLicensesMeta.platforms} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithLicensesMeta.platforms} LIKE '%p1%' OR {TicketsWithLicensesMeta.platforms} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithLicensesMeta.platforms} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithLicensesMeta.platforms} IS NULL OR NOT ({TicketsWithLicensesMeta.platforms} LIKE '%p1%' OR {TicketsWithLicensesMeta.platforms} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithLicensesMeta.platforms} IS NULL OR NOT ({TicketsWithLicensesMeta.platforms} LIKE '%p1%'))"
        ),
    ]
)
def test_generate_platforms_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_platforms_filter(
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
            f'AND ({TicketsWithLicensesMeta.products} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithLicensesMeta.products} LIKE '%p1%' OR {TicketsWithLicensesMeta.products} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithLicensesMeta.products} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithLicensesMeta.products} IS NULL OR NOT ({TicketsWithLicensesMeta.products} LIKE '%p1%' OR {TicketsWithLicensesMeta.products} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithLicensesMeta.products} IS NULL OR NOT ({TicketsWithLicensesMeta.products} LIKE '%p1%'))"
        ),
    ]
)
def test_generate_products_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_products_filter(
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
            f'WHERE ({EmployeesIterationsMeta.pos_id} IS NULL)',
        ),
        (
            MockFilterParametersNode(include=True, values=[
                'qwe',
                'asd',
            ]),
            f"WHERE {EmployeesIterationsMeta.pos_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"WHERE {EmployeesIterationsMeta.pos_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=[
                'qwe',
                'asd',
            ]),
            f"WHERE ({EmployeesIterationsMeta.pos_id} IS NULL OR {EmployeesIterationsMeta.pos_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"WHERE ({EmployeesIterationsMeta.pos_id} IS NULL OR {EmployeesIterationsMeta.pos_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_positions_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_positions_filter(
        params=input
    ) == output
