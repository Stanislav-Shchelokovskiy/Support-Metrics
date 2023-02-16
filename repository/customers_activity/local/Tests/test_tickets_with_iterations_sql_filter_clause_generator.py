import pytest
from repository.customers_activity.local.generators.filters_generators.tickets_with_iterations.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta, BaselineAlignedModeMeta
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
            f"WHERE {TicketsWithIterationsMeta.creation_date} BETWEEN 'qwe' AND 'asd'",
        ),
        (
            {
                'range_start': 'qwe',
                'range_end': 'asd',
                'filter_prefix': 'AND',
            },
            f"AND {TicketsWithIterationsMeta.creation_date} BETWEEN 'qwe' AND 'asd'",
        ),
    ]
)
def test_generate_creation_date_filter(
    kwargs: dict,
    output,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.common.generate_creation_date_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.common.generate_creation_date_with_rank_offset_start_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.customers.generate_customer_groups_filter(
        params=input
    ) == output


@pytest.mark.parametrize(
    'input, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f'AND {BaselineAlignedModeMeta.id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {BaselineAlignedModeMeta.id} IN ('qwe','asd')"
        ),
        (
            MockFilterParametersNode(include=True, values=['asd']),
            f"AND {BaselineAlignedModeMeta.id} IN ('asd')"
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({BaselineAlignedModeMeta.id} IS NULL OR {BaselineAlignedModeMeta.id} NOT IN ('qwe','asd'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({BaselineAlignedModeMeta.id} IS NULL OR {BaselineAlignedModeMeta.id} NOT IN ('qwe'))"
        ),
    ]
)
def test_generate_tracked_customer_groups_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.customers.generate_tracked_customer_groups_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets_types.generate_ticket_types_filter(
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
            f'AND {TicketsWithIterationsMeta.duplicated_to_ticket_type} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f'AND {TicketsWithIterationsMeta.duplicated_to_ticket_type} IN (1,2)'
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f'AND {TicketsWithIterationsMeta.duplicated_to_ticket_type} IN (1)'
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f'AND ({TicketsWithIterationsMeta.duplicated_to_ticket_type} IS NULL OR {TicketsWithIterationsMeta.duplicated_to_ticket_type} NOT IN (1,2))'
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f'AND ({TicketsWithIterationsMeta.duplicated_to_ticket_type} IS NULL OR {TicketsWithIterationsMeta.duplicated_to_ticket_type} NOT IN (1))'
        ),
    ]
)
def test_generate_duplicated_to_ticket_types_filter(
    ticket_types: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets_types.generate_duplicated_to_ticket_types_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_ticket_tags_filter(
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
            f'AND {TicketsWithIterationsMeta.tribes_ids} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"AND ({TicketsWithIterationsMeta.tribes_ids} LIKE '%t1%' OR {TicketsWithIterationsMeta.tribes_ids} LIKE '%t2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"AND ({TicketsWithIterationsMeta.tribes_ids} LIKE '%t1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"AND ({TicketsWithIterationsMeta.tribes_ids} IS NULL OR NOT ({TicketsWithIterationsMeta.tribes_ids} LIKE '%t1%' OR {TicketsWithIterationsMeta.tribes_ids} LIKE '%t2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"AND ({TicketsWithIterationsMeta.tribes_ids} IS NULL OR NOT ({TicketsWithIterationsMeta.tribes_ids} LIKE '%t1%'))"
        ),
    ]
)
def test_generate_tribes_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_tribes_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.cat.generate_reply_types_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.cat.generate_components_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.cat.generate_features_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.customers.generate_license_status_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.customers.generate_conversion_status_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.platforms_products.generate_platforms_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.platforms_products.generate_products_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.employees.generate_emp_positions_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.employees.generate_emp_tribes_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.employees.generate_employees_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.customers.generate_customers_filter(
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
    assert TicketsWithIterationsSqlFilterClauseGenerator.limit.get_percentile_filter(
        alias=alias,
        percentile=percentile,
    ) == output


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f'AND {TicketsWithIterationsMeta.builds} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.builds} LIKE '%p1%' OR {TicketsWithIterationsMeta.builds} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.builds} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.builds} IS NULL OR NOT ({TicketsWithIterationsMeta.builds} LIKE '%p1%' OR {TicketsWithIterationsMeta.builds} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.builds} IS NULL OR NOT ({TicketsWithIterationsMeta.builds} LIKE '%p1%'))"
        ),
    ]
)
def test_generate_builds_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_builds_filter(
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
            f'AND {TicketsWithIterationsMeta.severity} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.severity} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.severity} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.severity} IS NULL OR {TicketsWithIterationsMeta.severity} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.severity} IS NULL OR {TicketsWithIterationsMeta.severity} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_severity_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.bugs.generate_severity_filter(
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
            f'AND {TicketsWithIterationsMeta.ticket_status} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.ticket_status} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.ticket_status} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.ticket_status} IS NULL OR {TicketsWithIterationsMeta.ticket_status} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.ticket_status} IS NULL OR {TicketsWithIterationsMeta.ticket_status} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_ticket_status_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.bugs.generate_ticket_status_filter(
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
            f'AND {TicketsWithIterationsMeta.ide_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.ide_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.ide_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.ide_id} IS NULL OR {TicketsWithIterationsMeta.ide_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.ide_id} IS NULL OR {TicketsWithIterationsMeta.ide_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_ides_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_ides_filter(
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
            f'AND {TicketsWithIterationsMeta.operating_system_id} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe', 'asd']),
            f"AND {TicketsWithIterationsMeta.operating_system_id} IN ('qwe','asd')",
        ),
        (
            MockFilterParametersNode(include=True, values=['qwe']),
            f"AND {TicketsWithIterationsMeta.operating_system_id} IN ('qwe')",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe', 'asd']),
            f"AND ({TicketsWithIterationsMeta.operating_system_id} IS NULL OR {TicketsWithIterationsMeta.operating_system_id} NOT IN ('qwe','asd'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['qwe']),
            f"AND ({TicketsWithIterationsMeta.operating_system_id} IS NULL OR {TicketsWithIterationsMeta.operating_system_id} NOT IN ('qwe'))",
        ),
    ]
)
def test_generate_operating_systems_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_operating_systems_filter(
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
            f'AND {TicketsWithIterationsMeta.frameworks} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.frameworks} LIKE '%p1%' OR {TicketsWithIterationsMeta.frameworks} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.frameworks} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"AND ({TicketsWithIterationsMeta.frameworks} IS NULL OR NOT ({TicketsWithIterationsMeta.frameworks} LIKE '%p1%' OR {TicketsWithIterationsMeta.frameworks} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"AND ({TicketsWithIterationsMeta.frameworks} IS NULL OR NOT ({TicketsWithIterationsMeta.frameworks} LIKE '%p1%'))"
        ),
    ]
)
def test_generate_frameworks_filter(
    input: MockFilterParametersNode,
    output: str,
):
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_frameworks_filter(
        params=input
    ) == output


def test_generate_privacy_filter():
    assert TicketsWithIterationsSqlFilterClauseGenerator.tickets.generate_privacy_filter(
        params=MockFilterParameterNode(include=True, value=100),
    ) == f'AND {TicketsWithIterationsMeta.is_private} = 100'
