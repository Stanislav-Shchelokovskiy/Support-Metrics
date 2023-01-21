import pytest
from repository.customers_activity.local.query_parts.sub_queries.customers_rank import get_percentile_filter
from repository.customers_activity.local.Tests.mocks import (
    Percentile,
    FilterParameterNode,
)


@pytest.mark.parametrize(
    'alias, percentile, output', [
        (
            'alias',
            Percentile(
                metric='tickets',
                value=FilterParameterNode(include=True, value=100)
            ),
            'alias <= 100',
        ),
        (
            'alias',
            Percentile(
                metric='tickets',
                value=FilterParameterNode(include=False, value=100)
            ),
            'alias > 100',
        ),
        (
            'alias',
            Percentile(
                metric='tickets',
                value=FilterParameterNode(include=True, value=50)
            ),
            'alias <= 50',
        ),
        (
            'alias',
            Percentile(
                metric='tickets',
                value=FilterParameterNode(include=False, value=50)
            ),
            'alias > 50',
        ),
    ]
)
def test_get_percentile_filter(
    alias: str,
    percentile: Percentile,
    output: str,
):
    assert get_percentile_filter(alias=alias, percentile=percentile) == output