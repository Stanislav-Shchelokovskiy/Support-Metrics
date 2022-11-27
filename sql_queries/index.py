from toolbox.sql.index import RootPath


class CustomersActivitySqlPathIndex:

    @staticmethod
    def get_root_path() -> str:
        return RootPath.get_cwd() + '/customers_activity'

    @staticmethod
    def get_extract_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/extract'

    @staticmethod
    def get_local_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/local'

    @staticmethod
    def get_tables_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/tables'

    @staticmethod
    def get_customers_groups_path() -> str:
        return CustomersActivitySqlPathIndex.get_extract_path() + '/groups.sql'

    @staticmethod
    def get_tags_path() -> str:
        return CustomersActivitySqlPathIndex.get_extract_path() + '/tags.sql'

    @staticmethod
    def get_tickets_with_iterations_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_extract_path()
            + '/tickets_with_iterations.sql'
        )

    @staticmethod
    def get_tickets_with_iterations_period_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_local_path()
            + '/get_tickets_with_iterations_period.sql'
        )

    @staticmethod
    def get_select_all() -> str:
        return (
            CustomersActivitySqlPathIndex.get_local_path() + '/select_all.sql'
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
    def get_tickets_with_iterations_name() -> str:
        return (
            CustomersActivityDBIndex.get_root_name() + 'TicketsWithIterations'
        )

    @staticmethod
    def get_tickets_types_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'TicketsTypes'
