import pytest
from repository.customers_activity.local.sql_query_params_generator import PlatformsProductsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import PlatformsProductsMeta


def test_generate_components_filter_raises_value_error():
    with pytest.raises(ValueError) as excInfo:
        PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
            tribe_ids=[]
        )
        assert 'tribe_ids cannot be empty' in str(excInfo)


@pytest.mark.parametrize(
    'input,output', [
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
def test_generate_components_filter(
    input: list[str],
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter(
        tribe_ids=input
    ) == output


@pytest.mark.parametrize(
    'tribes,platforms,output', [
        (
            ['t1'],
            ['p1'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1') AND {PlatformsProductsMeta.platform_id} IN ('p1')",
        ),
        (
            ['t1', 't2'],
            ['p1', 'p2'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND {PlatformsProductsMeta.platform_id} IN ('p1','p2')",
        ),
        (
            ['t1', 't2'],
            ['p1'],
            f"WHERE {PlatformsProductsMeta.tribe_id} IN ('t1','t2') AND {PlatformsProductsMeta.platform_id} IN ('p1')",
        ),
    ]
)
def test_generate_features_filter(
    tribes: list[str],
    platforms: list[str],
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
        tribe_ids=tribes,
        platform_ids=platforms,
    ) == output


def test_generate_features_filter_raises_value_error():
    with pytest.raises(ValueError) as excInfo:
        PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
            tribe_ids=['t1'],
            platform_ids=[],
        )
        assert 'platform_ids cannot be empty' in str(excInfo)
