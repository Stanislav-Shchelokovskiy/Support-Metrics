from collections.abc import Callable, Mapping
from toolbox.sql.aggs import Metric, COUNT_DISTINCT, COUNT, SUM, MEDIAN, AVG, NONE_METRIC
from sql_queries.meta.aggs import TicketsWithIterations, CSI


class MetricGroup:
    entities = 'Entities'
    productivity = 'Productivity'
    service = 'Service'


people = Metric(
    'People',
    '',
    MetricGroup.entities,
    COUNT_DISTINCT(TicketsWithIterations.user_id),
)
tickets = Metric(
    'Tickets',
    '',
    MetricGroup.entities,
    COUNT_DISTINCT(TicketsWithIterations.ticket_scid),
)
replies = Metric(
    'Iterations',
    'Replies',
    MetricGroup.entities,
    COUNT(TicketsWithIterations.emp_post_id),
)

iterations_to_tickets = Metric.from_metric(
    'Iterations / Tickets',
    'Replies Rate',
    MetricGroup.productivity,
    replies / tickets,
)

ticket_resolution_time = Metric(
    'Ticket Resolution Time',
    '',
    MetricGroup.productivity,
    AVG(TicketsWithIterations.resolution_in_hours),
)

ticket_lifetime = Metric(
    'Ticket Lifetime',
    '',
    MetricGroup.service,
    MEDIAN(TicketsWithIterations.lifetime_in_hours),
)

csi = Metric(
    'Satisfaction Index',
    'Customer Satisfaction Index',
    MetricGroup.service,
    SUM(f'IIF({CSI.rating} = 1, 1, 0)') / COUNT('*') * 100,
)

metrics = {
    replies.name: replies,
    people.name: people,
    tickets.name: tickets,
    iterations_to_tickets.name: iterations_to_tickets,
    csi.name: csi,
    ticket_lifetime.name: ticket_lifetime,
    ticket_resolution_time.name: ticket_resolution_time,
}


def get_metric(metric: str) -> Metric:
    return get_metrics().get(metric, NONE_METRIC)


def select_metrics(
    projector: Callable[[Metric], str] = lambda x: x,
) -> list[str]:
    return [projector(x) for x in get_metrics().values()]


def get_metrics() -> Mapping[str, Metric]:
    return metrics


def is_csi(kwargs: Mapping) -> bool:
    return kwargs.get('metric', None) == csi.name


def is_ticket_lifetime(kwargs: Mapping) -> bool:
    return kwargs.get('metric', None) == ticket_lifetime.name


def is_baseline_aligned_mode(kwargs: Mapping) -> bool:
    return not (is_csi(kwargs) or is_ticket_lifetime(kwargs)) and kwargs['use_baseline_aligned_mode']
