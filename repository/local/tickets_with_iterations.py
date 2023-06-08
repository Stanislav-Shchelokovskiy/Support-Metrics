from collections.abc import Mapping, Iterable
from itertools import chain
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.meta import (
    TicketsWithIterationsAggregatesOnlyMeta,
    TicketsWithIterationsAggregatesMeta,
    TicketsWithIterationsRawMeta,
    TicketsWithIterationsMeta,
    TicketsWithIterationsPeriodMeta,
    BaselineAlignedModeMeta,
)
from configs.config import Config
from repository.local.core.tickets_with_iterations_table import get_tickets_with_iterations_table
from repository.local.core.filters import try_get_creation_date_and_tickets_filters
import repository.local.generators.periods as PeriodsGenerator


# yapf: disable
class TicketsPeriod(AsyncQueryDescriptor):
    """
    Query to a local table storing min and max boundarise
    for tickets and iterations.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_period_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsWithIterationsPeriodMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'table_name': CustomersActivityDBIndex.get_customers_tickets_name(),
            'rank_period_offset': Config.get_rank_period_offset(),
        }


class TicketsWithIterationsRaw(AsyncQueryDescriptor):
    """
    Query to a local table storing raw tickets with iterations data.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_raw_path()

    def get_general_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'tickets_with_iterations_table': get_tickets_with_iterations_table(**kwargs),
            'tickets_filter': try_get_creation_date_and_tickets_filters(**kwargs),
        }

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'replies_types_table': CustomersActivityDBIndex.get_cat_replies_types_name(),
            'components_features_table': CustomersActivityDBIndex.get_cat_components_features_name(),
            'license_statuses_table': CustomersActivityDBIndex.get_license_statuses_name(),
            'conversion_statuses_table': CustomersActivityDBIndex.get_conversion_statuses_name(),
            'tickets_types_table': CustomersActivityDBIndex.get_tickets_types_name(),
            'employees_table': CustomersActivityDBIndex.get_employees_name(),
            'severity_table': CustomersActivityDBIndex.get_severity_name(),
            'operating_systems_table': CustomersActivityDBIndex.get_operating_systems_name(),
            'ides_table': CustomersActivityDBIndex.get_ides_name(),
            'platforms_products_table': CustomersActivityDBIndex.get_platforms_products_name(),
            'tickets_tags_table': CustomersActivityDBIndex.get_tickets_tags_name(),
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
            return chain(res, (BaselineAlignedModeMeta.days_since_baseline,))
        return res


class TicketsWithIterationsAggregates(TicketsWithIterationsRaw):
    """
    Query to a local table storing aggregated tickets with iterations data.
    """

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_aggregates_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsWithIterationsAggregatesOnlyMeta

    def get_fields(self, kwargs: Mapping) -> Iterable[str]:
        return self.get_fields_meta(kwargs).get_values()

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        group_by_period = PeriodsGenerator.generate_group_by_period(
            format=kwargs['group_by_period'],
            field=BaselineAlignedModeMeta.days_since_baseline if kwargs['use_baseline_aligned_mode'] else TicketsWithIterationsMeta.creation_date,
            use_baseline_aligned_mode=kwargs['use_baseline_aligned_mode'],
        )
        return {
            **TicketsWithIterationsAggregatesMeta.get_attrs(),
            'group_by_period': group_by_period,
            **TicketsWithIterationsRaw.get_general_format_params(self, **kwargs)
        }
