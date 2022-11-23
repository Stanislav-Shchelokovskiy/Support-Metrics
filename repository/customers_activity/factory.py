from toolbox.sql.base_repository import BaseRepository
from repository.customers_activity.remote.repository import (
    GroupsRepository,
    TagsRepository,
    TicketsWithIterationsRepository,
)
from repository.customers_activity.local.repository import (
    TicketsWithIterationsRepository as SqliteTicketsWithIterationsRepository,
)


class SqlServerFactory:

    def create_groups_repository(**kwargs) -> GroupsRepository:
        return GroupsRepository()

    def create_tags_repository(**kwargs) -> TagsRepository:
        return TagsRepository()

    def create_tickets_with_iterations_repository(**kwargs) -> TicketsWithIterationsRepository:
        return TicketsWithIterationsRepository()


class SqliteFactory:

    def create_TicketsWithIterationsRepository(*kwargs) -> SqliteTicketsWithIterationsRepository:
        return SqliteTicketsWithIterationsRepository()


class CustomersActivityFactory:
    remote = SqlServerFactory()
    local = SqliteFactory()
