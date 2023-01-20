import pytest
from repository.customers_activity.local.sql_filters_generator.employees import EmployeesSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import EmployeesMeta
from repository.customers_activity.local.Tests.mocks import MockFilterParametersNode


@pytest.mark.parametrize(
    'positions,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {EmployeesMeta.position_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1','p2'))",
        ),
    ]
)
def test_generate_positions_filter(
    positions: list[str],
    output: str,
):
    assert EmployeesSqlFilterClauseGenerator._generate_positions_filter(
        position_ids=positions
    ) == output


@pytest.mark.parametrize(
    'positions,tribes,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {EmployeesMeta.position_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {EmployeesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {EmployeesMeta.position_id} IS NULL AND {EmployeesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE {EmployeesMeta.position_id} IN ('p1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            MockFilterParametersNode(include=True, values=[]),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {EmployeesMeta.position_id} IN ('p1') AND {EmployeesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1')) AND {EmployeesMeta.tribe_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IS NULL AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IS NULL AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1') AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1')) AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1') AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1')) AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2') AND {EmployeesMeta.tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            MockFilterParametersNode(include=True, values=['t1', 't2']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1','p2')) AND {EmployeesMeta.tribe_id} IN ('t1','t2')",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2') AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1','t2'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            MockFilterParametersNode(include=False, values=['t1', 't2']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1','p2')) AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1','t2'))",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2') AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            MockFilterParametersNode(include=True, values=['t1']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1','p2')) AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2') AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1'))",
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            MockFilterParametersNode(include=False, values=['t1']),
            f"WHERE ({EmployeesMeta.position_id} IS NULL OR {EmployeesMeta.position_id} NOT IN ('p1','p2')) AND ({EmployeesMeta.tribe_id} IS NULL OR {EmployeesMeta.tribe_id} NOT IN ('t1'))",
        ),
    ]
)
def test_generate_positions_tribes_filter(
    positions: list[str],
    tribes: list[str],
    output: str,
):
    assert EmployeesSqlFilterClauseGenerator.generate_positions_tribes_filter(
        position_ids=positions,
        tribe_ids=tribes,
    ) == output
