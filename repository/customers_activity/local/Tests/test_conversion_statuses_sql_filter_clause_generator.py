import pytest
from repository.customers_activity.local.sql_query_params_generator.conversion_statuses import ConversionStatusesSqlFilterClauseGenerator
from sql_queries.customers_activity.meta import ConversionStatusesMeta
from repository.customers_activity.local.Tests.mocks import MockFilterParametersNode


@pytest.mark.parametrize(
    'input,output', [
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            f"WHERE {ConversionStatusesMeta.license_status_id} IS NULL",
        ),
        (
            MockFilterParametersNode(include=True, values=[1]),
            f"WHERE {ConversionStatusesMeta.license_status_id} IN (1)",
        ),
        (
            MockFilterParametersNode(include=False, values=[1]),
            f"WHERE ({ConversionStatusesMeta.license_status_id} IS NULL OR {ConversionStatusesMeta.license_status_id} NOT IN (1))",
        ),
        (
            MockFilterParametersNode(include=True, values=[1, 2]),
            f"WHERE {ConversionStatusesMeta.license_status_id} IN (1,2)",
        ),
        (
            MockFilterParametersNode(include=False, values=[1, 2]),
            f"WHERE ({ConversionStatusesMeta.license_status_id} IS NULL OR {ConversionStatusesMeta.license_status_id} NOT IN (1,2))",
        ),
    ]
)
def test_generate_conversion_filter(
    input: list[str],
    output: str,
):
    assert ConversionStatusesSqlFilterClauseGenerator.generate_conversion_filter(
        license_status_ids=input
    ) == output
