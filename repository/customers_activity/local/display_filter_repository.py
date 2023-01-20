from toolbox.sql.repository import SqliteRepository
from toolbox.utils.converters import DF_to_JSON
from repository.customers_activity.local.sql_filters_generator.sql_filter_clause_generator import FilterParametersNode
from sql_queries.index import CustomersActivityDBIndex, CustomersActivitySqlPathIndex
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
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
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
            table=CustomersActivityDBIndex.get_replies_types_name(),
            value_field=ReplyTypesMeta.id,
            display_field=ReplyTypesMeta.name,
        ),
    'components_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_components_features_name(),
            value_field=ComponentsFeaturesMeta.component_id,
            display_field=ComponentsFeaturesMeta.component_name,
        ),
    'feature_ids':
        QueryParams(
            table=CustomersActivityDBIndex.get_components_features_name(),
            value_field=ComponentsFeaturesMeta.feature_id,
            display_field=ComponentsFeaturesMeta.feature_name,
        ),
    'customers_crmids':
        QueryParams(
            table=CustomersActivityDBIndex.get_customers_name(),
            value_field=CustomersMeta.id,
            display_field=CustomersMeta.name,
        ),
}


class DisplayFilterRepository(SqliteRepository):

    def get_display_filter(self, **kwargs) -> list[list]:
        filters = []
        for k, v in kwargs.items():
            print(k)
            print(v)
            print()
            qp = query_params_store[k]
            values = ', '.join([f"'{value}'" for value in v.values])
            display_values = self.execute_query(
                query_file_path=CustomersActivitySqlPathIndex.get_general_select_path(),
                query_format_params={
                        'columns': f'{qp.display_field} AS qwe',#{alias}',
                        'table_name': qp.table,
                        'filter_group_limit_clause': f'WHERE {qp.value_field} IN ({values})',
                    }
            ).reset_index(drop=True)[qp.display_field].values.tolist()
            filters.append(['alias', 'in', display_values])
        return filters
