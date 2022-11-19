from toolbox.sql.index import RootPath


class CustomersActivitySqlPathIndex:

    @staticmethod
    def get_root_path() -> str:
        return RootPath.get_cwd() + '/customers_activity'

    @staticmethod
    def get_groups_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/groups.sql'

    @staticmethod
    def get_tags_path() -> str:
        return CustomersActivitySqlPathIndex.get_root_path() + '/tags.sql'

    @staticmethod
    def get_tickets_with_iterations_path() -> str:
        return (
            CustomersActivitySqlPathIndex.get_root_path()
            + '/tickets_with_iterations.sql'
        )


class CustomersActivityDBIndex:

    @staticmethod
    def get_root_name() -> str:
        return 'customers_activity_'

    @staticmethod
    def get_tags_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'tags'

    @staticmethod
    def get_groups_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'groups'

    @staticmethod
    def get_tickets_with_iterations_name() -> str:
        return CustomersActivityDBIndex.get_root_name() + 'tags'
