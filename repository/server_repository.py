import repository.factory as RepositoryFactory


# yapf: disable
async def get_group_by_periods() -> str:
    generator = RepositoryFactory.local.create_periods_generator()
    return await generator.get_group_by_periods_json()


async def get_tickets_with_iterations_period() -> str:
    repository = RepositoryFactory.local.create_tickets_with_iterations_period_repository()
    return await repository.get_data()


async def get_customers_groups() -> str:
    repository = RepositoryFactory.local.create_customers_groups_repository()
    return await repository.get_data()


async def get_tracked_customers_groups() -> str:
    repository = RepositoryFactory.local.create_tracked_customers_groups_repository()
    return await repository.get_data()


async def get_tickets_types() -> str:
    repository = RepositoryFactory.local.create_tickets_types_repository()
    return await repository.get_data()


async def get_tickets_tags() -> str:
    repository = RepositoryFactory.local.create_tickets_tags_repository()
    return await repository.get_data()


async def get_cat_replies_types() -> str:
    repository = RepositoryFactory.local.create_reply_types_repository()
    return await repository.get_data()


async def get_frameworks() -> str:
    repository = RepositoryFactory.local.create_frameworks_repository()
    return await repository.get_data()


async def get_operating_systems() -> str:
    repository = RepositoryFactory.local.create_operating_systems_repository()
    return await repository.get_data()


async def get_builds() -> str:
    repository = RepositoryFactory.local.create_builds_repository()
    return await repository.get_data()


async def get_severity_values() -> str:
    repository = RepositoryFactory.local.create_severity_repository()
    return await repository.get_data()


async def get_ticket_statuses() -> str:
    repository = RepositoryFactory.local.create_ticket_statuses_repository()
    return await repository.get_data()


async def get_ides() -> str:
    repository = RepositoryFactory.local.create_ides_repository()
    return await repository.get_data()


async def get_license_statuses() -> str:
    repository = RepositoryFactory.local.create_license_statuses_repository()
    return await repository.get_data()


async def get_conversion_statuses(**kwargs) -> str:
    repository = RepositoryFactory.local.create_conversion_statuses_repository()
    return await repository.get_data(**kwargs)


async def get_platforms(**kwargs) -> str:
    repository = RepositoryFactory.local.create_platforms_repository()
    return await repository.get_data(**kwargs)


async def get_products(**kwargs) -> str:
    repository = RepositoryFactory.local.create_products_repository()
    return await repository.get_data(**kwargs)


async def get_cat_components(**kwargs) -> str:
    repository = RepositoryFactory.local.create_components_repository()
    return await repository.get_data(**kwargs)


async def get_cat_features(**kwargs) -> str:
    repository = RepositoryFactory.local.create_features_repository()
    return await repository.get_data(**kwargs)


async def get_emp_positions() -> str:
    repository = RepositoryFactory.local.create_emp_positions_repository()
    return await repository.get_data()


async def get_emp_tribes() -> str:
    repository = RepositoryFactory.local.create_emp_tribes_repository()
    return await repository.get_data()


async def get_emp_tents() -> str:
    repository = RepositoryFactory.local.create_emp_tents_repository()
    return await repository.get_data()


async def get_employees(**kwargs) -> str:
    repository = RepositoryFactory.local.create_employees_repository()
    return await repository.get_data(**kwargs)


async def get_customers(**kwargs) -> str:
    repository = RepositoryFactory.local.create_customers_repository()
    return await repository.get_data(**kwargs)


async def validate_customers(**kwargs) -> str:
    repository = RepositoryFactory.local.create_customers_validation_repository()
    return await repository.get_data(**kwargs)


async def get_tickets_with_iterations_aggregates(**kwargs) -> str:
    repository = RepositoryFactory.local.create_tickets_with_iterations_aggregates_repository()
    return await repository.get_data(**kwargs)


async def get_tickets_with_iterations_raw(**kwargs) -> str:
    repository = RepositoryFactory.local.create_tickets_with_iterations_raw_repository()
    return await repository.get_data(**kwargs)


async def get_display_filter(*args) -> str:
    generator = RepositoryFactory.local.create_display_filter_generator()
    return await generator.generate_display_filter(*args)


async def get_periods_array(**kwargs) -> str:
    generator = RepositoryFactory.local.create_periods_generator()
    return await generator.generate_periods(**kwargs)
# yapf: enable
