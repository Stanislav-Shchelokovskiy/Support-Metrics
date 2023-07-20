from typing import Iterable
from sql_queries.meta import (
    CATComponentsFeaturesMeta,
    BaselineAlignedCustomersGroupsMeta,
    EmployeesIterationsMeta,
    PlatformsProductsMeta,
    TicketsWithPropertiesMeta,
)
import sql_queries.index.db as DbIndex


def _create_index_statement(tbl: str, cols: Iterable[str]) -> str:
    return f'CREATE INDEX idx_{tbl}_{"_".join(cols)} ON {tbl}({",".join(cols)});'


# yapf: disable
def get_create_index_statements() -> dict[str, tuple[str]]:
    return __create_index_statements

__create_index_statements = {
        DbIndex.customers_tickets:
            (
                _create_index_statement(
                    tbl=DbIndex.customers_tickets,
                    cols=(
                        TicketsWithPropertiesMeta.user_crmid,
                        TicketsWithPropertiesMeta.creation_date,
                    )
                ),
            ),
        DbIndex.employees_iterations:
            (
                _create_index_statement(
                    tbl=DbIndex.employees_iterations,
                    cols=(EmployeesIterationsMeta.ticket_id,)
                ),
            ),
        DbIndex.cat_components_features:
            (
                _create_index_statement(
                    tbl=DbIndex.cat_components_features,
                    cols=(
                        CATComponentsFeaturesMeta.tent_id,
                        CATComponentsFeaturesMeta.component_id,
                        CATComponentsFeaturesMeta.component_name,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.cat_components_features,
                    cols=(
                        CATComponentsFeaturesMeta.tent_id,
                        CATComponentsFeaturesMeta.component_id,
                        CATComponentsFeaturesMeta.feature_id,
                        CATComponentsFeaturesMeta.feature_name,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.cat_components_features,
                    cols=(
                        CATComponentsFeaturesMeta.component_id,
                        CATComponentsFeaturesMeta.component_name,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.cat_components_features,
                    cols=(
                        CATComponentsFeaturesMeta.feature_id,
                        CATComponentsFeaturesMeta.feature_name,
                    )
                ),
            ),
        DbIndex.platforms_products:
            (
                _create_index_statement(
                    tbl=DbIndex.platforms_products,
                    cols=(
                        PlatformsProductsMeta.product_tent_id,
                        PlatformsProductsMeta.product_id,
                        PlatformsProductsMeta.product_name,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.platforms_products,
                    cols=(
                        PlatformsProductsMeta.platform_tent_id,
                        PlatformsProductsMeta.platform_id,
                        PlatformsProductsMeta.platform_name,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.platforms_products,
                    cols=(
                        PlatformsProductsMeta.platform_id,
                        PlatformsProductsMeta.platform_name,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.platforms_products,
                    cols=(
                        PlatformsProductsMeta.product_id,
                        PlatformsProductsMeta.product_name,
                    )
                ),
            ),
        DbIndex.tracked_customers_groups:
            (
                _create_index_statement(
                    tbl=DbIndex.tracked_customers_groups,
                    cols=(
                        BaselineAlignedCustomersGroupsMeta.assignment_date,
                        BaselineAlignedCustomersGroupsMeta.id,
                        BaselineAlignedCustomersGroupsMeta.user_crmid,
                        BaselineAlignedCustomersGroupsMeta.removal_date,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.tracked_customers_groups,
                    cols=(
                        BaselineAlignedCustomersGroupsMeta.user_crmid,
                        BaselineAlignedCustomersGroupsMeta.assignment_date,
                        BaselineAlignedCustomersGroupsMeta.id,
                    )
                ),
                _create_index_statement(
                    tbl=DbIndex.tracked_customers_groups,
                    cols=(
                        BaselineAlignedCustomersGroupsMeta.id,
                        BaselineAlignedCustomersGroupsMeta.name,
                    )
                ),
            ),
    }
