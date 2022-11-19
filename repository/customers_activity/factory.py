from toolbox.sql.base_repository import BaseRepository
from repository.customers_activity.groups_repository import GroupsRepository
from repository.customers_activity.tags_repository import TagsRepository
from repository.customers_activity.tickets_with_iterations_repository import TicketsWithIterationsRepository


class CustomersActivityFactory:

    def create_groups_repository(**kwargs) -> BaseRepository:
        return GroupsRepository()

    def create_tags_repository(**kwargs) -> BaseRepository:
        return TagsRepository()

    def create_tickets_with_iterations_repository(**kwargs) -> BaseRepository:
        return TicketsWithIterationsRepository()
