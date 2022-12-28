from repository.customers_activity.factory import (
    CustomersActivityFactory,
    TablesBuilder as InnerTablesBuilder,
)


class RepositoryFactory:
    customers_activity = CustomersActivityFactory


class TablesBuilder:
    customers_activity = InnerTablesBuilder()
