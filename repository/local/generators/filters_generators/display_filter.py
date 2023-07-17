from repository.local.core.customers_rank import Percentile
from sql_queries.index import CustomersActivityDBIndex
from sql_queries.meta import (
    PlatformsProductsMeta,
    TicketsTagsMeta,
    TicketsTypesMeta,
    CustomersGroupsMeta,
    LicenseStatusesMeta,
    ConversionStatusesMeta,
    PositionsMeta,
    TribesMeta,
    TentsMeta,
    EmployeesIterationsMeta,
    CATRepliesTypesMeta,
    CATComponentsFeaturesMeta,
    CustomersMeta,
    SeverityMeta,
    TicketStatusesMeta,
    IDEsMeta,
    OperatingSystemsMeta,
    FrameworksMeta,
)
from toolbox.sql.generators.display_filter import QueryParams
from toolbox.sql.generators.filter_clause_generator_factory import BaseNode
import toolbox.sql.generators.display_filter as DisplayFilterGenerator
import repository.local.generators.filters_generators.tickets_with_iterations.limit as limit


def __get_emps_params():
    return QueryParams(
        table=CustomersActivityDBIndex.get_employees_name(),
        value_field=EmployeesIterationsMeta.scid,
        display_field=EmployeesIterationsMeta.name,
    )


def __get_tickets_types_params():
    return QueryParams(
        table=CustomersActivityDBIndex.get_tickets_types_name(),
        value_field=TicketsTypesMeta.id,
        display_field=TicketsTypesMeta.name,
    )


# yapf: disable
_query_params_store = {
    'tribe_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_tribes_name(),
            value_field=TribesMeta.id,
            display_field=TribesMeta.name,
        ),
    'tent_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_tents_name(),
            value_field=TentsMeta.id,
            display_field=TentsMeta.name,
        ),
    'platforms_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_platforms_products_name(),
            value_field=PlatformsProductsMeta.platform_id,
            display_field=PlatformsProductsMeta.platform_name,
        ),
    'products_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_platforms_products_name(),
            value_field=PlatformsProductsMeta.product_id,
            display_field=PlatformsProductsMeta.product_name,
        ),
    'tickets_tags':
        QueryParams(
            table=CustomersActivityDBIndex.get_tickets_tags_name(),
            value_field=TicketsTagsMeta.id,
            display_field=TicketsTagsMeta.name,
        ),
    'tickets_types': __get_tickets_types_params(),
    'duplicated_to_tickets_types': __get_tickets_types_params(),
    'severity':
        QueryParams(
            table=CustomersActivityDBIndex.get_severity_name(),
            value_field=SeverityMeta.id,
            display_field=SeverityMeta.name,
        ),
    'ticket_status':
        QueryParams(
            table=CustomersActivityDBIndex.get_ticket_statuses_name(),
            value_field=TicketStatusesMeta.id,
            display_field=TicketStatusesMeta.name,
        ),
    'frameworks':
        QueryParams(
            table=CustomersActivityDBIndex.get_frameworks_name(),
            value_field=FrameworksMeta.id,
            display_field=FrameworksMeta.name,
        ),
    'operating_system_id':
        QueryParams(
            table=CustomersActivityDBIndex.get_operating_systems_name(),
            value_field=OperatingSystemsMeta.id,
            display_field=OperatingSystemsMeta.name,
        ),
    'ide_id':
        QueryParams(
            table=CustomersActivityDBIndex.get_ides_name(),
            value_field=IDEsMeta.id,
            display_field=IDEsMeta.name,
        ),
    'customers_groups':
        QueryParams(
            table=CustomersActivityDBIndex.get_customers_groups_name(),
            value_field=CustomersGroupsMeta.id,
            display_field=CustomersGroupsMeta.name,
        ),
    'license_statuses':
        QueryParams(
            table=CustomersActivityDBIndex.get_license_statuses_name(),
            value_field=LicenseStatusesMeta.id,
            display_field=LicenseStatusesMeta.name,
        ),
    'conversion_statuses':
        QueryParams(
            table=CustomersActivityDBIndex.get_conversion_statuses_name(),
            value_field=ConversionStatusesMeta.id,
            display_field=ConversionStatusesMeta.name,
        ),
    'positions_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_emp_positions_name(),
            value_field=PositionsMeta.id,
            display_field=PositionsMeta.name,
        ),
    'emp_tribe_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_emp_tribes_name(),
            value_field=TribesMeta.id,
            display_field=TribesMeta.name,
        ),
    'emp_tent_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_emp_tents_name(),
            value_field=TentsMeta.id,
            display_field=TentsMeta.name,
        ),
    'emp_ids': __get_emps_params(),
    'assigned_to_ids': __get_emps_params(),
    'closed_by_ids': __get_emps_params(),
    'fixed_by_ids': __get_emps_params(),
    'reply_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_cat_replies_types_name(),
            value_field=CATRepliesTypesMeta.id,
            display_field=CATRepliesTypesMeta.name,
        ),
    'components_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_cat_components_features_name(),
            value_field=CATComponentsFeaturesMeta.component_id,
            display_field=CATComponentsFeaturesMeta.component_name,
        ),
    'feature_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_cat_components_features_name(),
            value_field=CATComponentsFeaturesMeta.feature_id,
            display_field=CATComponentsFeaturesMeta.feature_name,
        ),
    'customers_crmids':
        QueryParams(
            table=CustomersActivityDBIndex.get_customers_name(),
            value_field=CustomersMeta.id,
            display_field=CustomersMeta.name,
        ),
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
