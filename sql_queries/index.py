from toolbox.sql.index import RootPath


class CustomersActivitySqlPathIndex:

    @staticmethod
    def get_root_path() -> str:
        return RootPath.get_cwd() + '/customers_activity'

    @staticmethod
    def get_extract_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/extract'

    @staticmethod
    def get_tables_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/tables'

    @staticmethod
    def get_groups_path() -> str:
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
    def get_ticket_types_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_tables_path()
            + '/ticket_types.sql'
        )

    @staticmethod
    def get_fill_ticket_types_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_tables_path()
            + '/fill_ticket_types.sql'
        )


class CustomersActivityDBIndex:

    @staticmethod
    def get_root_name() -> str:
        return 'CustomersActivity_'

    @staticmethod
    def get_tags_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'TicketTags'

    @staticmethod
    def get_groups_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'UserGroups'

    @staticmethod
    def get_tickets_with_iterations_name() -> str:
        return CustomersActivityDBIndex.get_root_name(
        ) + 'TicketsWithIterations'

    @staticmethod
    def get_ticket_types_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'TicketTypes'
