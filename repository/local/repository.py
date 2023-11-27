from toolbox.sql_async import (
    AsyncRepository,
    AsyncSqlQuery,
    AsyncSQLiteQueryExecutor,
    AsyncRepositoryQueries,
    QueryDescriptor,
)
from toolbox.utils.converters import Object_to_JSON
from repository.local.aggs import select_metrics
import repository.local.customers as _customers
import repository.local.tickets as _tickets
import repository.local.platforms_products as _platforms_products
import repository.local.cat as _cat
import repository.local.tickets_with_iterations as _tickets_with_iterations
import repository.local.employees as _employees
import repository.local.tribes_tents as _tribes_tents
import repository.local.generators.filters_generators.display_filter as DisplayFilterGenerator
import toolbox.sql.generators.sqlite.periods_generator as PeriodsGenerator


# yapf: disable
def create_repository(query_descriptor: QueryDescriptor) -> AsyncRepository:
    return AsyncRepository(
        queries=AsyncRepositoryQueries[AsyncSqlQuery](main_query=query_descriptor),
        query_executor=AsyncSQLiteQueryExecutor()
    )


tickets_with_iterations_period = create_repository(_tickets_with_iterations.TicketsPeriod())
customers_groups = create_repository(_customers.CustomersGroups())
tracked_customers_groups = create_repository(_customers.TrackedCustomersGroups())
tickets_types = create_repository(_tickets.TicketsTypes())
tickets_tags = create_repository(_tickets.TicketsTags())
replies_types = create_repository(_cat.CATRepliesTypes())
frameworks = create_repository(_tickets.Frameworks())
operating_systems = create_repository(_tickets.OperatingSystems())
builds = create_repository(_tickets.Builds())
severity = create_repository(_tickets.Severity())
ticket_statuses = create_repository(_tickets.TicketStatuses())
ides = create_repository(_tickets.IDEs())
license_statuses = create_repository(_customers.LicenseStatuses())
conversion_statuses = create_repository(_customers.ConversionStatuses())
platforms = create_repository(_platforms_products.Platforms())
products = create_repository(_platforms_products.Products())
components = create_repository(_cat.CATComponents())
features = create_repository(_cat.CATFeatures())
tickets_with_iterations_raw = create_repository(_tickets_with_iterations.TicketsWithIterationsRaw())
tickets_with_iterations_aggregates = create_repository(_tickets_with_iterations.TicketsWithIterationsAggregates())
emp_positions = create_repository(_employees.Positions())
emp_tribes = create_repository(_employees.EmpTribes())
emp_tents = create_repository(_employees.EmpTents())
roles = create_repository(_employees.Roles())
employees = create_repository(_employees.Employees())
customers = create_repository(_customers.Customers())
customers_validation = create_repository(_customers.CustomersValidation())
tents = create_repository(_tribes_tents.Tents())
tribes = create_repository(_tribes_tents.Tribes())

async def get_group_by_periods() -> str:
    return await PeriodsGenerator.get_group_by_periods_json()

async def get_display_filter(*args) -> str:
    return await DisplayFilterGenerator.generate_display_filter(*args)

async def get_periods_array(**kwargs) -> str:
    return await PeriodsGenerator.generate_periods(**kwargs)


# yapf: enable
async def get_metrics() -> str:
    return Object_to_JSON.convert(
        select_metrics(
            projector=lambda metric: {
                'name': metric.name,
                'displayName': metric.get_display_name(),
                'group': metric.group,
                'context': 0,
            }
        )
    )
