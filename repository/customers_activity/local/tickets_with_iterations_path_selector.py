from repository.customers_activity.local.sql_query_params_generator import FilterParametersNode
from sql_queries.index import CustomersActivitySqlPathIndex


def canUseSimpleQuery(kwargs: dict) -> bool:
    positions_node: FilterParametersNode = kwargs['positions_ids']
    return positions_node.include and len(positions_node.values) == 0


def select_tickets_with_iterations_raw_path(kwargs: dict) -> str:
    if (canUseSimpleQuery(kwargs)):
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path()
    return 'to do'


def select_tickets_with_iterations_aggregates_path(kwargs: dict) -> str:
    if (canUseSimpleQuery(kwargs)):
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_aggregates_path()
    return 'to do'
