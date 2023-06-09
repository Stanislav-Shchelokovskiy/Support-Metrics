from collections.abc import Iterable, Callable, Mapping
from toolbox.sql.aggs import Metric, COUNT_DISTINCT, COUNT, none_metric
from sql_queries.meta import TicketsWithIterationsMeta


people = Metric(
    'People',
    COUNT_DISTINCT(TicketsWithIterationsMeta.user_id),
)
tickets = Metric(
    'Tickets',
    COUNT_DISTINCT(TicketsWithIterationsMeta.ticket_scid),
)
iterations = Metric(
    'Iterations',
    COUNT(TicketsWithIterationsMeta.emp_post_id),
)
iterations_to_tickets = Metric.from_metric('Iterations / Tickets', iterations / tickets)


metrics = {
    people.name: people,
    tickets.name: tickets,
    iterations.name: iterations,
    iterations_to_tickets.name: iterations_to_tickets,
}


def get_metric(metric: str) -> Metric:
    return get_metrics().get(metric, none_metric)


def get_metrics_names(formatter: Callable[[Metric], str] = lambda x: x.name) -> Iterable:
    return [formatter(x) for x in get_metrics().values()]


def get_metrics() -> Mapping[str, Metric]:
    return metrics
