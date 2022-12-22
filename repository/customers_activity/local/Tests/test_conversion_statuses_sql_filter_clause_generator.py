import pytest
from repository.customers_activity.local.sql_query_params_generator import ConversionStatusesSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import ConversionStatusesMeta


def test_generate_filter_raises_value_error():
    with pytest.raises(ValueError) as excInfo:
        ConversionStatusesSqlFilterClauseGenerator.generate_filter(
            license_status_ids=[]
        )
        assert 'license_status_ids cannot be empty' in str(excInfo)


@pytest.mark.parametrize(
    'input,output', [
        (
            [1],
            f"WHERE {ConversionStatusesMeta.license_status_id} IN (1)",
        ),
        (
            [1, 2],
            f"WHERE {ConversionStatusesMeta.license_status_id} IN (1,2)",
        ),
    ]
)
def test_generate_filter(
    input: list[str],
    output: str,
):
    assert ConversionStatusesSqlFilterClauseGenerator.generate_filter(
        license_status_ids=input
    ) == output
