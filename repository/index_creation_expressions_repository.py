from sql_queries.index import CustomersActivityDBIndex
from sql_queries.customers_activity.meta import (
    ComponentsFeaturesMeta,
    TicketsWithIterationsMeta,
)


def _create_index_expression(tbl: str, col: str) -> str:
    return f'CREATE INDEX idx_{col} ON {tbl}({col});'


class IndexCreationExpressionsRepository:
    customers_activity_create_index_expressions = {
        CustomersActivityDBIndex.get_components_features_name():
            _create_index_expression(
                tbl=CustomersActivityDBIndex.get_components_features_name(),
                col=ComponentsFeaturesMeta.tribe_id
            ),
        CustomersActivityDBIndex.get_tickets_with_iterations_name():
            _create_index_expression(
                tbl=CustomersActivityDBIndex.get_tickets_with_iterations_name(),
                col=TicketsWithIterationsMeta.creation_date
            ),
    }
