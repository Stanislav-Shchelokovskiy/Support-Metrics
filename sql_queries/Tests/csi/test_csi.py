import pytest
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from repository import RepositoryFactory
from sql_queries.meta.aggs import CSI
from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import transform


csi = {
    CSI.ticket_scid.name: ['ticket1', 'ticket2', 'ticket3', 'ticket4'],
    CSI.date.name: ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
    CSI.rating.name: [0, -1, 1, 0],
}


@pytest.mark.integration
def test_csi():
    with db(
        up='sql_queries/Tests/csi/migrations/up.sql',
        down='sql_queries/Tests/csi/migrations/down.sql',
    ):
        got: DataFrame = RepositoryFactory.remote.create_csi_repository().get_data()

        want = DataFrame(data=csi)

        got = transform(got, dtfields=(CSI.date.name,))
        want = transform(want, dtfields=(CSI.date.name,))

        assert_frame_equal(got, want)
