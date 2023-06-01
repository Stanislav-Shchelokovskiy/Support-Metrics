import pytest
from toolbox.sql.generators.Tests.mocks import MockFilterParametersNode
import repository.customers_activity.local.generators.filters_generators.cat as CATSqlFilterClauseGenerator
import repository.customers_activity.local.generators.filters_generators.conversion_statuses as ConversionStatusesSqlFilterClauseGenerator
import repository.customers_activity.local.generators.filters_generators.employees as EmployeesSqlFilterClauseGenerator
import repository.customers_activity.local.generators.filters_generators.platforms_products as PlatformsProductsSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import (
    CATComponentsFeaturesMeta,
    ConversionStatusesMeta,
    EmployeesMeta,
    PlatformsProductsMeta,
)


# yapf: disable
@pytest.mark.parametrize(
    'generator, field, param_name, values_converter', [
        (
            CATSqlFilterClauseGenerator.generate_components_filter,
            CATComponentsFeaturesMeta.tent_id,
            'tent_ids',
            None,
        ),
        (
            ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter,
            ConversionStatusesMeta.license_status_id,
            'license_status_ids',
            str,
        ),
        (
            EmployeesSqlFilterClauseGenerator.generate_positions_filter,
            EmployeesMeta.position_id,
            'position_ids',
            None,
        ),
        (
            PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter,
            PlatformsProductsMeta.platform_tent_id,
            'tent_ids',
            None,
        ),
    ]
)
def test_single_in_filters(
    generator,
    field: str,
    param_name: str,
    values_converter,
    single_in_filter_cases,
):
    for values, output in single_in_filter_cases(values_converter):
        assert generator(**{param_name: values}) == output.format(field=field)
# yapf: enable


@pytest.mark.parametrize(
    'generator, field1, field2, param_name1, param_name2, values_converter', [
        (
            CATSqlFilterClauseGenerator.generate_features_filter,
            CATComponentsFeaturesMeta.tent_id,
            CATComponentsFeaturesMeta.component_id,
            'tent_ids',
            'component_ids',
            None,
        )
    ]
)
def test_double_in_filter(
    generator,
    field1,
    field2,
    param_name1,
    param_name2,
    values_converter,
    double_in_filter_cases,
):
    for values1, values2, output in double_in_filter_cases(values_converter):
        assert generator(**{
            param_name1: values1,
            param_name2: values2
        }) == output.format(field1=field1, field2=field2)


@pytest.mark.parametrize(
    'tents, output', [
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
            f"WHERE {PlatformsProductsMeta.product_tent_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {PlatformsProductsMeta.product_tent_id} IN ('t1') OR {PlatformsProductsMeta.platform_tent_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({PlatformsProductsMeta.product_tent_id} IS NULL OR {PlatformsProductsMeta.product_tent_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {PlatformsProductsMeta.product_tent_id} IN ('t1','t2') OR {PlatformsProductsMeta.platform_tent_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({PlatformsProductsMeta.product_tent_id} IS NULL OR {PlatformsProductsMeta.product_tent_id} NOT IN ('t1','t2'))",
        ),
    ]
)
def test_generate_products_filter(
    tents: MockFilterParametersNode,
    output: str,
):
    assert PlatformsProductsSqlFilterClauseGenerator.generate_products_filter(
        tent_ids=tents,
    ) == output


@pytest.mark.parametrize(
    'positions, tribes, tents, output', [
        (
            None,
            None,
            None,
            '',
        ), (
            None,
            None,
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {EmployeesMeta.tent_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {EmployeesMeta.tribe_id} IN ('t1') AND {EmployeesMeta.tent_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IN ('t1') AND {EmployeesMeta.tribe_id} IN ('t1') AND ({EmployeesMeta.tent_id} IS NULL OR {EmployeesMeta.tent_id} NOT IN ('t1'))",
        )
    ]
)
def test_generate_positions_tribes_tents_filter(
    positions: MockFilterParametersNode,
    tribes: MockFilterParametersNode,
    tents: MockFilterParametersNode,
    output: str,
):
    assert EmployeesSqlFilterClauseGenerator.generate_positions_tribes_tents_filter(
        position_ids=positions,
        tribe_ids=tribes,
        tent_ids=tents,
    ) == output
