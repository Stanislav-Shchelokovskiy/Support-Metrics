import pytest
import sql_queries.Tests.resolution_time.params as params
import sql_queries.Tests.resolution_time.data as test_data
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from repository import RepositoryFactory
from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import transform


@pytest.mark.parametrize(
    'up, want', [
        ('iterations_in_non_bugs_only', test_data.iterations_in_non_bugs_only),
        ('bugs_only_after_most_recent_conversion_to_bug', test_data.bugs_only_after_most_recent_conversion_to_bug),
        ('bugs_only_between_period', test_data.bugs_only_between_period),
        ('only_bugs_with_audit', test_data.only_bugs_with_audit),
        ('bugs_with_only_closed_audit_records', test_data.bugs_with_only_closed_audit_records),
        ('resolution_time_includes_iterations_and_bugs', test_data.resolution_time_includes_iterations_and_bugs),
    ]
)
@pytest.mark.integration
def test_resolution_time(up, want):
    with db(
        up=f'{params.root}{up}.sql',
        down=params.down,
    ):
        got: DataFrame = RepositoryFactory.remote.create_resolution_time_repository().get_data(
            years_of_history='YEAR, -35',
            employees_json='',
        )

        got = transform(got)
        want = transform(DataFrame(data=want))

        assert_frame_equal(got, want)
