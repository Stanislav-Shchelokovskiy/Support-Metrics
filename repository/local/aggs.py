from collections.abc import Callable, Mapping
from toolbox.sql.aggs import Metric, COUNT_DISTINCT, COUNT, NONE_METRIC
from sql_queries.meta import TicketsWithIterationsMeta


people = Metric(
    'People',
    'Activity',
    COUNT_DISTINCT(TicketsWithIterationsMeta.user_id),
)
tickets = Metric(
    'Tickets',
    'Activity',
    COUNT_DISTINCT(TicketsWithIterationsMeta.ticket_scid),
)
iterations = Metric(
    'Iterations',
    'Activity',
    COUNT(TicketsWithIterationsMeta.emp_post_id),
)
iterations_to_tickets = Metric.from_metric(
    'Iterations / Tickets',
    'Activity',
    iterations / tickets,
)

metrics = {
    people.name: people,
    tickets.name: tickets,
    iterations.name: iterations,
    iterations_to_tickets.name: iterations_to_tickets,
}


def get_metric(metric: str) -> Metric:
    return get_metrics().get(metric, NONE_METRIC)


def get_metrics_projections(
    projector: Callable[[Metric], str] = lambda x: x.name
) -> list[str]:
    return [projector(x) for x in get_metrics().values()]


def get_metrics() -> Mapping[str, Metric]:
    return metrics
