import pytest
from toolbox.sql.generators.Tests.mocks import MockFilterParametersNode
from sql_queries.meta.cat import CatComponentsFeatures
from sql_queries.meta.customers import ConversionStatuses
from sql_queries.meta.platforms_products import PlatformsProducts
from sql_queries.meta.employees import Employees
import repository.local.generators.filters_generators.cat as CATSqlFilterClauseGenerator
import repository.local.generators.filters_generators.conversion_statuses as ConversionStatusesSqlFilterClauseGenerator
import repository.local.generators.filters_generators.employees as EmployeesSqlFilterClauseGenerator
import repository.local.generators.filters_generators.platforms_products as PlatformsProductsSqlFilterClauseGenerator


# yapf: disable
@pytest.mark.parametrize(
    'generator, field, param_name, values_converter', [
        (
            CATSqlFilterClauseGenerator.generate_components_filter,
            CatComponentsFeatures.tent_id,
            'tent_ids',
            None,
        ),
        (
            ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter,
            ConversionStatuses.license_status_id,
            'license_status_ids',
            str,
        ),
        (
            EmployeesSqlFilterClauseGenerator.generate_positions_filter,
            Employees.position_id,
            'position_ids',
            None,
        ),
        (
            PlatformsProductsSqlFilterClauseGenerator.generate_platforms_filter,
            PlatformsProducts.platform_tent_id,
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
            CatComponentsFeatures.tent_id,
            CatComponentsFeatures.component_id,
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
            f"WHERE {PlatformsProducts.product_tent_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {PlatformsProducts.product_tent_id} IN ('t1') OR {PlatformsProducts.platform_tent_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({PlatformsProducts.product_tent_id} IS NULL OR {PlatformsProducts.product_tent_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {PlatformsProducts.product_tent_id} IN ('t1','t2') OR {PlatformsProducts.platform_tent_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({PlatformsProducts.product_tent_id} IS NULL OR {PlatformsProducts.product_tent_id} NOT IN ('t1','t2'))",
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
    'positions, tribes, tents, roles, output', [
        (
            None,
            None,
            None,
            None,
            '',
        ), (
            None,
            None,
            None,
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {Employees.tent_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['r1']),
            f"WHERE {Employees.tribe_id} IN ('t1') AND {Employees.tent_id} IN ('t1') AND ({Employees.roles} LIKE '%r1%')",
        ),
        (
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=True, values=['t1']),
            MockFilterParametersNode(include=False, values=['t1']),
            MockFilterParametersNode(include=False, values=['r1']),
            f"WHERE {Employees.position_id} IN ('t1') AND {Employees.tribe_id} IN ('t1') AND ({Employees.tent_id} IS NULL OR {Employees.tent_id} NOT IN ('t1')) AND ({Employees.roles} IS NULL OR NOT ({Employees.roles} LIKE '%r1%'))",
        )
    ]
)
def test_generate_positions_tribes_tents_roles_filter(
    positions: MockFilterParametersNode,
    tribes: MockFilterParametersNode,
    tents: MockFilterParametersNode,
    roles:MockFilterParametersNode,
    output: str,
):
    assert EmployeesSqlFilterClauseGenerator.generate_positions_tribes_tents_roles_filter(
        position_ids=positions,
        tribe_ids=tribes,
        tent_ids=tents,
        roles=roles,
    ) == output
