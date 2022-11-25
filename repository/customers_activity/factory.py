from toolbox.sql.base_repository import BaseRepository
from repository.customers_activity.remote.repository import (
    GroupsRepository,
    TagsRepository,
    TicketsWithIterationsRepository,
)
from repository.customers_activity.local.repository import (
    TicketsWithIterationsRepository as SqliteTicketsWithIterationsRepository,
    CustomersGroupsRepository as SqliteCustomersGroupsRepository,
)


class SqlServerFactory:

    def create_groups_repository(self, **kwargs) -> GroupsRepository:
        return GroupsRepository()

    def create_tags_repository(self, **kwargs) -> TagsRepository:
        return TagsRepository()

    def create_tickets_with_iterations_repository(self, **kwargs) -> TicketsWithIterationsRepository:
        return TicketsWithIterationsRepository()


class SqliteFactory:

    def create_tickets_with_iterations_repository(self, **kwargs) -> SqliteTicketsWithIterationsRepository:
        return SqliteTicketsWithIterationsRepository()
    
    def create_customers_groups_repository(self, **kwargs) -> SqliteCustomersGroupsRepository:
        return SqliteCustomersGroupsRepository()


class CustomersActivityFactory:
    remote = SqlServerFactory()
    local = SqliteFactory()
