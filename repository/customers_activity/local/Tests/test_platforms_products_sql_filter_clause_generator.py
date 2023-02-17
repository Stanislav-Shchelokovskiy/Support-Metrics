import pytest
from repository.customers_activity.local.generators.filters_generators.platforms_products import PlatformsProductsSqlFilterClauseGenerator
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
            f"WHERE {PlatformsProductsMeta.platform_tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {PlatformsProductsMeta.platform_tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({PlatformsProductsMeta.platform_tribe_id} IS NULL OR {PlatformsProductsMeta.platform_tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {PlatformsProductsMeta.platform_tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({PlatformsProductsMeta.platform_tribe_id} IS NULL OR {PlatformsProductsMeta.platform_tribe_id} NOT IN ('t1','t2'))",
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
    'tribes, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {PlatformsProductsMeta.product_tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {PlatformsProductsMeta.product_tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({PlatformsProductsMeta.product_tribe_id} IS NULL OR {PlatformsProductsMeta.product_tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {PlatformsProductsMeta.product_tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({PlatformsProductsMeta.product_tribe_id} IS NULL OR {PlatformsProductsMeta.product_tribe_id} NOT IN ('t1','t2'))",
        ),
    ]
)
def test_generate_products_filter(
    tribes: MockFilterParametersNode,
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
        tribe_ids=tribes,
    ) == output
