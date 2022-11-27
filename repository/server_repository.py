from toolbox.utils.converters import DF_to_JSON
from repository.factory import RepositoryFactory


# yapf: disable
def customers_activity_get_tickets_with_iterations_period() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_repository()
    return repository.get_period()

def customers_activity_get_customers_groups() -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_groups_repository()
    return DF_to_JSON.convert(repository.get_data())

def customers_activity_get_tickets_types() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_types_repository()
    return DF_to_JSON.convert(repository.get_data())
# yapf: enable