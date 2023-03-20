import pytest
import repository.customers_activity.local.generators.filters_generators.cat as CATSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import CATComponentsFeaturesMeta
from repository.customers_activity.local.Tests.mocks import MockFilterParametersNode


@pytest.mark.parametrize(
    'tribes, output', [
        (
            None,
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2'))",
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
            None,
            None,
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            None,
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {CATComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IS NULL AND {CATComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1') AND {CATComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1')) AND {CATComponentsFeaturesMeta.component_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IS NULL AND {CATComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IS NULL AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1') AND {CATComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1')) AND {CATComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1') AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1')) AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1', 'c2']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND {CATComponentsFeaturesMeta.component_id} IN ('c1','c2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1', 'c2']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND {CATComponentsFeaturesMeta.component_id} IN ('c1','c2')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1', 'c2']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1','c2'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1', 'c2']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1','c2'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND {CATComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=True, values=['c1']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND {CATComponentsFeaturesMeta.component_id} IN ('c1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE {CATComponentsFeaturesMeta.tribe_id} IN ('t1','t2') AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            MockFilterParametersNode(include=False, values=['c1']),
            f"WHERE ({CATComponentsFeaturesMeta.tribe_id} IS NULL OR {CATComponentsFeaturesMeta.tribe_id} NOT IN ('t1','t2')) AND ({CATComponentsFeaturesMeta.component_id} IS NULL OR {CATComponentsFeaturesMeta.component_id} NOT IN ('c1'))",
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
