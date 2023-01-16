from toolbox.sql.index import RootPath


class CustomersActivitySqlPathIndex:

    @staticmethod
    def get_root_path() -> str:
        return RootPath.get_cwd() + '/customers_activity'

    @staticmethod
    def get_extract_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/extract'

    @staticmethod
    def get_transform_load_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_root_path() + '/transform_load'
        )

    @staticmethod
    def get_local_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/local'

    @staticmethod
    def get_extract_temp_tables_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path() + '/temp_tables'
        )

    @staticmethod
    def get_customers_groups_path() -> str:
        return CustomersActivitySqlPathIndex.get_extract_path() + '/groups.sql'

    @staticmethod
    def get_tracked_customers_groups_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/tracked_groups.sql'
        )

    @staticmethod
    def get_ticket_tags_path() -> str:
        return CustomersActivitySqlPathIndex.get_extract_path() + '/tags.sql'

    @staticmethod
    def get_replies_types_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/replies_types.sql'
        )

    @staticmethod
    def get_components_features_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/components_features.sql'
        )

    @staticmethod
    def get_platforms_products_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/platforms_products.sql'
        )

    @staticmethod
    def get_employees_iterations_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/employees_iterations.sql'
        )

    @staticmethod
    def get_tickets_period_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_local_path()
            + '/get_tickets_period.sql'
        )

    @staticmethod
    def get_create_tickets_with_licenses_temp_table_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_temp_tables_path()
            + '/TicketsWithLicenses.sql'
        )

    @staticmethod
    def get_fill_tickets_with_licenses_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/fill_tickets_with_licenses.sql'
        )

    @staticmethod
    def get_tickets_with_licenses_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/tickets_with_licenses.sql'
        )

    @staticmethod
    def get_general_select_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_local_path()
            + '/general_select.sql'
        )

    @staticmethod
    def get_tickets_with_iterations_aggregates_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_local_path()
            + '/tickets_with_iterations_aggregates.sql'
        )

    @staticmethod
    def get_tickets_with_iterations_raw_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_local_path()
            + '/tickets_with_iterations_raw.sql'
        )

    @staticmethod
    def get_tickets_with_iterations_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_transform_load_path()
            + '/tickets_with_iterations.sql'
        )

    @staticmethod
    def get_emp_positions_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_transform_load_path()
            + '/emp_positions.sql'
        )

    @staticmethod
    def get_emp_tribes_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_transform_load_path()
            + '/emp_tribes.sql'
        )

    @staticmethod
    def get_employees_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_transform_load_path()
            + '/emps.sql'
        )

    @staticmethod
    def get_customers_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_transform_load_path()
            + '/customers.sql'
        )


class CustomersActivityDBIndex:

    @staticmethod
    def get_root_name() -> str:
        return 'CustomersActivity_'

    @staticmethod
    def get_tickets_tags_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'TicketsTags'

    @staticmethod
    def get_customers_groups_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'CustomersGroups'

    @staticmethod
    def get_tracked_customers_groups_name() -> str:
        return (
            CustomersActivityDBIndex.get_root_name() + 'TrackedCustomersGroups'
        )

    @staticmethod
    def get_replies_types_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'CatRepliesTypes'

    @staticmethod
    def get_components_features_name() -> str:
        return (
            CustomersActivityDBIndex.get_root_name() + 'CatComponentsFeatures'
        )

    @staticmethod
    def get_platforms_products_name() -> str:
        return (CustomersActivityDBIndex.get_root_name() + 'PlatformsProducts')

    @staticmethod
    def get_tickets_types_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'TicketsTypes'

    @staticmethod
    def get_license_statuses_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'LicenseStatuses'

    @staticmethod
    def get_conversion_statuses_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'ConversionStatuses'

    @staticmethod
    def get_emp_positions_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'EmpPositions'

    @staticmethod
    def get_emp_tribes_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'EmpTribes'

    @staticmethod
    def get_employees_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'Employees'

    @staticmethod
    def get_customers_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'Customers'

    @staticmethod
    def get_tickets_with_licenses_name() -> str:
        return (
            CustomersActivityDBIndex.get_root_name() + 'TicketsWithLicenses'
        )

    @staticmethod
    def get_employees_iterations_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'EmployeesIterations'

    @staticmethod
    def get_tickets_with_iterations_name() -> str:
        return (
            CustomersActivityDBIndex.get_root_name() + 'TicketsWithIterations'
        )
