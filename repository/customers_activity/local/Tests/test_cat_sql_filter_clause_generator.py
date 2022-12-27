import pytest
from repository.customers_activity.local.sql_query_params_generator.cat import CATSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import ComponentsFeaturesMeta


@pytest.mark.parametrize(
    'input,output', [
        (
            [],
            '',
        ),
        (
            ['t1'],
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1')",
        ),
        (
            ['t1', 't2'],
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2')",
        ),
    ]
)
def test_generate_components_filter(
    input: list[str],
    output: str,
):
    assert CATSqlFilterClauseGenerator.generate_components_filter(
        tribe_ids=input
    ) == output


@pytest.mark.parametrize(
    'tribes,components,output', [
        (
            [],
            [],
            '',
        ),
        (
            ['t1'],
            [],
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1')",
        ),
        (
            [],
            ['c1'],
            f"WHERE {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            ['t1'],
            ['c1'],
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1') AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            ['t1', 't2'],
            ['c1', 'c2'],
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND {ComponentsFeaturesMeta.component_id} IN ('c1','c2')",
        ),
        (
            ['t1', 't2'],
            ['c1'],
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
    ]
)
def test_generate_features_filter(
    tribes: list[str],
    components: list[str],
    output: str,
):
    assert CATSqlFilterClauseGenerator.generate_features_filter(
        tribe_ids=tribes,
        component_ids=components,
    ) == output
