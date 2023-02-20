from repository.customers_activity.remote.tickets_and_iterations import (
    CustomersTicketsRepository,
    EmployeesIterationsRepository,
)
from repository.customers_activity.remote.tickets import (
    TicketsTagsRepository,
    TicketsTypesRepository,
    FrameworksRepository,
    OperatingSystemsRepository,
    BuildsRepository,
    SeverityRepository,
    TicketStatusesRepository,
    IDEsRepository,
)
from repository.customers_activity.remote.customers_groups import (
    CustomersGroupsRepository,
    TrackedCustomersGroupsRepository,
)
from repository.customers_activity.remote.cat import (
    CATRepliesTypesRepository,
    CATComponentsFeaturesRepository,
)
from repository.customers_activity.remote.platforms_products import PlatformsProductsRepository
from repository.customers_activity.remote.licenses_conversion import (
    LicenseStatusesRepository,
    ConversionStatusesRepository,
)
from repository.customers_activity.local.customers import (
    CustomersGroupsRepository as SqliteCustomersGroupsRepository,
    TrackedCustomersGroupsRepository as SqliteTrackedCustomersGroupsRepository,
    CustomersRepository as SqliteCustomersRepository,
)
from repository.customers_activity.local.tickets import (
    TicketsTypesRepository as SqliteTicketsTypesRepository,
    TicketsTagsRepository as SqliteTicketsTagsRepository,
    FrameworksRepository as SqliteFrameworksRepository,
    OperatingSystemsRepository as SqliteOperatingSystemsRepository,
    BuildsRepository as SqliteBuildsRepository,
    SeverityRepository as SqliteSeverityRepository,
    TicketStatueseRepository as SqliteTicketStatueseRepository,
    IDEsRepository as SqliteIDEsRepository,
)
from repository.customers_activity.local.licenses_conversion import (
    LicenseStatusesRepository as SqliteLicenseStatusesRepository,
    ConversionStatusesRepository as SqliteConversionStatusesRepository,
)
from repository.customers_activity.local.platforms_products import (
    PlatformsRepository as SqlitePlatformsRepository,
    ProductsRepository as SqliteProductsRepository,
)
from repository.customers_activity.local.cat import (
    CATRepliesTypesRepository as SqliteReplyTypesRepository,
    CATComponentsRepository as SqliteComponentsRepository,
    CATFeaturesRepository as SqliteFeaturesRepository,
)
from repository.customers_activity.local.tickets_with_iterations import (
    TicketsPeriodRepository as SqliteTicketsWithIterationsPeriodRepository,
    TicketsWithIterationsRawRepository as
    SqliteTicketsWithIterationsRawRepository,
    TicketsWithIterationsAggregatesRepository as
    SqliteTicketsWithIterationsAggregatesRepository,
)
from repository.customers_activity.local.employees import (
    EmpPositionsRepository as SqliteEmpPositionsRepository,
    EmpTribesRepository as SqliteEmpTribesRepository,
    EmployeesRepository as SqliteEmployeesRepository,
)
from repository.customers_activity.local.generators.filters_generators.display_filter import DisplayFilterGenerator
from repository.customers_activity.local.generators.periods import PeriodsGenerator
from repository.customers_activity.local.tables_builder import TablesBuilder


# yapf: disable
class SqlServerFactory:

    def create_groups_repository(self, **kwargs) -> CustomersGroupsRepository:
        return CustomersGroupsRepository()

    def create_tracked_groups_repository(self, **kwargs) -> TrackedCustomersGroupsRepository:
        return TrackedCustomersGroupsRepository()

    def create_tags_repository(self, **kwargs) -> TicketsTagsRepository:
        return TicketsTagsRepository()

    def create_replies_types_repository(self, **kwargs) -> CATRepliesTypesRepository:
        return CATRepliesTypesRepository()

    def create_components_features_repository(self, **kwargs) -> CATComponentsFeaturesRepository:
        return CATComponentsFeaturesRepository()

    def create_customers_tickets_repository(self, **kwargs) -> CustomersTicketsRepository:
        return CustomersTicketsRepository()

    def create_license_statuses_repository(self, **kwargs) -> LicenseStatusesRepository:
        return LicenseStatusesRepository()

    def create_conversion_statuses_repository(self, **kwargs) -> ConversionStatusesRepository:
        return ConversionStatusesRepository()

    def create_platforms_products_repository(self, **kwargs) -> PlatformsProductsRepository:
        return PlatformsProductsRepository()

    def create_employees_iterations_repository(self, **kwargs)-> EmployeesIterationsRepository:
        return EmployeesIterationsRepository()

    def create_tickets_types_repository(self, **kwargs) -> TicketsTypesRepository:
        return TicketsTypesRepository()

    def create_frameworks_repository(self, **kwargs) -> FrameworksRepository:
        return FrameworksRepository()

    def create_operating_systems_repository(self, **kwargs) -> OperatingSystemsRepository:
        return OperatingSystemsRepository()

    def create_builds_repository(self, **kwargs) -> BuildsRepository:
        return BuildsRepository()

    def create_severity_repository(self, **kwargs) -> SeverityRepository:
        return SeverityRepository()

    def create_ticket_statuses_repository(self, **kwargs) -> TicketStatusesRepository:
        return TicketStatusesRepository()

    def create_ides_repository(self, **kwargs) -> IDEsRepository:
        return IDEsRepository()


