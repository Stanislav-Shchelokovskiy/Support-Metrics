import pytest
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from repository import RepositoryFactory
from sql_queries.meta.aggs import ResolutionTime
from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import transform


csi = {
    ResolutionTime.ticket_scid.name: [3, 11],
    ResolutionTime.resolution_in_hours.name: [4, 22],
    ResolutionTime.lifetime_in_hours.name: [98, 22],
}


@pytest.mark.integration
def test_resolution_time():
    with db(
        up='sql_queries/Tests/resolution_time/migrations/up.sql',
        down='sql_queries/Tests/resolution_time/migrations/down.sql',
    ):
        got: DataFrame = RepositoryFactory.remote.create_resolution_time_repository().get_data(
            years_of_history='YEAR, -5',
            employees_json='',
        )

        want = DataFrame(data=csi)

        got = transform(got)
        want = transform(want)

        assert_frame_equal(got, want)
