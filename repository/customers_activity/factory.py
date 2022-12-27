from repository.customers_activity.remote.repository import (
    GroupsRepository,
    TagsRepository,
    TicketsWithIterationsRepository,
    RepliesTypesRepository,
    ComponentsFeaturesRepository,
    LicenseStatusesRepository,
    ConversionStatusesRepository,
    PlatformsProductsRepository,
    EmployeesIterationsRepository,
)
from repository.customers_activity.local.repository import (
    TicketsWithIterationsPeriodRepository as
    SqliteTicketsWithIterationsPeriodRepository,
    CustomersGroupsRepository as SqliteCustomersGroupsRepository,
    TicketsTypesRepository as SqliteTicketsTypesRepository,
    TicketsTagsRepository as SqliteTicketsTagsRepository,
    TicketsWithIterationsRawRepository as
    SqliteTicketsWithIterationsRawRepository,
    TicketsWithIterationsAggregatesRepository as
    SqliteTicketsWithIterationsAggregatesRepository,
    ReplyTypesRepository as SqliteReplyTypesRepository,
    ComponentsRepository as SqliteComponentsRepository,
    FeaturesRepository as SqliteFeaturesRepository,
    LicenseStatusesRepository as SqliteLicenseStatusesRepository,
    ConversionStatusesRepository as SqliteConversionStatusesRepository,
    PlatformsRepository as SqlitePlatformsRepository,
    ProductsRepository as SqliteProductsRepository,
    PositionsRepository as SqlitePositionsRepository,
)


# yapf: disable
class SqlServerFactory:

    def create_groups_repository(self, **kwargs) -> GroupsRepository:
        return GroupsRepository()

    def create_tags_repository(self, **kwargs) -> TagsRepository:
        return TagsRepository()

    def create_replies_types_repository(self, **kwargs) -> RepliesTypesRepository:
        return RepliesTypesRepository()

    def create_components_features_repository(self, **kwargs) -> ComponentsFeaturesRepository:
        return ComponentsFeaturesRepository()

    def create_tickets_with_iterations_repository(self, **kwargs) -> TicketsWithIterationsRepository:
        return TicketsWithIterationsRepository()

    def create_license_statuses_repository(self, **kwargs) -> LicenseStatusesRepository:
        return LicenseStatusesRepository()

    def create_conversion_statuses_repository(self, **kwargs) -> ConversionStatusesRepository:
        return ConversionStatusesRepository()

    def create_platforms_products_repository(self, **kwargs) -> PlatformsProductsRepository:
        return PlatformsProductsRepository()

    def create_employees_iterations_repository(self, **kwargs)-> EmployeesIterationsRepository:
        return EmployeesIterationsRepository()


class SqliteFactory:

    def create_tickets_with_iterations_period_repository(self, **kwargs) -> SqliteTicketsWithIterationsPeriodRepository:
        return SqliteTicketsWithIterationsPeriodRepository()

    def create_customers_groups_repository(self, **kwargs) -> SqliteCustomersGroupsRepository:
        return SqliteCustomersGroupsRepository()

    def create_tickets_types_repository(self, **kwargs) -> SqliteTicketsTypesRepository:
        return SqliteTicketsTypesRepository()

    def create_tickets_tags_repository(self, **kwargs) -> SqliteTicketsTagsRepository:
        return SqliteTicketsTagsRepository()

    def create_reply_types_repository(self, **kwargs) -> SqliteReplyTypesRepository:
        return SqliteReplyTypesRepository()

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

    def create_positions_repository(self, **kwargs) -> SqlitePositionsRepository:
        return SqlitePositionsRepository()
# yapf: enable


class CustomersActivityFactory:
    remote = SqlServerFactory()
    local = SqliteFactory()
