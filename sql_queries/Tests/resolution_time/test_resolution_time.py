import pytest
import sql_queries.Tests.resolution_time.params as params
import sql_queries.Tests.resolution_time.cases as cases
from pandas import DataFrame
from repository import RepositoryFactory
from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import assert_equal


@pytest.mark.parametrize(
    'up, want', [
        ('iterations_in_non_bugs_only', cases.iterations_in_non_bugs_only),
        ('bugs_only_after_most_recent_conversion_to_bug', cases.bugs_only_after_most_recent_conversion_to_bug),
        ('bugs_only_between_period', cases.bugs_only_between_period),
        ('only_bugs_with_audit', cases.only_bugs_with_audit),
        ('bugs_with_only_closed_audit_records', cases.bugs_with_only_closed_audit_records),
        ('resolution_time_includes_iterations_and_bugs', cases.resolution_time_includes_iterations_and_bugs),
    ]
)
@pytest.mark.integration
def test_resolution_time(up, want):
    with db(
        up=(params.up, f'{params.root}{up}.sql'),
        down=params.down,
    ):
        got: DataFrame = RepositoryFactory.remote.create_resolution_time_repository().get_data(
            years_of_history='YEAR, -35',
            employees_json='',
        )

        assert_equal(got, want)
