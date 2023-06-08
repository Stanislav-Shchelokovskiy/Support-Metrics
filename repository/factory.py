from toolbox.sql.repository import SqlServerRepository, Repository
from toolbox.sql.repository_queries import RepositoryQueries

from toolbox.sql_async import (
    AsyncRepository,
    AsyncSqlQuery,
    AsyncSQLiteQueryExecutor,
    AsyncRepositoryQueries,
    QueryDescriptor,
)

import repository.remote.tickets_and_iterations as tickets_and_iterations
import repository.remote.tickets as tickets
import repository.remote.customers_groups as customers_groups
import repository.remote.cat as cat
import repository.remote.platforms_products as platforms_products
import repository.remote.licenses_conversion as licenses_conversion
import repository.remote.employees as employees

import repository.local.customers as sqlite_customers
import repository.local.tickets as sqlite_tickets
import repository.local.licenses_conversion as sqlite_licenses_conversion
import repository.local.platforms_products as sqlite_platforms_products
import repository.local.cat as sqlite_cat
import repository.local.tickets_with_iterations as sqlite_tickets_with_iterations
import repository.local.employees as sqlite_employees

import repository.local.generators.filters_generators.display_filter as DisplayFilterGenerator
import toolbox.sql.generators.sqlite_periods_generator as PeriodsGenerator


# yapf: disable
class SqlServerFactory:
    def _create_repository(self, queries: RepositoryQueries) -> Repository:
        return SqlServerRepository(queries=queries)

    def create_customers_groups_repository(self) -> Repository:
        return self._create_repository(queries=customers_groups.CustomersGroups())

    def create_tracked_customers_groups_repository(self) -> Repository:
        return self._create_repository(queries=customers_groups.TrackedCustomersGroups())

    def create_tickets_tags_repository(self) -> Repository:
        return self._create_repository(queries=tickets.TicketsTags())

    def create_cat_replies_types_repository(self) -> Repository:
        return self._create_repository(queries=cat.CATRepliesTypes())

    def create_cat_components_features_repository(self) -> Repository:
        return self._create_repository(queries=cat.CATComponentsFeatures())

    def create_customers_tickets_repository(self) -> Repository:
        return self._create_repository(queries=tickets_and_iterations.CustomersTickets())

    def create_license_statuses_repository(self) -> Repository:
        return licenses_conversion.LicenseStatusesRepository()

    def create_conversion_statuses_repository(self) -> Repository:
        return licenses_conversion.ConversionStatusesRepository()

    def create_platforms_products_repository(self) -> Repository:
        return self._create_repository(queries=platforms_products.PlatformsProducts())

    def create_employees_iterations_repository(self) -> Repository:
        return self._create_repository(queries=tickets_and_iterations.EmployeesIterations())

    def create_employees_repository(self) -> Repository:
        return self._create_repository(queries=employees.Employees())

    def create_tickets_types_repository(self) -> Repository:
        return self._create_repository(queries=tickets.TicketsTypes())

    def create_frameworks_repository(self) -> Repository:
        return self._create_repository(queries=tickets.Frameworks())

    def create_operating_systems_repository(self) -> Repository:
        return self._create_repository(queries=tickets.OperatingSystems())

    def create_builds_repository(self) -> Repository:
        return self._create_repository(queries=tickets.Builds())

    def create_severity_repository(self) -> Repository:
        return self._create_repository(queries=tickets.Severity())

    def create_ticket_statuses_repository(self) -> Repository:
        return self._create_repository(queries=tickets.TicketStatuses())

    def create_ides_repository(self) -> Repository:
        return self._create_repository(queries=tickets.IDEs())


class SqliteFactory:
    def _create_repository(self, query_descriptor: QueryDescriptor) -> AsyncRepository:
        return AsyncRepository(
            queries=AsyncRepositoryQueries[AsyncSqlQuery](main_query=query_descriptor),
            query_executor=AsyncSQLiteQueryExecutor()
        )

    def create_tickets_with_iterations_period_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets_with_iterations.TicketsPeriod())

    def create_customers_groups_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_customers.CustomersGroups())

    def create_tracked_customers_groups_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_customers.TrackedCustomersGroups())

    def create_tickets_types_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.TicketsTypes())

    def create_tickets_tags_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.TicketsTags())

    def create_reply_types_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_cat.CATRepliesTypes())

    def create_frameworks_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.Frameworks())

    def create_operating_systems_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.OperatingSystems())

    def create_builds_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.Builds())

    def create_severity_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.Severity())

    def create_ticket_statuses_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.TicketStatuses())

    def create_ides_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets.IDEs())

    def create_license_statuses_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_licenses_conversion.LicenseStatuses())

    def create_conversion_statuses_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_licenses_conversion.ConversionStatuses())

    def create_platforms_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_platforms_products.Platforms())

    def create_products_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_platforms_products.Products())

    def create_components_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_cat.CATComponents())

    def create_features_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_cat.CATFeatures())

    def create_tickets_with_iterations_raw_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets_with_iterations.TicketsWithIterationsRaw())

    def create_tickets_with_iterations_aggregates_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_tickets_with_iterations.TicketsWithIterationsAggregates())

    def create_emp_positions_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_employees.EmpPositions())

    def create_emp_tribes_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_employees.EmpTribes())

    def create_emp_tents_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_employees.EmpTents())

    def create_employees_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_employees.Employees())

    def create_customers_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_customers.Customers())

    def create_customers_validation_repository(self) -> AsyncRepository:
        return self._create_repository(query_descriptor=sqlite_customers.CustomersValidation())

    def create_display_filter_generator(self) -> DisplayFilterGenerator:
        return DisplayFilterGenerator

    def create_periods_generator(self) -> PeriodsGenerator:
        return PeriodsGenerator
# yapf: enable

remote = SqlServerFactory()
local = SqliteFactory()
