from repository.customers_activity.remote.repository import (
    GroupsRepository,
    TagsRepository,
    TicketsWithIterationsRepository,
    TicketsTypesRepository,
    ReplyTypesRepository,
    ControlsFeaturesRepository,
)
from repository.customers_activity.local.repository import (
    TicketsWithIterationsRepository as SqliteTicketsWithIterationsRepository,
    CustomersGroupsRepository as SqliteCustomersGroupsRepository,
    TicketsTypesRepository as SqliteTicketsTypesRepository,
    TicketsTagsRepository as SqliteTicketsTagsRepository,
    TicketsWithIterationsAggregatesRepository as SqliteTicketsWithIterationsAggregatesRepository,
    ReplyTypesRepository as SqliteReplyTypesRepository,
)


class SqlServerFactory:

    def create_groups_repository(self, **kwargs) -> GroupsRepository:
        return GroupsRepository()

    def create_tags_repository(self, **kwargs) -> TagsRepository:
        return TagsRepository()

    def create_reply_types_repository(self, **kwargs) -> ReplyTypesRepository:
        return ReplyTypesRepository()

    def create_controls_features_repository(self, **kwargs) -> ControlsFeaturesRepository:
        return ControlsFeaturesRepository()

    def create_tickets_with_iterations_repository(self, **kwargs) -> TicketsWithIterationsRepository:
        return TicketsWithIterationsRepository()

    def create_tickets_types_repository(self, **kwargs) -> TicketsTypesRepository:
        return TicketsTypesRepository()


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
    
    def create_tickets_with_iterations_aggregates_repository(self, **kwargs) -> SqliteTicketsWithIterationsAggregatesRepository:
        return SqliteTicketsWithIterationsAggregatesRepository()


class CustomersActivityFactory:
    remote = SqlServerFactory()
    local = SqliteFactory()
