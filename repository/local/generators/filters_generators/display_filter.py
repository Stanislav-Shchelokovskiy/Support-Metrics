from repository.local.core.customers_rank import Percentile
from sql_queries.meta import (
    PlatformsProductsMeta,
    CustomersGroupsMeta,
    ConversionStatusesMeta,
    EmployeesIterationsMeta,
    CATComponentsFeaturesMeta,
)
from toolbox.sql.generators.display_filter import QueryParams
from toolbox.sql.generators.filter_clause_generator_factory import BaseNode
import toolbox.sql.generators.display_filter as DisplayFilterGenerator
import repository.local.generators.filters_generators.tickets_with_iterations.limit as limit
import sql_queries.index.db as DbIndex


def __get_emps_params():
    return QueryParams(
        table=DbIndex.employees,
        value_field=EmployeesIterationsMeta.scid.name,
        display_field=EmployeesIterationsMeta.name.name,
    )


def __get_tickets_types_params():
    return QueryParams(table=DbIndex.tickets_types)


# yapf: disable
_query_params_store = {
    'tribe_ids': QueryParams(table=DbIndex.tribes),
    'tent_ids': QueryParams(table=DbIndex.tents),
    'platforms_ids':
        QueryParams(
            table=DbIndex.platforms_products,
            value_field=PlatformsProductsMeta.platform_id.name,
            display_field=PlatformsProductsMeta.platform_name.name,
        ),
    'products_ids':
        QueryParams(
            table=DbIndex.platforms_products,
            value_field=PlatformsProductsMeta.product_id.name,
            display_field=PlatformsProductsMeta.product_name.name,
        ),
    'tickets_tags': QueryParams(table=DbIndex.tickets_tags),
    'tickets_types': __get_tickets_types_params(),
    'duplicated_to_tickets_types': __get_tickets_types_params(),
    'severity': QueryParams(table=DbIndex.severity),
    'ticket_status': QueryParams(table=DbIndex.ticket_statuses),
    'frameworks': QueryParams(table=DbIndex.frameworks),
    'operating_system_id': QueryParams(table=DbIndex.operating_systems),
    'ide_id': QueryParams(table=DbIndex.ides),
    'customers_groups':
        QueryParams(
            table=DbIndex.customers_groups,
            value_field=CustomersGroupsMeta.id.name,
            display_field=CustomersGroupsMeta.name.name,
        ),
    'license_statuses': QueryParams(table=DbIndex.license_statuses),
    'conversion_statuses':
        QueryParams(
            table=DbIndex.conversion_statuses,
            value_field=ConversionStatusesMeta.id.name,
            display_field=ConversionStatusesMeta.name.name,
        ),
    'positions_ids': QueryParams(table=DbIndex.emp_positions),
    'emp_tribe_ids': QueryParams(table=DbIndex.emp_tribes),
    'emp_tent_ids': QueryParams(table=DbIndex.emp_tents),
    'emp_ids': __get_emps_params(),
    'assigned_to_ids': __get_emps_params(),
    'closed_by_ids': __get_emps_params(),
    'fixed_by_ids': __get_emps_params(),
    'reply_ids': QueryParams(table=DbIndex.cat_replies_types),
    'components_ids':
        QueryParams(
            table=DbIndex.cat_components_features,
            value_field=CATComponentsFeaturesMeta.component_id.name,
            display_field=CATComponentsFeaturesMeta.component_name.name,
        ),
    'feature_ids':
        QueryParams(
            table=DbIndex.cat_components_features,
            value_field=CATComponentsFeaturesMeta.feature_id.name,
            display_field=CATComponentsFeaturesMeta.feature_name.name,
        ),
    'customers_crmids': QueryParams(table=DbIndex.customers),
}
# yapf: enable


class DisplayValuesStore:

    @staticmethod
    def get_query_params(field: str) -> QueryParams:
        return _query_params_store.get(field)

    @staticmethod
    def get_display_value(field: str, alias: str, value) -> str:
        if field == 'is_private':
            value = 'Private' if value else 'Public'
        return value


def custom_display_filter(
    field_name: str,
    field_alias: str,
    filter_node,
) -> list | None:
    if isinstance(filter_node, Percentile):
        percentile: Percentile = filter_node
        percentile_filter = limit.generate_percentile_filter(
            alias=field_alias,
            percentile=percentile.value,
        )
        return [int(clause) if clause.isdigit() else clause for clause in percentile_filter.split(' ')]
    return None


async def generate_display_filter(node: BaseNode) -> str:
    return await DisplayFilterGenerator.generate_display_filter(
        node=node,
        custom_display_filter=custom_display_filter,
        display_values_store=DisplayValuesStore,
    )
