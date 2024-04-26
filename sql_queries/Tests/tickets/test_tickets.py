import pytest
import sql_queries.Tests.tickets.params as params
import sql_queries.Tests.tickets.results as results
from pandas import DataFrame
from repository import RepositoryFactory
import sql_queries.index.path.remote as path_index
from sql_queries.meta.aggs import TicketsWithIterations
from sql_queries.Tests.helpers.db import db
from sql_queries.Tests.helpers.df import assert_equal

from toolbox.sql.repository import SqlServerRepository
from toolbox.sql.repository_queries import RepositoryAlchemyQueries, SqlAlchemyQuery


@pytest.mark.parametrize(
    'up, want, query_file, tbl, dtfields', [
        (
            'sale_item_platforms',
            results.sale_item_platforms,
            path_index.sale_item_platforms,
            '#SaleItemPlatforms',
            None,
        ),
        (
            'sale_tem_products',
            results.sale_tem_products,
            path_index.sale_tem_products,
            '#SaleItemProducts',
            None,
        ),
        (
            'sale_items_flat',
            results.sale_items_flat,
            path_index.sale_items_flat,
            '#SaleItemsFlat',
            None,
        ),
        (
            'licenses',
            results.licenses,
            path_index.licenses,
            '#LisencesOnly',
            [results.lcs.revoked_since],
        ),
    ]
)
@pytest.mark.integration
def test_prerequisites(up, want, query_file, tbl, dtfields):
    with db(
        up=f'{params.root}{up}.sql',
        down=params.down,
    ):
        r = SqlServerRepository(
            queries=RepositoryAlchemyQueries(
                prep_queries=(
                    SqlAlchemyQuery(
                        query_file_path=query_file,
                        format_params={},
                    ),
                ),
                main_query_path=params.select,
                main_query_format_params={
                    'select': '*',
                    'from': tbl,
                }
            )
        )

        assert_equal(r.get_data(), want, dtfields)


@pytest.mark.integration
def test_tickets_with_licenses():
    with db(
        up=params.tickets_with_licenses,
        down=params.down,
    ):
        r = SqlServerRepository(
            queries=RepositoryAlchemyQueries(
                prep_queries=[
                    SqlAlchemyQuery(
                        query_file_path=path,
                        format_params={
                            'start_date': '2022-01-01',
                            'end_date': '2025-01-01',
                        },
                    ) for path in (
                        path_index.sale_item_platforms,
                        path_index.sale_tem_products,
                        path_index.sale_items_flat,
                        path_index.licenses,
                        path_index.tickets_with_licenses,
                    )
                ],
                main_query_path=params.select,
                main_query_format_params={
                    'select': '*',
                    'from': '#TicketsWithLicenses',
                },
            )
        )
        dtfields = (
            TicketsWithIterations.user_register_date.name,
            TicketsWithIterations.creation_date.name,
            results.lcs.revoked_since,
            TicketsWithIterations.subscription_start.name,
            TicketsWithIterations.expiration_date.name,
        )

        assert_equal(r.get_data(), results.tickets_with_licenses, dtfields)


@pytest.mark.integration
def test_tickets_with_properties():
    with db(
        up=params.tickets_with_properties,
        down=params.down,
    ):
        got: DataFrame = RepositoryFactory.remote.create_tickets_repository().get_data(
            years_of_history='YEAR, -35',
            employees_json='',
            start_date='2022-01-01',
            end_date='2025-01-01',
        )

        dtfields = (
            TicketsWithIterations.user_register_date.name,
            TicketsWithIterations.creation_date.name,
            TicketsWithIterations.fixed_on.name,
            TicketsWithIterations.closed_on.name,
            TicketsWithIterations.converted_to_bug_on.name,
            TicketsWithIterations.subscription_start.name,
            TicketsWithIterations.expiration_date.name,
        )

        assert_equal(got, results.tickets_with_properties, dtfields)
