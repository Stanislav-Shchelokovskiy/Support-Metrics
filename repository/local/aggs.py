from collections.abc import Iterable, Callable, Mapping
from toolbox.sql.aggs import Metric, COUNT_DISTINCT, COUNT, none_metric
from sql_queries.meta import TicketsWithIterationsAggregatesMeta


people = Metric(
    'people',
    COUNT_DISTINCT(TicketsWithIterationsAggregatesMeta.user_id),
)
tickets = Metric(
    'tickets',
    COUNT_DISTINCT(TicketsWithIterationsAggregatesMeta.ticket_scid),
)
iterations = Metric(
    'iterations',
    COUNT(TicketsWithIterationsAggregatesMeta.emp_post_id),
)

metrics = {
    people.name: people,
    tickets.name: tickets,
    iterations.name: iterations,
}


def get_metric(metric: str) -> Metric:
    return get_metrics().get(metric, none_metric)


def get_metrics_names(
    formatter: Callable[[Metric], str] = lambda x: x.name
) -> Iterable:
    return [formatter(x) for x in get_metrics().values()]


def get_metrics() -> Mapping[str, Metric]:
    return metrics
