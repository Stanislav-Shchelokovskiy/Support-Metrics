from collections.abc import Mapping, Iterable
from itertools import chain
from toolbox.sql_async import (
    AsyncQueryDescriptor,
    MetricAsyncQueryDescriptor,
    GeneralSelectAsyncQueryDescriptor,
)
from toolbox.sql import MetaData, PeriodMeta
from sql_queries.meta import (
    TicketsWithIterationsRawMeta,
    TicketsWithIterationsMeta,
    BaselineAlignedModeMeta,
)
from repository.local.core.tickets_with_iterations_table import get_tickets_with_iterations_table
from repository.local.aggs import get_metric
from toolbox.sql.generators.utils import build_multiline_string_ignore_empties
import sql_queries.index.path.local as LocalPathIndex
import sql_queries.index.name as name_index
import repository.local.generators.periods as PeriodsGenerator
import configs.config as config


class TicketsPeriod(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return PeriodMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': f"DATE(MIN({TicketsWithIterationsMeta.creation_date}), '+{config.get_rank_period_offset()}') AS {PeriodMeta.start}, MAX({TicketsWithIterationsMeta.creation_date}) AS {PeriodMeta.end}",
            'from': name_index.tickets_with_iterations,
            'where_group_limit': '',
        }


class TicketsWithIterationsRaw(AsyncQueryDescriptor):
    """
    Query to a local table storing raw tickets with iterations data.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return LocalPathIndex.tickets_with_iterations_raw

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'csi_table': name_index.csi,
            'replies_types_table': name_index.cat_replies_types,
            'components_features_table': name_index.cat_components_features,
            'license_statuses_table': name_index.license_statuses,
            'conversion_statuses_table': name_index.conversion_statuses,
            'tickets_types_table': name_index.tickets_types,
            'employees_table': name_index.employees,
            'severity_table': name_index.severity,
            'operating_systems_table': name_index.operating_systems,
            'ides_table': name_index.ides,
            'platforms_products_table': name_index.platforms_products,
            'tickets_tags_table': name_index.tickets_tags,
            **TicketsWithIterationsRawMeta.get_attrs(),
            'baseline_aligned_mode_fields': self.get_baseline_aligned_mode_fields(**kwargs),
            'tickets_with_iterations_table': get_tickets_with_iterations_table(**kwargs),
            'tbl_alias': name_index.tickets_with_iterations_alias,
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
            return tuple(chain(res, (BaselineAlignedModeMeta.days_since_baseline, )))
        return res


class TicketsWithIterationsAggregates(MetricAsyncQueryDescriptor):

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        period, agg, agg_name, *_ = self.get_fields(kwargs)
        groupby_period = PeriodsGenerator.generate_group_by_period(kwargs)
        metric = get_metric(kwargs['metric'])
        return {
            'select': f"{groupby_period} AS {period}, {metric} AS {agg}, '{metric.get_display_name()}' AS {agg_name}",
            'from':  get_tickets_with_iterations_table(**kwargs),
            'where_group_limit': build_multiline_string_ignore_empties(
                (
                    f'GROUP BY {groupby_period}', 
                    f'ORDER BY {period}',
                )
            )
        }
