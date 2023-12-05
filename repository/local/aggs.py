from collections.abc import Callable, Mapping
from toolbox.sql.aggs import Metric, COUNT_DISTINCT, COUNT, SUM, NONE_METRIC
from sql_queries.meta.aggs import TicketsWithIterations, CSI

people = Metric(
    'People',
    '',
    'Entities',
    COUNT_DISTINCT(TicketsWithIterations.user_id),
)
tickets = Metric(
    'Tickets',
    '',
    'Entities',
    COUNT_DISTINCT(TicketsWithIterations.ticket_scid),
)
iterations = Metric(
    'Iterations',
    'Replies',
    'Entities',
    COUNT(TicketsWithIterations.emp_post_id),
)

iterations_to_tickets = Metric.from_metric(
    'Iterations / Tickets',
    'Replies Rate',
    'Productivity',
    iterations / tickets,
)

csi = Metric(
    'Satisfaction Index',
    'Customer Satisfaction Index',
    'Customers',
    SUM(f'IIF({CSI.rating} = 1, 1, 0)') / COUNT('*') * 100,
)

metrics = {
    iterations.name: iterations,
    people.name: people,
    tickets.name: tickets,
    iterations_to_tickets.name: iterations_to_tickets,
    csi.name: csi,
}


def get_metric(metric: str) -> Metric:
    return get_metrics().get(metric, NONE_METRIC)


def select_metrics(
    projector: Callable[[Metric], str] = lambda x: x,
) -> list[str]:
    return [projector(x) for x in get_metrics().values()]


def get_metrics() -> Mapping[str, Metric]:
    return metrics


def is_csi(name: str) -> bool:
    return name == csi.name
