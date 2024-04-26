import pytest
import sql_queries.Tests.csi.params as params
import sql_queries.Tests.csi.data as test_data
from pandas import DataFrame
from repository import RepositoryFactory
from sql_queries.meta.aggs import CSI
from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import assert_equal


@pytest.mark.parametrize(
    'up, want', [
        ('only_existing_tickets', test_data.only_existing_tickets),
        ('rating_range', test_data.rating_range),
    ]
)
@pytest.mark.integration
def test_csi(up, want):
    with db(
        up=f'{params.root}{up}.sql',
        down=params.down,
    ):
        got: DataFrame = RepositoryFactory.remote.create_csi_repository().get_data()

        assert_equal(got, want, (CSI.date.name, ))