class SqliteFactory:

    def create_tickets_with_iterations_period_repository(self, **kwargs) -> SqliteTicketsWithIterationsPeriodRepository:
        return SqliteTicketsWithIterationsPeriodRepository()

    def create_customers_groups_repository(self, **kwargs) -> SqliteCustomersGroupsRepository:
        return SqliteCustomersGroupsRepository()

    def create_tracked_customers_groups_repository(self, **kwargs) -> SqliteTrackedCustomersGroupsRepository:
        return SqliteTrackedCustomersGroupsRepository()

    def create_tickets_types_repository(self, **kwargs) -> SqliteTicketsTypesRepository:
        return SqliteTicketsTypesRepository()

    def create_tickets_tags_repository(self, **kwargs) -> SqliteTicketsTagsRepository:
        return SqliteTicketsTagsRepository()

    def create_reply_types_repository(self, **kwargs) -> SqliteReplyTypesRepository:
        return SqliteReplyTypesRepository()

    def create_frameworks_repository(self, **kwargs) -> SqliteFrameworksRepository:
        return SqliteFrameworksRepository()

    def create_operating_systems_repository(self, **kwargs) -> SqliteOperatingSystemsRepository:
        return SqliteOperatingSystemsRepository()

    def create_builds_repository(self, **kwargs) -> SqliteBuildsRepository:
        return SqliteBuildsRepository()

    def create_severity_repository(self, **kwargs) -> SqliteSeverityRepository:
        return SqliteSeverityRepository()

    def create_ticket_statuses_repository(self, **kwargs) -> SqliteTicketStatueseRepository:
        return SqliteTicketStatueseRepository()

    def create_ides_repository(self, **kwargs) -> SqliteIDEsRepository:
        return SqliteIDEsRepository()

    def create_license_statuses_repository(self, **kwargs) -> SqliteLicenseStatusesRepository:
        return SqliteLicenseStatusesRepository()

    def create_conversion_statuses_repository(self, **kwargs) -> SqliteConversionStatusesRepository:
        return SqliteConversionStatusesRepository()

    def create_platforms_repository(self, **kwargs) -> SqlitePlatformsRepository:
        return SqlitePlatformsRepository()

    def create_products_repository(self, **kwargs) -> SqliteProductsRepository:
        return SqliteProductsRepository()

    def create_components_repository(self, **kwargs) -> SqliteComponentsRepository:
        return SqliteComponentsRepository()

    def create_features_repository(self, **kwargs) -> SqliteFeaturesRepository:
        return SqliteFeaturesRepository()

    def create_tickets_with_iterations_raw_repository(self, **kwargs) -> SqliteTicketsWithIterationsRawRepository:
        return SqliteTicketsWithIterationsRawRepository()

    def create_tickets_with_iterations_aggregates_repository(self, **kwargs) -> SqliteTicketsWithIterationsAggregatesRepository:
        return SqliteTicketsWithIterationsAggregatesRepository()

    def create_emp_positions_repository(self, **kwargs) -> SqliteEmpPositionsRepository:
        return SqliteEmpPositionsRepository()

    def create_emp_tribes_repository(self, **kwargs) -> SqliteEmpTribesRepository:
        return SqliteEmpTribesRepository()

    def create_employees_repository(self, **kwargs) -> SqliteEmployeesRepository:
        return SqliteEmployeesRepository()

    def create_customers_repository(self, **kwargs) -> SqliteCustomersRepository:
        return SqliteCustomersRepository()

    def create_display_filter_generator(self, **kwargs) -> DisplayFilterGenerator:
        return DisplayFilterGenerator

    def create_periods_generator(self, **kwargs) -> PeriodsGenerator:
        return PeriodsGenerator
# yapf: enable


class CustomersActivityFactory:
    remote = SqlServerFactory()
    local = SqliteFactory()


class CustomersActivityTablesBuilderFactory:
    customers_activity = TablesBuilder()
