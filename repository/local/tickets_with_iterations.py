from collections.abc import Mapping, Iterable
from itertools import chain
from toolbox.sql_async import (
    AsyncQueryDescriptor,
    MetricAsyncQueryDescriptor,
    GeneralSelectAsyncQueryDescriptor,
)
from toolbox.sql import MetaData, PeriodMeta
from repository.local.core.tickets_with_iterations_table import get_tickets_with_iterations_table
from repository.local.aggs import get_metric, is_baseline_aligned_mode
from toolbox.sql.generators.utils import build_multiline_string_ignore_empties
import sql_queries.meta.aggs as aggs
import sql_queries.meta.customers as customers
import sql_queries.meta.tickets as tickets
import sql_queries.meta.cat as cat
import sql_queries.meta.platforms_products as platforms_products
import sql_queries.meta.employees as employees
import sql_queries.meta.tribes_tents as tribes_tents
import sql_queries.index.path.local as LocalPathIndex
import repository.local.generators.periods as PeriodsGenerator
import configs.tasks_config as tasks_config


class TicketsPeriod(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return PeriodMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': f"DATE(MIN({aggs.TicketsWithIterations.creation_date}), '+{tasks_config.get_rank_period_offset()}') AS {PeriodMeta.start}, MAX({aggs.TicketsWithIterations.creation_date}) AS {PeriodMeta.end}",
            'from': aggs.TicketsWithIterations.get_name(),
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
            'csi_table': aggs.CSI.get_name(),
            'replies_types_table': cat.CatRepliesTypes.get_name(),
            'components_features_table': cat.CatComponentsFeatures.get_name(),
            'license_statuses_table': customers.LicenseStatuses.get_name(),
            'conversion_statuses_table': customers.ConversionStatuses.get_name(),
            'tickets_types_table': tickets.TicketsTypes.get_name(),
            'employees_table': employees.Employees.get_name(),
            'severity_table': tickets.Severity.get_name(),
            'operating_systems_table': tickets.OperatingSystems.get_name(),
            'ides_table': tickets.IDEs.get_name(),
            'platforms_products_table': platforms_products.PlatformsProducts.get_name(),
            'tickets_tags_table': tickets.TicketsTags.get_name(),
            **aggs.TicketsWithIterationsRaw.get_attrs(),
            'baseline_aligned_mode_fields': self.get_baseline_aligned_mode_fields(kwargs),
            'tickets_with_iterations_table': get_tickets_with_iterations_table(**kwargs),
            'roles_table': employees.Roles.get_name(),
            'tribes_table': tribes_tents.Tribes.get_name(),
            'tents_table': tribes_tents.Tents.get_name(),
            'tbl_alias': aggs.TicketsWithIterationsRaw.get_alias(),
        }

    def get_baseline_aligned_mode_fields(self, kwargs) -> str:
        if is_baseline_aligned_mode(kwargs):
            return f', {aggs.TicketsWithIterationsRaw.get_alias()}.{customers.BaselineAlignedMode.days_since_baseline}'
        return ''

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return aggs.TicketsWithIterationsRaw

    def get_fields(self, kwargs: Mapping) -> Iterable[str]:
        res = self.get_fields_meta(kwargs).get_values()
        if is_baseline_aligned_mode(kwargs):
            return tuple(chain(res, (customers.BaselineAlignedMode.days_since_baseline, )))
        return res


class TicketsWithIterationsAggregates(MetricAsyncQueryDescriptor):

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        period, agg, agg_name, *_ = self.get_fields(kwargs)
        groupby_period = PeriodsGenerator.generate_group_by_period(kwargs)
        metric = get_metric(kwargs['metric'])
        return {
            'select': f"{groupby_period} AS {period}, {metric} AS {agg}, '{metric.get_display_name()}' AS {agg_name}",
            'from': get_tickets_with_iterations_table(**kwargs, groupby_period=groupby_period),
            'where_group_limit': build_multiline_string_ignore_empties(
                (
                    f'GROUP BY {groupby_period}',
                    f'ORDER BY {period}',
                )
            ),
        }
