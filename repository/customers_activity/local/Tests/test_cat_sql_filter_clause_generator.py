import pytest
from repository.customers_activity.local.filters_generators.cat import CATSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import ComponentsFeaturesMeta
from repository.customers_activity.local.Tests.mocks import MockFilterParametersNode


@pytest.mark.parametrize(
    'tribes, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2'))",
        ),
    ]
)
def test_generate_components_filter(
    tribes: list[str],
    output: str,
):
    assert CATSqlFilterClauseGenerator.generate_components_filter(
        tribe_ids=tribes
    ) == output


@pytest.mark.parametrize(
    'tribes, components, output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {ComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IS NULL AND {ComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1') AND {ComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1')) AND {ComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IS NULL AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IS NULL AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1') AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1')) AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1') AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1')) AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1', 'c2']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND {ComponentsFeaturesMeta.component_id} IN ('c1','c2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1', 'c2']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND {ComponentsFeaturesMeta.component_id} IN ('c1','c2')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1', 'c2']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1','c2'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1', 'c2']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1','c2'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND {ComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE {ComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE ({ComponentsFeaturesMeta.tribe_id} IS NULL OR {ComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND ({ComponentsFeaturesMeta.component_id} IS NULL OR {ComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
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
