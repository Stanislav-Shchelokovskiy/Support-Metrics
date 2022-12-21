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

def customers_activity_get_replies_types() -> str:
    repository = RepositoryFactory.customers_activity.local.create_reply_types_repository()
    return repository.get_data_json()

def customers_activity_get_components(tribe_ids: list[str]) -> str:
    repository = RepositoryFactory.customers_activity.local.create_components_repository()
    return repository.get_data_json(tribe_ids=tribe_ids,)

def customers_activity_get_features(tribe_ids: list[str], component_ids: list[str],) -> str:
    repository = RepositoryFactory.customers_activity.local.create_features_repository()
    return repository.get_data_json(
            tribe_ids=tribe_ids,
            component_ids=component_ids,
        )

def customers_activity_get_group_by_periods() -> str:
    # format should contain a valid strftime string.
    # https://sqlite.org/lang_datefunc.html
    return '''[
        { "name": "Day",        "format": "%Y-%m-%d" },
        { "name": "Week-Year",  "format": "%Y-%W" },
        { "name": "Month-Year", "format": "%Y-%m" },
        { "name": "Year",       "format": "%Y" }
    ]
    '''

def customers_activity_get_license_statuses() -> str:
    repository = RepositoryFactory.customers_activity.local.create_license_statuses_repository()
    return repository.get_data_json()

def customers_activity_get_conversion_statuses(license_status_ids: list[int]) -> str:
    repository = RepositoryFactory.customers_activity.local.create_conversion_statuses_repository()
    return repository.get_data_json(license_status_ids=license_status_ids)

def customers_activity_get_tickets_with_iterations_aggregates(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_aggregates_repository()
    return repository.get_data_json(**kwargs)

def customers_activity_get_tickets_with_iterations_raw(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_raw_repository()
    return repository.get_data_json(**kwargs)
# yapf: enable
