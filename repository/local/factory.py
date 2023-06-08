from toolbox.sql_async import (
    AsyncRepository,
    AsyncSqlQuery,
    AsyncSQLiteQueryExecutor,
    AsyncRepositoryQueries,
    QueryDescriptor,
)
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
def __create_repository(query_descriptor: QueryDescriptor) -> AsyncRepository:
    return AsyncRepository(
        queries=AsyncRepositoryQueries[AsyncSqlQuery](main_query=query_descriptor),
        query_executor=AsyncSQLiteQueryExecutor()
    )

def create_tickets_with_iterations_period_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets_with_iterations.TicketsPeriod())

def create_customers_groups_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_customers.CustomersGroups())

def create_tracked_customers_groups_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_customers.TrackedCustomersGroups())

def create_tickets_types_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.TicketsTypes())

def create_tickets_tags_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.TicketsTags())

def create_reply_types_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_cat.CATRepliesTypes())

def create_frameworks_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.Frameworks())

def create_operating_systems_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.OperatingSystems())

def create_builds_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.Builds())

def create_severity_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.Severity())

def create_ticket_statuses_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.TicketStatuses())

def create_ides_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets.IDEs())

def create_license_statuses_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_licenses_conversion.LicenseStatuses())

def create_conversion_statuses_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_licenses_conversion.ConversionStatuses())

def create_platforms_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_platforms_products.Platforms())

def create_products_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_platforms_products.Products())

def create_components_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_cat.CATComponents())

def create_features_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_cat.CATFeatures())

def create_tickets_with_iterations_raw_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets_with_iterations.TicketsWithIterationsRaw())

def create_tickets_with_iterations_aggregates_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_tickets_with_iterations.TicketsWithIterationsAggregates())

def create_emp_positions_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_employees.EmpPositions())

def create_emp_tribes_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_employees.EmpTribes())

def create_emp_tents_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_employees.EmpTents())

def create_employees_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_employees.Employees())

def create_customers_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_customers.Customers())

def create_customers_validation_repository() -> AsyncRepository:
    return __create_repository(query_descriptor=sqlite_customers.CustomersValidation())

def create_display_filter_generator() -> DisplayFilterGenerator:
    return DisplayFilterGenerator

def create_periods_generator() -> PeriodsGenerator:
    return PeriodsGenerator
