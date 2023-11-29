from repository.local.core.customers_rank import Percentile
from toolbox.sql.generators.display_filter import QueryParams
from toolbox.sql.generators.filter_clause_generator_factory import BaseNode
import toolbox.sql.generators.display_filter as DisplayFilterGenerator
import repository.local.generators.filters_generators.tickets_with_iterations.limit as limit
import sql_queries.meta.platforms_products as platforms_products
import sql_queries.meta.customers as customers
import sql_queries.meta.cat as cat
import sql_queries.meta.employees as employees
import sql_queries.meta.tickets as tickets
import sql_queries.meta.tribes_tents as tribes_tents


def __get_emps_params():
    return QueryParams(
        table=employees.Employee.get_name(),
        value_field=employees.Employee.scid.name,
        display_field=employees.Employee.name.name,
    )


def __get_tickets_types_params():
    return QueryParams(table=tickets.TicketsTypes.get_name())


# yapf: disable
_query_params_store = {
    'tribe_ids': QueryParams(table=tribes_tents.Tribes.get_name()),
    'tent_ids': QueryParams(table=tribes_tents.Tents.get_name()),
    'platforms_ids':
        QueryParams(
            table=platforms_products.Platforms.get_name(),
            value_field=platforms_products.Platforms.platform_id.name,
            display_field=platforms_products.Platforms.platform_name.name,
        ),
    'products_ids':
        QueryParams(
            table=platforms_products.Products.get_name(),
            value_field=platforms_products.Products.product_id.name,
            display_field=platforms_products.Products.product_name.name,
        ),
    'tickets_tags': QueryParams(table=tickets.TicketsTags.get_name()),
    'tickets_types': __get_tickets_types_params(),
    'duplicated_to_tickets_types': __get_tickets_types_params(),
    'severity': QueryParams(table=tickets.Severity.get_name()),
    'ticket_status': QueryParams(table=tickets.TicketStatuses.get_name()),
    'frameworks': QueryParams(table=tickets.Frameworks.get_name()),
    'operating_system_id': QueryParams(table=tickets.OperatingSystems.get_name()),
    'ide_id': QueryParams(table=tickets.IDEs.get_name()),
    'customers_groups':
        QueryParams(
            table=customers.CustomersGroups.get_name(),
            value_field=customers.CustomersGroups.id.name,
            display_field=customers.CustomersGroups.name.name,
        ),
    'license_statuses': QueryParams(table=customers.LicenseStatuses.get_name()),
    'conversion_statuses':
        QueryParams(
            table=customers.ConversionStatuses.get_name(),
            value_field=customers.ConversionStatuses.id.name,
            display_field=customers.ConversionStatuses.name.name,
        ),
    'positions_ids': QueryParams(table=employees.Positions.get_name()),
    'emp_tribe_ids': QueryParams(table=employees.EmpTribes.get_name()),
    'emp_tent_ids': QueryParams(table=employees.EmpTents.get_name()),
    'emp_ids': __get_emps_params(),
    'assigned_to_ids': __get_emps_params(),
    'closed_by_ids': __get_emps_params(),
    'fixed_by_ids': __get_emps_params(),
    'reply_ids': QueryParams(table=cat.CatRepliesTypes.get_name()),
    'components_ids':
        QueryParams(
            table=cat.Components.get_name(),
            value_field=cat.Components.component_id.name,
            display_field=cat.Components.component_name.name,
        ),
    'feature_ids':
        QueryParams(
            table=cat.Features.get_name(),
            value_field=cat.Features.feature_id.name,
            display_field=cat.Features.feature_name.name,
        ),
    'customers_crmids': QueryParams(table=customers.Customers.get_name()),
    'roles': QueryParams(table=employees.Roles.get_name()),
}
# yapf: enable


class DisplayValuesStore:

    @staticmethod
    def get_query_params(field: str) -> QueryParams:
        return _query_params_store.get(field)

    @staticmethod
    def get_display_value(field: str, alias: str, value) -> str:
        return {
            'is_private': 'Private' if value else 'Public',
            'is_employee': 'Employee' if value else 'Customer',
            'closed_for_n_days': f'{value} day(s)',
            'resolution_in_hours': f'{value} hour(s)'
        }.get(field, value)


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
