import pytest
import sql_queries.Tests.tickets.params as params
import sql_queries.Tests.tickets.cases as cases
from sql_queries.Tests.test_case import TestCase
from pandas import DataFrame
from repository import RepositoryFactory

from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import assert_equal

from toolbox.sql.repository import SqlServerRepository
from toolbox.sql.repository_queries import RepositoryAlchemyQueries, SqlAlchemyQuery


@pytest.mark.parametrize(
    'up, case', [
        ('sale_item_platforms', cases.sale_item_platforms),
        ('sale_tem_products', cases.sale_tem_products),
        ('sale_items_flat', cases.sale_items_flat),
        ('licenses', cases.licenses),
        ('tickets_with_licenses', cases.tickets_with_licenses),
    ]
)
@pytest.mark.integration
def test_prerequisites(up, case: TestCase):
    with db(
        up=(params.up, f'{params.root}{up}.sql'),
        down=params.down,
    ):
        r = SqlServerRepository(
            queries=RepositoryAlchemyQueries(
                prep_queries=[
                    SqlAlchemyQuery(
                        query_file_path=query_file,
                        format_params=case.params,
                    ) for query_file in case.queries
                ],
                main_query_path=params.select,
                main_query_format_params={
                    'select': ','.join(case.want.keys()),
                    'from': case.tbl,
                }
            )
        )

        assert_equal(r.get_data(), case.want, case.dtfields)


@pytest.mark.integration
def test_tickets_with_properties():
    with db(
        up=(params.up, params.tickets_with_properties),
        down=params.down,
    ):
        case = cases.tickets_with_properties
        got: DataFrame = RepositoryFactory.remote.create_tickets_repository().get_data(**case.params)

        assert_equal(got, case.want, case.dtfields)
