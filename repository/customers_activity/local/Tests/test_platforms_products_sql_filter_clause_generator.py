import pytest
from repository.customers_activity.local.sql_query_params_generator import PlatformsProductsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import PlatformsProductsMeta


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        (
            ['t1'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1')",
        ),
        (
            ['t1', 't2'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2')",
        ),
    ]
)
def test_generate_platforms_filter(
    input: list[str],
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
        tribe_ids=input
    ) == output


@pytest.mark.parametrize(
    'tribes,platforms,output', [
        (
            [],
            [],
            f'WHERE {PlatformsProductsMeta.product_id} IS NOT NULL',
        ),
        (
            ['t1'],
            [],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            [],
            ['p1'],
            f"WHERE {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            ['t1'],
            ['p1'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            ['t1', 't2'],
            ['p1', 'p2'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND {PlatformsProductsMeta.platform_id} IN ('p1','p2') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
        (
            ['t1', 't2'],
            ['p1'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND {PlatformsProductsMeta.platform_id} IN ('p1') AND {PlatformsProductsMeta.product_id} IS NOT NULL",
        ),
    ]
)
def test_generate_products_filter(
    tribes: list[str],
    platforms: list[str],
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
        tribe_ids=tribes,
        platform_ids=platforms,
    ) == output
