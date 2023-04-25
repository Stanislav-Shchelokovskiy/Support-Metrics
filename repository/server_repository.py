from repository.factory import RepositoryFactory


# yapf: disable
async def customers_activity_get_group_by_periods() -> str:
    generator = RepositoryFactory.customers_activity.local.create_periods_generator()
    return await generator.get_group_by_periods_json()


async def customers_activity_get_tickets_with_iterations_period() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_period_repository()
    return await repository.get_data()


async def customers_activity_get_customers_groups() -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_groups_repository()
    return await repository.get_data()


async def customers_activity_get_tracked_customers_groups() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tracked_customers_groups_repository()
    return await repository.get_data()


async def customers_activity_get_tickets_types() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_types_repository()
    return await repository.get_data()


async def customers_activity_get_tickets_tags() -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_tags_repository()
    return await repository.get_data()


async def customers_activity_get_replies_types() -> str:
    repository = RepositoryFactory.customers_activity.local.create_reply_types_repository()
    return await repository.get_data()


async def customers_activity_get_frameworks() -> str:
    repository = RepositoryFactory.customers_activity.local.create_frameworks_repository()
    return await repository.get_data()


async def customers_activity_get_operating_systems() -> str:
    repository = RepositoryFactory.customers_activity.local.create_operating_systems_repository()
    return await repository.get_data()


async def customers_activity_get_builds() -> str:
    repository = RepositoryFactory.customers_activity.local.create_builds_repository()
    return await repository.get_data()


async def customers_activity_get_severity_values() -> str:
    repository = RepositoryFactory.customers_activity.local.create_severity_repository()
    return await repository.get_data()


async def customers_activity_get_ticket_statuses() -> str:
    repository = RepositoryFactory.customers_activity.local.create_ticket_statuses_repository()
    return await repository.get_data()


async def customers_activity_get_ides() -> str:
    repository = RepositoryFactory.customers_activity.local.create_ides_repository()
    return await repository.get_data()


async def customers_activity_get_license_statuses() -> str:
    repository = RepositoryFactory.customers_activity.local.create_license_statuses_repository()
    return await repository.get_data()


async def customers_activity_get_conversion_statuses(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_conversion_statuses_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_platforms(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_platforms_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_products(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_products_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_components(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_components_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_features(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_features_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_emp_positions() -> str:
    repository = RepositoryFactory.customers_activity.local.create_emp_positions_repository()
    return await repository.get_data()


async def customers_activity_get_emp_tribes() -> str:
    repository = RepositoryFactory.customers_activity.local.create_emp_tribes_repository()
    return await repository.get_data()


async def customers_activity_get_emp_tents() -> str:
    repository = RepositoryFactory.customers_activity.local.create_emp_tents_repository()
    return await repository.get_data()


async def customers_activity_get_employees(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_employees_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_customers(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_validate_customers(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_customers_validation_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_tickets_with_iterations_aggregates(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_aggregates_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_tickets_with_iterations_raw(**kwargs) -> str:
    repository = RepositoryFactory.customers_activity.local.create_tickets_with_iterations_raw_repository()
    return await repository.get_data(**kwargs)


async def customers_activity_get_display_filter(*args) -> str:
    generator = RepositoryFactory.customers_activity.local.create_display_filter_generator()
    return await generator.generate_display_filter(*args)


async def customers_activity_get_periods_array(**kwargs) -> str:
    generator = RepositoryFactory.customers_activity.local.create_periods_generator()
    return await generator.generate_periods(**kwargs)
# yapf: enable
