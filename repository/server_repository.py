from repository.factory import RepositoryFactory


# yapf: disable
def customers_activity_get_tickets_with_iterations_period() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_repository()
    return repository.get_period_json()

def customers_activity_get_customers_groups() -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_groups_repository()
    return repository.get_data_json()

def customers_activity_get_tickets_types() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_types_repository()
    return repository.get_data_json()

def customers_activity_get_tickets_tags() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_tags_repository()
    return repository.get_data_json()

def customers_activity_get_tickets_with_iterations_aggregates(
    group_by_period: str,
    range_start: str,
    range_end: str,
) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_aggregates_repository()
    return repository.get_data_json(
        group_by_period=group_by_period,
        range_start=range_start,
        range_end=range_end,
    )
# yapf: enable
