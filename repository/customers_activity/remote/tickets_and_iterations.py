from toolbox.sql.repository import Repository
from toolbox.sql.sql_query import SqlQuery
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    TicketsWithLicensesMeta,
    EmployeesIterationsMeta,
)


class EmployeesIterationsRepository(Repository):
    """
    Loads employee iterations.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_employees_iterations_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **EmployeesIterationsMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return EmployeesIterationsMeta.get_values()


class CustomersTicketsRepository(Repository):
    """
    Loads customers with their tickets and licenses.
    """

    def get_prep_queries(self, kwargs: dict) -> list[SqlQuery]:
        return [
            self.sql_query_type(
                query_file_path=CustomersActivitySqlPathIndex.get_tickets_with_licenses_and_users_path(),
                format_params=kwargs,
            ),
        ]

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_properties_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsWithLicensesMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsWithLicensesMeta.get_values()
