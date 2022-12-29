import pytest
from repository.customers_activity.local.sql_query_params_generator.employees import EmployeesSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import EmployeesMeta


@pytest.mark.parametrize(
    'positions,output', [
        (
            [],
            '',
        ),
        (
            ['p1'],
            f"WHERE {EmployeesMeta.position_id} IN ('p1')",
        ),
        (
            ['p1', 'p2'],
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2')",
        ),
    ]
)
def test_generate_positions_filter(
    positions: list[str],
    output: str,
):
    assert EmployeesSqlFilterClauseGenerator.generate_positions_filter(
        position_ids=positions
    ) == output


@pytest.mark.parametrize(
    'positions,tribes,output', [
        (
            [],
            [],
            '',
        ),
        (
            ['p1'],
            [],
            f"WHERE {EmployeesMeta.position_id} IN ('p1')",
        ),
        (
            [],
            ['t1'],
            f"WHERE {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            ['p1'],
            ['t1'],
            f"WHERE {EmployeesMeta.position_id} IN ('p1') AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
        (
            ['p1', 'p2'],
            ['t1', 't2'],
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2') AND {EmployeesMeta.tribe_id} IN ('t1','t2')",
        ),
        (
            ['p1', 'p2'],
            ['t1'],
            f"WHERE {EmployeesMeta.position_id} IN ('p1','p2') AND {EmployeesMeta.tribe_id} IN ('t1')",
        ),
    ]
)
def test_generate_filter(
    positions: list[str],
    tribes: list[str],
    output: str,
):
    assert EmployeesSqlFilterClauseGenerator.generate_filter(
        position_ids=positions,
        tribe_ids=tribes,
    ) == output
