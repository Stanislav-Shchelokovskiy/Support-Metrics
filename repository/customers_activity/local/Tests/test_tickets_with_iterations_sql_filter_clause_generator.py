import pytest
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta
from sql_queries.index import CustomersActivityDBIndex
from repository.customers_activity.local.Tests.mocks import (
    MockFilterParametersNode,
    MockFilterParameterNode,
    MockPercentile,
)
from configs.customers_activity_config import CustomersActivityConfig


@pytest.mark.parametrize(
    'kwargs, output', [
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
            },
            f"{TicketsWithIterationsMeta.creation_date} BETWEEN 'qwe' AND 'asd'",
        ),
    ]
)
def test_generate_creation_date_filter(
    kwargs: dict,
    output,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_creation_date_filter(
        **kwargs
    ) == output


@pytest.mark.parametrize(
    'kwargs, output', [
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
            },
            f"{TicketsWithIterationsMeta.creation_date} BETWEEN DATE('qwe', '-{CustomersActivityConfig.get_rank_period_offset()}') AND 'asd'",
        ),
    ]
)
def test_generate_creation_date_with_offset_start_filter(
    kwargs: dict,
    output,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_creation_date_with_offset_start_filter(
        **kwargs
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f'AND {TicketsWithIterationsMeta.user_groups} IS NULL',
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
            f"AND ({TicketsWithIterationsMeta.user_groups} IS NULL OR NOT ({TicketsWithIterationsMeta.user_groups} LIKE '%p1%' OR {TicketsWithIterationsMeta.user_groups} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.user_groups} IS NULL OR NOT ({TicketsWithIterationsMeta.user_groups} LIKE '%p1%'))"
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
    'ticket_types, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f'AND {TicketsWithIterationsMeta.ticket_type} IS NULL',
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
            f'AND ({TicketsWithIterationsMeta.ticket_type} IS NULL OR {TicketsWithIterationsMeta.ticket_type} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithIterationsMeta.ticket_type} IS NULL OR {TicketsWithIterationsMeta.ticket_type} NOT IN (1))'
        ),
    ]
)
def test_generate_ticket_types_filter(
    ticket_types: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_ticket_types_filter(
        params=ticket_types
    ) == output


@pytest.mark.parametrize(
    'ticket_types, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f'AND {TicketsWithIterationsMeta.referred_ticket_type} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithIterationsMeta.referred_ticket_type} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithIterationsMeta.referred_ticket_type} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithIterationsMeta.referred_ticket_type} IS NULL OR {TicketsWithIterationsMeta.referred_ticket_type} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithIterationsMeta.referred_ticket_type} IS NULL OR {TicketsWithIterationsMeta.referred_ticket_type} NOT IN (1))'
        ),
    ]
)
def test_generate_referred_ticket_types_filter(
    ticket_types: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_referred_ticket_types_filter(
        params=ticket_types
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f'AND {TicketsWithIterationsMeta.ticket_tags} IS NULL',
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
            f"AND ({TicketsWithIterationsMeta.ticket_tags} IS NULL OR NOT ({TicketsWithIterationsMeta.ticket_tags} LIKE '%1%' OR {TicketsWithIterationsMeta.ticket_tags} LIKE '%2%'))",
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f"AND ({TicketsWithIterationsMeta.ticket_tags} IS NULL OR NOT ({TicketsWithIterationsMeta.ticket_tags} LIKE '%1%'))",
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
            f'AND {TicketsWithIterationsMeta.tribe_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.tribe_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.tribe_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.tribe_id} IS NULL OR {TicketsWithIterationsMeta.tribe_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.tribe_id} IS NULL OR {TicketsWithIterationsMeta.tribe_id} NOT IN ('qwe'))",
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
            f'AND {TicketsWithIterationsMeta.reply_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.reply_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.reply_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.reply_id} IS NULL OR {TicketsWithIterationsMeta.reply_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.reply_id} IS NULL OR {TicketsWithIterationsMeta.reply_id} NOT IN ('qwe'))",
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
            f'AND {TicketsWithIterationsMeta.component_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.component_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.component_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.component_id} IS NULL OR {TicketsWithIterationsMeta.component_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.component_id} IS NULL OR {TicketsWithIterationsMeta.component_id} NOT IN ('qwe'))",
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
            f'AND {TicketsWithIterationsMeta.feature_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.feature_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.feature_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.feature_id} IS NULL OR {TicketsWithIterationsMeta.feature_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.feature_id} IS NULL OR {TicketsWithIterationsMeta.feature_id} NOT IN ('qwe'))",
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
            f'AND {TicketsWithIterationsMeta.license_status} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithIterationsMeta.license_status} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithIterationsMeta.license_status} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithIterationsMeta.license_status} IS NULL OR {TicketsWithIterationsMeta.license_status} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithIterationsMeta.license_status} IS NULL OR {TicketsWithIterationsMeta.license_status} NOT IN (1))'
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
            f'AND {TicketsWithIterationsMeta.conversion_status} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithIterationsMeta.conversion_status} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithIterationsMeta.conversion_status} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithIterationsMeta.conversion_status} IS NULL OR {TicketsWithIterationsMeta.conversion_status} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithIterationsMeta.conversion_status} IS NULL OR {TicketsWithIterationsMeta.conversion_status} NOT IN (1))'
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
            f'AND {TicketsWithIterationsMeta.platforms} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.platforms} LIKE '%p1%' OR {TicketsWithIterationsMeta.platforms} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.platforms} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.platforms} IS NULL OR NOT ({TicketsWithIterationsMeta.platforms} LIKE '%p1%' OR {TicketsWithIterationsMeta.platforms} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.platforms} IS NULL OR NOT ({TicketsWithIterationsMeta.platforms} LIKE '%p1%'))"
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
            f'AND {TicketsWithIterationsMeta.products} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.products} LIKE '%p1%' OR {TicketsWithIterationsMeta.products} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.products} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.products} IS NULL OR NOT ({TicketsWithIterationsMeta.products} LIKE '%p1%' OR {TicketsWithIterationsMeta.products} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.products} IS NULL OR NOT ({TicketsWithIterationsMeta.products} LIKE '%p1%'))"
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
            f'AND {TicketsWithIterationsMeta.emp_position_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.emp_position_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.emp_position_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.emp_position_id} IS NULL OR {TicketsWithIterationsMeta.emp_position_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.emp_position_id} IS NULL OR {TicketsWithIterationsMeta.emp_position_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_emp_positions_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_emp_positions_filter(
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
            f'AND {TicketsWithIterationsMeta.emp_tribe_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.emp_tribe_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.emp_tribe_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.emp_tribe_id} IS NULL OR {TicketsWithIterationsMeta.emp_tribe_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.emp_tribe_id} IS NULL OR {TicketsWithIterationsMeta.emp_tribe_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_emp_tribes_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_emp_tribes_filter(
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
            f'AND {TicketsWithIterationsMeta.emp_crmid} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.emp_crmid} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.emp_crmid} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.emp_crmid} IS NULL OR {TicketsWithIterationsMeta.emp_crmid} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.emp_crmid} IS NULL OR {TicketsWithIterationsMeta.emp_crmid} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_employees_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_employees_filter(
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
            f'AND {CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} IS NULL OR {CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} IS NULL OR {CustomersActivityDBIndex.get_tickets_with_iterations_name()}.{TicketsWithIterationsMeta.user_crmid} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_customers_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.generate_customers_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'alias, percentile, output', [
        (
            'alias',
            MockFilterParameterNode(include=True, value=100),
            'alias <= 100',
        ),
        (
            'alias',
            MockFilterParameterNode(include=False, value=100),
            'alias > 100',
        ),
        (
            'alias',
            MockFilterParameterNode(include=True, value=50),
            'alias <= 50',
        ),
        (
            'alias',
            MockFilterParameterNode(include=False, value=50),
            'alias > 50',
        ),
    ]
)
def test_get_percentile_filter(
    alias: str,
    percentile: MockPercentile,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.get_percentile_filter(
        alias=alias,
        percentile=percentile,
    ) == output
