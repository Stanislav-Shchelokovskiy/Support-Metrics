from toolbox.sql.repository import SqlServerRepository, Repository
from toolbox.sql.repository_queries import RepositoryQueries
import repository.remote.tickets_and_iterations as tickets_and_iterations
import repository.remote.tickets as tickets
import repository.remote.customers_groups as customers_groups
import repository.remote.cat as cat
import repository.remote.platforms_products as platforms_products
import repository.remote.licenses_conversion as licenses_conversion
import repository.remote.employees as employees
import repository.remote.csi as csi
import repository.remote.tents as tents
import repository.remote.tribes as tribes
import repository.remote.resolution_time as resolution_time


def __create_repository(queries: RepositoryQueries) -> Repository:
    return SqlServerRepository(queries=queries)


def create_customers_groups_repository() -> Repository:
    return __create_repository(queries=customers_groups.CustomersGroups())


def create_tracked_customers_groups_repository() -> Repository:
    return __create_repository(queries=customers_groups.TrackedCustomersGroups())


def create_tickets_tags_repository() -> Repository:
    return __create_repository(queries=tickets.TicketsTags())


def create_cat_replies_types_repository() -> Repository:
    return __create_repository(queries=cat.CATRepliesTypes())


def create_cat_components_features_repository() -> Repository:
    return __create_repository(queries=cat.CATComponentsFeatures())


def create_tickets_repository() -> Repository:
    return __create_repository(queries=tickets_and_iterations.Tickets())


def create_license_statuses_repository() -> Repository:
    return licenses_conversion.LicenseStatusesRepository()


def create_conversion_statuses_repository() -> Repository:
    return licenses_conversion.ConversionStatusesRepository()


def create_platforms_products_repository() -> Repository:
    return __create_repository(queries=platforms_products.PlatformsProducts())


def create_employees_iterations_repository() -> Repository:
    return __create_repository(queries=tickets_and_iterations.EmployeesIterations())


def create_employees_repository() -> Repository:
    return __create_repository(queries=employees.Employees())


def create_roles_repository() -> Repository:
    return __create_repository(queries=employees.Roles())


def create_tickets_types_repository() -> Repository:
    return __create_repository(queries=tickets.TicketsTypes())


def create_frameworks_repository() -> Repository:
    return __create_repository(queries=tickets.Frameworks())


def create_operating_systems_repository() -> Repository:
    return __create_repository(queries=tickets.OperatingSystems())


def create_builds_repository() -> Repository:
    return __create_repository(queries=tickets.Builds())


def create_severity_repository() -> Repository:
    return __create_repository(queries=tickets.Severity())


def create_ticket_statuses_repository() -> Repository:
    return __create_repository(queries=tickets.TicketStatuses())


def create_ides_repository() -> Repository:
    return __create_repository(queries=tickets.IDEs())


def create_csi_repository() -> Repository:
    return __create_repository(queries=csi.CSI())


def create_tents_repository() -> Repository:
    return __create_repository(queries=tents.Tents())


def create_tribes_repository() -> Repository:
    return __create_repository(queries=tribes.Tribes())

def create_resolution_time_repository() -> Repository:
    return __create_repository(queries=resolution_time.ResolutionTime())
