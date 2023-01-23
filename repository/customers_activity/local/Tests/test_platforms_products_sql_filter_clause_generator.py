import pytest
from repository.customers_activity.local.filters_generators.platforms_products import PlatformsProductsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import PlatformsProductsMeta
from repository.customers_activity.local.Tests.mocks import MockFilterParametersNode


@pytest.mark.parametrize(
    'tribes, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {PlatformsProductsMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1','t2'))",
        ),
    ]
)
def test_generate_platforms_filter(
    tribes: MockFilterParametersNode,
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
        tribe_ids=tribes
    ) == output


@pytest.mark.parametrize(
    'tribes,platforms,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            f'WHERE {PlatformsProductsMeta.product_id} IS NOT NULL',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            f'WHERE {PlatformsProductsMeta.tribe_id} IS NULL AND {PlatformsProductsMeta.product_id} IS NOT NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f'WHERE {PlatformsProductsMeta.platform_id} IS NULL AND {PlatformsProductsMeta.product_id} IS NOT NULL',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f'WHERE {PlatformsProductsMeta.tribe_id} IS NULL AND {PlatformsProductsMeta.platform_id} IS NULL AND {PlatformsProductsMeta.product_id} IS NOT NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND {PlatformsProductsMeta.platform_id} IS NULL AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1')) AND {PlatformsProductsMeta.platform_id} IS NULL AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IS NULL AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IS NULL AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1')) AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1')) AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND {PlatformsProductsMeta.platform_id} IN ('p1','p2') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1','t2')) AND {PlatformsProductsMeta.platform_id} IN ('p1','p2') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1','p2')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1','t2')) AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1','p2')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1','t2')) AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE ({PlatformsProductsMeta.tribe_id} IS NULL OR {PlatformsProductsMeta.tribe_id} NOT IN ('t1','t2')) AND ({PlatformsProductsMeta.platform_id} IS NULL OR {PlatformsProductsMeta.platform_id} NOT IN ('p1')) AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
    ]
)
def test_generate_products_filter(
    tribes: MockFilterParametersNode,
    platforms: MockFilterParametersNode,
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
        tribe_ids=tribes,
        platform_ids=platforms,
    ) == output
