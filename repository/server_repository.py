from repository.factory import RepositoryFactory


# yapf: disable
def customers_activity_get_group_by_periods() -> str:
    generator = RepositoryFactory.customers_activity.local.create_periods_generator()
    return generator.get_group_by_periods_json()


def customers_activity_get_tickets_with_iterations_period() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_period_repository()
    return repository.get_period_json()


def customers_activity_get_customers_groups() -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_groups_repository()
    return repository.get_data_json()

def customers_activity_get_tracked_customers_groups() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tracked_customers_groups_repository()
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


def customers_activity_get_frameworks() -> str:
    repository = RepositoryFactory.customers_activity.local.create_frameworks_repository()
    return repository.get_data_json()


def customers_activity_get_operating_systems() -> str:
    repository = RepositoryFactory.customers_activity.local.create_operating_systems_repository()
    return repository.get_data_json()


def customers_activity_get_builds() -> str:
    repository = RepositoryFactory.customers_activity.local.create_builds_repository()
    return repository.get_data_json()


def customers_activity_get_severity_values() -> str:
    repository = RepositoryFactory.customers_activity.local.create_severity_repository()
    return repository.get_data_json()


def customers_activity_get_ticket_statuses() -> str:
    repository = RepositoryFactory.customers_activity.local.create_ticket_statuses_repository()
    return repository.get_data_json()


def customers_activity_get_license_statuses() -> str:
    repository = RepositoryFactory.customers_activity.local.create_license_statuses_repository()
    return repository.get_data_json()


def customers_activity_get_conversion_statuses(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_conversion_statuses_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_platforms(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_platforms_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_products(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_products_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_components(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_components_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_features(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_features_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_emp_positions() -> str:
    repository = RepositoryFactory.customers_activity.local.create_emp_positions_repository()
    return repository.get_data_json()


def customers_activity_get_emp_tribes() -> str:
    repository = RepositoryFactory.customers_activity.local.create_emp_tribes_repository()
    return repository.get_data_json()


def customers_activity_get_employees(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_employees_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_customers(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_validate_customers(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_repository()
    return repository.validate_values(**kwargs)


def customers_activity_get_tickets_with_iterations_aggregates(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_aggregates_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_tickets_with_iterations_raw(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_raw_repository()
    return repository.get_data_json(**kwargs)


def customers_activity_get_display_filter(*args) -> str:
    generator = RepositoryFactory.customers_activity.local.create_display_filter_generator()
    return generator.generate_display_filter(*args)

def customers_activity_get_periods_array(**kwargs) -> str:
    generator = RepositoryFactory.customers_activity.local.create_periods_generator()
    return generator.generate_periods(**kwargs)
# yapf: enable
