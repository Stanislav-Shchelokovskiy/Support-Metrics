from toolbox.sql.base_repository import BaseRepository
from repository.customers_activity.repository import (
    GroupsRepository,
    TagsRepository,
    TicketsWithIterationsRepository,
)


class CustomersActivityFactory:

    def create_groups_repository(**kwargs) -> BaseRepository:
        return GroupsRepository()

    def create_tags_repository(**kwargs) -> BaseRepository:
        return TagsRepository()

    def create_tickets_with_iterations_repository(**kwargs) -> BaseRepository:
        return TicketsWithIterationsRepository()
