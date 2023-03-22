from typing import Any
from toolbox.sql.repository import SqliteRepository
from toolbox.sql.repository_queries import RepositoryQueries
from repository.customers_activity.local.generators.filters_generators.sql_filter_clause_generator_factory import (
    BaseNode,
    FilterParametersNode,
    FilterParameterNode,
)
from repository.customers_activity.local.core.customers_rank import Percentile
from sql_queries.index import (
    CustomersActivityDBIndex,
    CustomersActivitySqlPathIndex,
)
from sql_queries.customers_activity.meta import (
    PlatformsProductsMeta,
    TicketsTagsMeta,
    TicketsTypesMeta,
    CustomersGroupsMeta,
    LicenseStatusesMeta,
    ConversionStatusesMeta,
    PositionsMeta,
    TribesMeta,
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
import repository.customers_activity.local.generators.filters_generators.tickets_with_iterations.limit as limit


class QueryParams:

    def __init__(
        self,
        table: str,
        value_field: str = 'id',
        display_field: str = 'name',
    ) -> None:
        self.table = table
        self.value_field = value_field
        self.display_field = display_field


query_params_store = {
    'tribe_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_tribes_name(),
            value_field=TribesMeta.id,
            display_field=TribesMeta.name,
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
    'tickets_types':
        QueryParams(
            table=CustomersActivityDBIndex.get_tickets_types_name(),
            value_field=TicketsTypesMeta.id,
            display_field=TicketsTypesMeta.name,
        ),
    'duplicated_to_tickets_types':
        QueryParams(
            table=CustomersActivityDBIndex.get_tickets_types_name(),
            value_field=TicketsTypesMeta.id,
            display_field=TicketsTypesMeta.name,
        ),
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
    'emp_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_employees_name(),
            value_field=EmployeesIterationsMeta.crmid,
            display_field=EmployeesIterationsMeta.name,
        ),
    'assigned_to_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_employees_name(),
            value_field=EmployeesIterationsMeta.crmid,
            display_field=EmployeesIterationsMeta.name,
        ),
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


class DisplayFilterGenerator:
    repository_type = SqliteRepository

    # yapf: disable
    @staticmethod
    def generate_display_filter(node: BaseNode) -> list[list]:
        filters = []
        filter_node: BaseNode | FilterParametersNode | FilterParameterNode | Percentile
        aliases = node.get_field_aliases()
        for field_name, filter_node in node.get_field_values().items():
            if not filter_node:
                continue
            field_alias = aliases[field_name]
            filter = None
            match filter_node:
                case FilterParametersNode():
                    filter = DisplayFilterGenerator.generate_filter_from_filter_parameters(
                        field=field_name,
                        field_alias=field_alias,
                        filter_node=filter_node,
                    )
                    if not filter:
                        continue
                case FilterParameterNode():
                    display_value = DisplayFilterGenerator.get_display_value(
                        field_name=field_name,
                        value=filter_node.value,
                    )
                    filter = [field_alias, '=', display_value]
                case Percentile():
                    percentile: Percentile = filter_node
                    percentile_filter = limit.generate_percentile_filter(
                        alias=field_alias,
                        percentile=percentile.value,
                    )
                    filter = [int(clause) if clause.isdigit() else clause for clause in percentile_filter.split(' ')]
                case _:
                    filter = DisplayFilterGenerator.generate_display_filter(node=filter_node)
            DisplayFilterGenerator.append_filter(filters, filter, node)

        if len(filters) == 1:
            return filters[0]
        return filters

    @staticmethod
    def get_display_value(field_name: str, value: Any):
        if field_name == 'is_private':
            value = 'Private' if value else 'Public'
        return value

    @staticmethod
    def generate_filter_from_filter_parameters(
        field: str,
        field_alias: str,
        filter_node: FilterParametersNode,
    ):
        if not filter_node.values:
            if not filter_node.include:
                return [field_alias, '=', 'NULL']
            return ''

        display_values = DisplayFilterGenerator.get_display_values(
            field=field,
            values=filter_node.values,
        )

        if filter_node.include:
            return [field_alias, 'in', display_values]

        filter = []
        filter.append([field_alias, '=', 'NULL'])
        filter.append('or')
        filter.append([field_alias, 'notin', display_values])
        return filter

    @staticmethod
    def get_display_values(
        field: str,
        values: list,
    ):
        if query_params := query_params_store.get(field):
            values = ', '.join([f"'{value}'" for value in values])
            return DisplayFilterGenerator.repository_type(
                queries=RepositoryQueries(
                    main_query_path=CustomersActivitySqlPathIndex.get_general_select_path(),
                    main_query_format_params={
                        'columns': query_params.display_field,
                        'table_name': query_params.table,
                        'filter_group_limit_clause': f'WHERE {query_params.value_field} IN ({values})\nGROUP BY {query_params.display_field}',
                    }
                )
            ).get_data().reset_index(drop=True)[query_params.display_field].values.tolist()
        return values

    @staticmethod
    def append_filter(filters: list, filter: list, node: BaseNode):
        if not filter:
            return
        if filters:
            filters.append(node.get_append_operator())
        filters.append(filter)
