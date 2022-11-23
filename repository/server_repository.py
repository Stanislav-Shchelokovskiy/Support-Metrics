from repository.factory import RepositoryFactory


def customers_activity_get_tickets_with_iterations_period() -> str:
    repository = RepositoryFactory.customers_activity.local.create_TicketsWithIterationsRepository()
    return repository.get_period()
