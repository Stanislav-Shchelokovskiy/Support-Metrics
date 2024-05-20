import pytest
from Tests.utils import (
    response_is_valid,
    network_post,
)
from Tests.test_case import TestCase
import Tests.cases as cases


# yapf: disable
@pytest.mark.e2e
@pytest.mark.parametrize(
    'resp_file,case', [
        ('people', cases.people),
    ]
)
def test_aggregates(resp_file: str, case: TestCase, test_client):
    response = network_post(
        client=test_client,
        url='/TicketsWithIterationsAggregates?'+
                f'group_by_period={case.group_by}&' +
                    f'range_start={case.start}&' +
                        f'range_end={case.end}&' +
                            f'baseline_aligned_mode_enabled={case.baseline_aligned_mode_enabled}&' +
                                f'metric={case.metric}',
        body=case.body,
    )
    assert response_is_valid(
        file=resp_file,
        check_file=resp_file,
        response=response,
    )
