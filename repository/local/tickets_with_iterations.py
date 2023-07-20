from collections.abc import Mapping, Iterable
from itertools import chain
from toolbox.sql_async import (
    AsyncQueryDescriptor,
    MetricAsyncQueryDescriptor,
    GeneralSelectAsyncQueryDescriptor,
)
from toolbox.sql import MetaData
from sql_queries.meta import (
    TicketsWithIterationsRawMeta,
    TicketsWithIterationsMeta,
    PeriodMeta,
    BaselineAlignedModeMeta,
)
from configs.config import Config
from repository.local.core.tickets_with_iterations_table import get_tickets_with_iterations_table
from repository.local.core.filters import try_get_creation_date_and_tickets_filters
from repository.local.aggs import get_metric
from toolbox.sql.generators.utils import build_multiline_string_ignore_empties
import sql_queries.index.path.local as LocalPathIndex
import sql_queries.index.db as DbIndex
import repository.local.generators.periods as PeriodsGenerator


class TicketsPeriod(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return PeriodMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': f"DATE(MIN({TicketsWithIterationsMeta.creation_date}), '+{Config.get_rank_period_offset()}') AS {PeriodMeta.period_start}, MAX({TicketsWithIterationsMeta.creation_date}) AS {PeriodMeta.period_end}",
            'from': DbIndex.customers_tickets,
            'where_group_limit': '',
        }


class TicketsWithIterationsRaw(AsyncQueryDescriptor):
    """
    Query to a local table storing raw tickets with iterations data.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return LocalPathIndex.tickets_with_iterations_raw

    def get_general_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'tickets_with_iterations_table': get_tickets_with_iterations_table(**kwargs),
            'tickets_filter': try_get_creation_date_and_tickets_filters(**kwargs),
        }

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'replies_types_table': DbIndex.cat_replies_types,
            'components_features_table': DbIndex.cat_components_features,
            'license_statuses_table': DbIndex.license_statuses,
            'conversion_statuses_table': DbIndex.conversion_statuses,
            'tickets_types_table': DbIndex.tickets_types,
            'employees_table': DbIndex.employees,
            'severity_table': DbIndex.severity,
            'operating_systems_table': DbIndex.operating_systems,
            'ides_table': DbIndex.ides,
            'platforms_products_table': DbIndex.platforms_products,
            'tickets_tags_table': DbIndex.tickets_tags,
            **TicketsWithIterationsRawMeta.get_attrs(),
            'baseline_aligned_mode_fields': self.get_baseline_aligned_mode_fields(**kwargs),
            **self.get_general_format_params(**kwargs)
        }

    def get_baseline_aligned_mode_fields(self, **kwargs) -> str:
        if kwargs['use_baseline_aligned_mode']:
            return f', t.{BaselineAlignedModeMeta.days_since_baseline}'
        return ''

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsWithIterationsRawMeta

    def get_fields(self, kwargs: Mapping) -> Iterable[str]:
        res = self.get_fields_meta(kwargs).get_values()
        if kwargs['use_baseline_aligned_mode']:
            return chain(res, (BaselineAlignedModeMeta.days_since_baseline, ))
        return res


class TicketsWithIterationsAggregates(MetricAsyncQueryDescriptor):

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        period, agg, agg_name, *_ = self.get_fields(kwargs)
        groupby_period = PeriodsGenerator.generate_group_by_period(kwargs)
        metric = get_metric(kwargs['metric'])
        return {
            'select': f'{groupby_period} AS {period}, {metric} AS {agg}, "{metric.name}" AS {agg_name}',
            'from':  get_tickets_with_iterations_table(**kwargs),
            'where_group_limit': build_multiline_string_ignore_empties(
                    (
                        try_get_creation_date_and_tickets_filters(**kwargs),
                        f'GROUP BY {groupby_period}', f'ORDER BY {period}'
                    )
                )
        }
