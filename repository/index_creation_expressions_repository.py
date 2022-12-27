from sql_queries.index import CustomersActivityDBIndex
from sql_queries.customers_activity.meta import (
    ComponentsFeaturesMeta,
    TicketsWithIterationsMeta,
    EmployeesIterations,
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
                        ComponentsFeaturesMeta.feature_id
                    ]
                ),
            ],
        CustomersActivityDBIndex.get_tickets_with_iterations_name():
            [
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.
                    get_tickets_with_iterations_name(),
                    cols=[
                        TicketsWithIterationsMeta.creation_date,
                        TicketsWithIterationsMeta.tribe_id,
                    ]
                ),
            ],
        CustomersActivityDBIndex.get_employees_iterations_name():
            [
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_employees_iterations_name(
                    ),
                    cols=[
                        EmployeesIterations.ticket_id,
                        EmployeesIterations.pos_id,
                    ]
                ),
                _create_index_expression(
                    tbl=CustomersActivityDBIndex.get_employees_iterations_name(
                    ),
                    cols=[
                        EmployeesIterations.pos_id,
                        EmployeesIterations.pos_name,
                    ]
                ),
            ],
    }
