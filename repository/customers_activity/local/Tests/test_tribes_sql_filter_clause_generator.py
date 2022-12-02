import pytest
from repository.customers_activity.local.sql_query_params_generator import TribesSqlFilterClauseGenerator


@pytest.mark.parametrize(
    'col,tribes,output', [
        (
            'col',
            [],
            '',
        ),
        (
            'col',
            ['p1', 'p2'],
            "WHERE col IN ('p1','p2')",
        ),
        (
            'col',
            ['p1'],
            "WHERE col IN ('p1')",
        ),
    ]
)
def test_generate_in_filter(col: str, tribes: list[str], output: str):
    assert TribesSqlFilterClauseGenerator.generate_in_filter(
        col=col,
        values=tribes,
    ) == output
