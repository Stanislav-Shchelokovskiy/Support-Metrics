from repository.customers_activity.factory import (
    CustomersActivityFactory,
    CustomersActivityTablesBuilderFactory,
)


class RepositoryFactory:
    customers_activity = CustomersActivityFactory


class TablesBuilder:
    customers_activity = CustomersActivityTablesBuilderFactory
