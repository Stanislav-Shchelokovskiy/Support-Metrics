import pytest
from os import getcwd
from wrapt import decorator
from collections.abc import Callable, Iterable


def __prepare_env(monkeypatch: pytest.MonkeyPatch):
    with open(getcwd() + '/.env', 'r') as env:
        for line in env:
            line = line.strip()
            if line[0] == '#':
                continue
            name, value = line.split('=')
            monkeypatch.setenv(name, value)
    monkeypatch.setenv('SQLITE_DATABASE', f'{getcwd()}/Tests/test_db')
    monkeypatch.setenv('QUERY_SERVICE', 'localhost:11005')
    monkeypatch.setenv('start_date', '2022-01-01')
    monkeypatch.setenv('end_date', '2023-01-01')


@decorator
def with_env(
    callable: Callable[..., None],
    instance,
    args: Iterable,
    kwargs: dict,
):
    with pytest.MonkeyPatch.context() as monkeypatch:
        __prepare_env(monkeypatch)
        mock_TicketsWithIterationsAggregates(monkeypatch)
        return callable(**kwargs)


# yapf: disable
def mock_TicketsWithIterationsAggregates(monkeypatch: pytest.MonkeyPatch):
    from sql_queries.meta import TicketsWithIterationsAggregatesOnlyMeta, BaselineAlignedModeMeta, TicketsWithIterationsMeta
    from repository.local.tickets_with_iterations import TicketsWithIterationsAggregates
    import repository.local.generators.periods as PeriodsGenerator
    from repository.local.aggs import get_metrics
    from repository.local.core.tickets_with_iterations_table import get_tickets_with_iterations_table
    from toolbox.sql.generators.utils import build_multiline_string_ignore_empties
    from repository.local.core.filters import try_get_creation_date_and_tickets_filters

    def get_fields_meta(self, kwargs):
        return TicketsWithIterationsAggregatesOnlyMeta

    monkeypatch.setattr(
        target=TicketsWithIterationsAggregates,
        name='get_fields_meta',
        value=get_fields_meta,
    )

    def get_format_params(self, kwargs):
        period, agg, agg_name, *_ = self.get_fields(kwargs)

        groupby_period = PeriodsGenerator.generate_group_by_period(kwargs)

        metrics = get_metrics().values()
        cols = f'{groupby_period} AS {period}, {", ".join(f"{metric} AS {metric.name}" for metric in metrics)}'
        return {
            'select': cols,
            'from':  get_tickets_with_iterations_table(**kwargs),
            'where_group_limit': build_multiline_string_ignore_empties(
                (
                    try_get_creation_date_and_tickets_filters(**kwargs),
                    f'GROUP BY {groupby_period}',
                    f'ORDER BY {period}'
                )
            )
        }

    monkeypatch.setattr(
        target=TicketsWithIterationsAggregates,
        name='get_format_params',
        value=get_format_params,
    )
