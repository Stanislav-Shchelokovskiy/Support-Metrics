from repository.customers_activity.remote.repository import (
    GroupsRepository,
    TagsRepository,
    TicketsWithIterationsRepository,
    TicketsTypesRepository,
    RepliesTypesRepository,
    ComponentsFeaturesRepository,
    LicenseStatusesRepository,
)
from repository.customers_activity.local.repository import (
    TicketsWithIterationsRepository as SqliteTicketsWithIterationsRepository,
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

    def create_tickets_types_repository(self, **kwargs) -> TicketsTypesRepository:
        return TicketsTypesRepository()

    def create_license_statuses_repository(self, **kwargs) -> LicenseStatusesRepository:
        return LicenseStatusesRepository()


class SqliteFactory:

    def create_tickets_with_iterations_repository(self, **kwargs) -> SqliteTicketsWithIterationsRepository:
        return SqliteTicketsWithIterationsRepository()

    def create_customers_groups_repository(self, **kwargs) -> SqliteCustomersGroupsRepository:
        return SqliteCustomersGroupsRepository()

    def create_tickets_types_repository(self, **kwargs) -> SqliteTicketsTypesRepository:
        return SqliteTicketsTypesRepository()

    def create_tickets_tags_repository(self, **kwargs) -> SqliteTicketsTagsRepository:
        return SqliteTicketsTagsRepository()

    def create_reply_types_repository(self, **kwargs) -> SqliteReplyTypesRepository:
        return SqliteReplyTypesRepository()

    def create_components_repository(self, **kwargs) -> SqliteComponentsRepository:
        return SqliteComponentsRepository()

    def create_features_repository(self, **kwargs) -> SqliteFeaturesRepository:
        return SqliteFeaturesRepository()

    def create_tickets_with_iterations_raw_repository(self, **kwargs) -> SqliteTicketsWithIterationsRawRepository:
        return SqliteTicketsWithIterationsRawRepository()

    def create_tickets_with_iterations_aggregates_repository(self, **kwargs) -> SqliteTicketsWithIterationsAggregatesRepository:
        return SqliteTicketsWithIterationsAggregatesRepository()

    def create_license_statuses_repository(self, **kwargs) ->SqliteLicenseStatusesRepository:
        return SqliteLicenseStatusesRepository()
# yapf: enable


class CustomersActivityFactory:
    remote = SqlServerFactory()
    local = SqliteFactory()
