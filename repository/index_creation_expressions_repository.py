from sql_queries.index import CustomersActivityDBIndex
from sql_queries.customers_activity.meta import (
    ComponentsFeaturesMeta,
    TrackedCustomersGroupsMeta,
    EmployeesIterationsMeta,
    PlatformsProductsMeta,
)


def _create_index_expression(tbl: str, cols: list[str]) -> str:
    return f'CREATE INDEX idx_{tbl}_{cols[0]} ON {tbl}({",".join(cols)});'


class IndexCreationExpressionsRepository:
    customers_activity_create_index_expressions = {
        CustomersActivityDBIndex.get_components_features_name():
            [
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_components_features_name(
                    ),
                    cols=[
                        ComponentsFeaturesMeta.tribe_id,
                        ComponentsFeaturesMeta.component_id,
                        ComponentsFeaturesMeta.feature_id,
                    ]
                ),
            ],
        CustomersActivityDBIndex.get_platforms_products_name():
            [
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_platforms_products_name(),
                    cols=[
                        PlatformsProductsMeta.tribe_id,
                        PlatformsProductsMeta.platform_id,
                        PlatformsProductsMeta.product_id,
                    ]
                ),
            ],
        CustomersActivityDBIndex.get_employees_iterations_name():
            [
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_employees_iterations_name(),
                    cols=[EmployeesIterationsMeta.ticket_id]
                ),
            ],
        CustomersActivityDBIndex.get_tracked_customers_groups_name():
            [
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_tracked_customers_groups_name(),
                    cols=[
                        TrackedCustomersGroupsMeta.user_crmid,
                        TrackedCustomersGroupsMeta.id,
                    ]
                ),
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_tracked_customers_groups_name(),
                    cols=[
                        TrackedCustomersGroupsMeta.id,
                        TrackedCustomersGroupsMeta.name,
                    ]
                ),
            ],
    }
