from typing import Iterable
from sql_queries.index import CustomersActivityDBIndex
from sql_queries.customers_activity.meta import (
    CATComponentsFeaturesMeta,
    BaselineAlignedCustomersGroupsMeta,
    EmployeesIterationsMeta,
    PlatformsProductsMeta,
    TicketsWithPropertiesMeta,
)


def _create_index_statement(tbl: str, cols: Iterable[str]) -> str:
    return f'CREATE INDEX idx_{tbl}_{"_".join(cols)} ON {tbl}({",".join(cols)});'


# yapf: disable
def get_create_index_statements() -> dict[str, tuple[str]]:
    return __create_index_statements

__create_index_statements = {
        CustomersActivityDBIndex.get_customers_tickets_name():
            (
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_customers_tickets_name(),
                    cols=(
                        TicketsWithPropertiesMeta.user_crmid,
                        TicketsWithPropertiesMeta.creation_date,
                    )
                ),
            ),
        CustomersActivityDBIndex.get_employees_iterations_name():
            (
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_employees_iterations_name(),
                    cols=(EmployeesIterationsMeta.ticket_id,)
                ),
            ),
        CustomersActivityDBIndex.get_cat_components_features_name():
            (
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_cat_components_features_name(),
                    cols=(
                        CATComponentsFeaturesMeta.tribe_id,
                        CATComponentsFeaturesMeta.component_id,
                        CATComponentsFeaturesMeta.component_name,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_cat_components_features_name(),
                    cols=(
                        CATComponentsFeaturesMeta.tribe_id,
                        CATComponentsFeaturesMeta.component_id,
                        CATComponentsFeaturesMeta.feature_id,
                        CATComponentsFeaturesMeta.feature_name,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_cat_components_features_name(),
                    cols=(
                        CATComponentsFeaturesMeta.component_id,
                        CATComponentsFeaturesMeta.component_name,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_cat_components_features_name(),
                    cols=(
                        CATComponentsFeaturesMeta.feature_id,
                        CATComponentsFeaturesMeta.feature_name,
                    )
                ),
            ),
        CustomersActivityDBIndex.get_platforms_products_name():
            (
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_platforms_products_name(),
                    cols=(
                        PlatformsProductsMeta.product_tribe_id,
                        PlatformsProductsMeta.product_id,
                        PlatformsProductsMeta.product_name,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_platforms_products_name(),
                    cols=(
                        PlatformsProductsMeta.platform_tribe_id,
                        PlatformsProductsMeta.platform_id,
                        PlatformsProductsMeta.platform_name,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_platforms_products_name(),
                    cols=(
                        PlatformsProductsMeta.platform_id,
                        PlatformsProductsMeta.platform_name,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_platforms_products_name(),
                    cols=(
                        PlatformsProductsMeta.product_id,
                        PlatformsProductsMeta.product_name,
                    )
                ),
            ),
        CustomersActivityDBIndex.get_tracked_customers_groups_name():
            (
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_tracked_customers_groups_name(),
                    cols=(
                        BaselineAlignedCustomersGroupsMeta.assignment_date,
                        BaselineAlignedCustomersGroupsMeta.id,
                        BaselineAlignedCustomersGroupsMeta.user_crmid,
                        BaselineAlignedCustomersGroupsMeta.removal_date,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_tracked_customers_groups_name(),
                    cols=(
                        BaselineAlignedCustomersGroupsMeta.user_crmid,
                        BaselineAlignedCustomersGroupsMeta.assignment_date,
                        BaselineAlignedCustomersGroupsMeta.id,
                    )
                ),
                _create_index_statement(
                    tbl=CustomersActivityDBIndex.get_tracked_customers_groups_name(),
                    cols=(
                        BaselineAlignedCustomersGroupsMeta.id,
                        BaselineAlignedCustomersGroupsMeta.name,
                    )
                ),
            ),
    }
