from toolbox.sql.repository import SqliteRepository, Repository
from repository.customers_activity.local.filters_generators.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator
from repository.customers_activity.local.filters_generators.sql_filter_clause_generator import FilterParametersNode
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
)


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
    # yapf: disable
    @staticmethod
    def generate_display_filter(
        aliases: dict[str, str],
        repository: Repository = SqliteRepository(),
        **kwargs,
    ) -> list[list]:
        filters = []
        v: FilterParametersNode
        for k, v in kwargs.items():
            display_field_alias = aliases[k]
            if qp:= query_params_store.get(k):
                if not v.values:
                    continue
                values = ', '.join([f"'{value}'" for value in v.values])
                display_values =repository.execute_query(
                    query_file_path=CustomersActivitySqlPathIndex.get_general_select_path(),
                    query_format_params={
                        'columns': qp.display_field,
                        'table_name': qp.table,
                        'filter_group_limit_clause': f'WHERE {qp.value_field} IN ({values})\n GROUP BY {qp.display_field}',
                    }
                ).reset_index(drop=True)[qp.display_field].values.tolist()
                if v.include:
                    DisplayFilterGenerator.append_filter(filters, [display_field_alias, 'in', display_values])
                else:
                    filter = []
                    filter.append([display_field_alias, '=', 'NULL'])
                    filter.append('or')
                    filter.append([display_field_alias, 'notin', display_values])
                    DisplayFilterGenerator.append_filter(filters, filter)
            else:
                percentile: Percentile = kwargs['percentile']
                percentile_filter = TicketsWithIterationsSqlFilterClauseGenerator.get_percentile_filter(
                        alias = display_field_alias,
                        percentile=percentile.value,
                )
                filters.append([ int(clause) if clause.isdigit() else clause for clause in percentile_filter.split(' ')])
        return filters

    @staticmethod
    def append_filter(filters: list, filter):
        if filters:
            filters.append('and')
        filters.append(filter)
