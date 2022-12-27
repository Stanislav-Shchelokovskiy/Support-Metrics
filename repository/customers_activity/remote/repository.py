from pandas import DataFrame
from toolbox.sql.repository import Repository
from toolbox.sql.sql_query import SqlQuery
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    TicketsTagsMeta,
    TicketsWithIterationsMeta,
    TicketsTypesMeta,
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
    ConversionStatusesMeta,
    PlatformsProductsMeta,
    PositionsMeta,
    EmployeesIterations,
)


class GroupsRepository(Repository):
    """
    Loads groups we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_customers_groups_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersGroupsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TagsRepository(Repository):
    """
    Loads tags we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tags_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsTagsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTagsMeta.get_values()


class RepliesTypesRepository(Repository):
    """
    Loads CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_replies_types_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **ReplyTypesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ReplyTypesMeta.get_values()


class PositionsRepository(Repository):
    """
    Loads employees positions.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_positions_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **PositionsMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return PositionsMeta.get_values()


class LicenseStatusesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                TicketsTypesMeta.id: [0, 1, 2, 3, 4],
                TicketsTypesMeta.name:
                    [
                        'Licensed',
                        'Expired',
                        'Revoked',
                        'Free',
                        'Trial',
                    ]
            }
        )


class ConversionStatusesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                ConversionStatusesMeta.license_status_id: [0, 3, 4, 4],
                ConversionStatusesMeta.id: [5, 6, 5, 6],
                ConversionStatusesMeta.name: [
                    'Paid',
                    'Free',
                    'Paid',
                    'Free',
                ]
            }
        )


class ComponentsFeaturesRepository(Repository):
    """
    Loads CAT components and features.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_components_features_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **ComponentsFeaturesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ComponentsFeaturesMeta.get_values()


class PlatformsProductsRepository(Repository):
    """
    Loads available platforms and products.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_platforms_products_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **PlatformsProductsMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return PlatformsProductsMeta.get_values()


class EmployeesIterationsRepository(Repository):
    """
    Loads employee iterations.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_employees_iterations_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **EmployeesIterations.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return EmployeesIterations.get_values()


class TicketsWithIterationsRepository(Repository):
    """
    Loads customers with their tickets and iterations.
    """

    def get_prep_queries(self, kwargs: dict) -> list[SqlQuery]:
        return [
            self.sql_query_type(
                query_file_path=CustomersActivitySqlPathIndex.
                get_create_tickets_with_iterations_and_licenses_temp_table_path(
                ),
                format_params={},
            ),
            self.sql_query_type(
                query_file_path=CustomersActivitySqlPathIndex.
                get_fill_tickets_with_iterations_path(),
                format_params=kwargs,
            ),
        ]

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsWithIterationsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsWithIterationsMeta.get_values()
