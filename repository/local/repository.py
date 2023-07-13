from toolbox.sql_async import (
    AsyncRepository,
    AsyncSqlQuery,
    AsyncSQLiteQueryExecutor,
    AsyncRepositoryQueries,
    QueryDescriptor,
)
from toolbox.utils.converters import Object_to_JSON
from repository.local.aggs import get_metrics_projections
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
def create_repository(query_descriptor: QueryDescriptor) -> AsyncRepository:
    return AsyncRepository(
        queries=AsyncRepositoryQueries[AsyncSqlQuery](main_query=query_descriptor),
        query_executor=AsyncSQLiteQueryExecutor()
    )


tickets_with_iterations_period = create_repository(sqlite_tickets_with_iterations.TicketsPeriod())
customers_groups = create_repository(sqlite_customers.CustomersGroups())
tracked_customers_groups = create_repository(sqlite_customers.TrackedCustomersGroups())
tickets_types = create_repository(sqlite_tickets.TicketsTypes())
tickets_tags = create_repository(sqlite_tickets.TicketsTags())
replies_types = create_repository(sqlite_cat.CATRepliesTypes())
frameworks = create_repository(sqlite_tickets.Frameworks())
operating_systems = create_repository(sqlite_tickets.OperatingSystems())
builds = create_repository(sqlite_tickets.Builds())
severity = create_repository(sqlite_tickets.Severity())
ticket_statuses = create_repository(sqlite_tickets.TicketStatuses())
ides = create_repository(sqlite_tickets.IDEs())
license_statuses = create_repository(sqlite_licenses_conversion.LicenseStatuses())
conversion_statuses = create_repository(sqlite_licenses_conversion.ConversionStatuses())
platforms = create_repository(sqlite_platforms_products.Platforms())
products = create_repository(sqlite_platforms_products.Products())
components = create_repository(sqlite_cat.CATComponents())
features = create_repository(sqlite_cat.CATFeatures())
tickets_with_iterations_raw = create_repository(sqlite_tickets_with_iterations.TicketsWithIterationsRaw())
tickets_with_iterations_aggregates = create_repository(sqlite_tickets_with_iterations.TicketsWithIterationsAggregates())
emp_positions = create_repository(sqlite_employees.EmpPositions())
emp_tribes = create_repository(sqlite_employees.EmpTribes())
emp_tents = create_repository(sqlite_employees.EmpTents())
employees = create_repository(sqlite_employees.Employees())
customers = create_repository(sqlite_customers.Customers())
customers_validation = create_repository(sqlite_customers.CustomersValidation())

async def get_group_by_periods() -> str:
    return await PeriodsGenerator.get_group_by_periods_json()

async def get_display_filter(*args) -> str:
    return await DisplayFilterGenerator.generate_display_filter(*args)

async def get_periods_array(**kwargs) -> str:
    return await PeriodsGenerator.generate_periods(**kwargs)


# yapf: enable
async def get_metrics() -> str:
    return Object_to_JSON.convert(
        get_metrics_projections(
            projector=lambda x: {
                'name': x.name,
                'group': x.group,
                'context': 0,
            }
        )
    )
