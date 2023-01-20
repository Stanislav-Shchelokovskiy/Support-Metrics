from repository.customers_activity.local.sql_filters_generator.tickets_with_iterations import TicketsWithIterationsSqlFilterClauseGenerator


def get_creation_date_with_offset_start_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    return filter_generator.generate_creation_date_with_offset_start_filter(
        range_start=kwargs['range_start'],
        range_end=kwargs['range_end'],
    )


def get_creation_date_and_tickets_filters(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
):
    return f"""{filter_generator.generate_creation_date_filter(
                range_start= kwargs['range_start'],
                range_end=kwargs['range_end'],
            )}
            {get_tickets_filter(kwargs=kwargs,filter_generator=filter_generator) if kwargs['use_tracked_customer_groups'] else ''}"""


def get_tickets_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    return f"""{filter_generator.generate_tribes_filter(params=kwargs['tribe_ids'])}
                    {filter_generator.generate_platforms_filter(params=kwargs['platforms_ids'])}
                    {filter_generator.generate_products_filter(params=kwargs['products_ids'])}
                    {filter_generator.generate_ticket_types_filter(params=kwargs['tickets_types'])}
                    {filter_generator.generate_ticket_tags_filter(params=kwargs['tickets_tags'])}
                    {get_customer_groups_filter(kwargs=kwargs,filter_generator=filter_generator)}
                    {filter_generator.generate_license_status_filter(params=kwargs['license_statuses'])}
                    {filter_generator.generate_conversion_status_filter(params=kwargs['conversion_statuses'])}
                    {filter_generator.generate_emp_positions_filter(params=kwargs['positions_ids'])}
                    {filter_generator.generate_emp_tribes_filter(params=kwargs['emp_tribe_ids'])}
                    {filter_generator.generate_employees_filter(params=kwargs['emp_ids'])}
                    {filter_generator.generate_reply_types_filter(params=kwargs['reply_ids'])}
                    {filter_generator.generate_components_filter(params=kwargs['components_ids'])}
                    {filter_generator.generate_features_filter(params=kwargs['feature_ids'])}
                    {filter_generator.generate_customers_filter(params=kwargs['customers_crmids'])}"""


def get_customer_groups_filter(
    kwargs: dict,
    filter_generator: TicketsWithIterationsSqlFilterClauseGenerator,
) -> str:
    return (
        '' if kwargs['use_tracked_customer_groups'] else
        filter_generator.generate_customer_groups_filter(
            params=kwargs['customers_groups']
        )
    )
