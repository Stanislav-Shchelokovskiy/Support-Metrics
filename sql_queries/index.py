from toolbox.sql.index import RootPath


class CustomersActivityIndex:

    @staticmethod
    def get_root_path() -> str:
        return RootPath.get_cwd() + '/customers_activity'

    def get_groups_path() -> str:
        return CustomersActivityIndex.get_root_path() + '/groups.sql'

    def get_tags_path() -> str:
        return CustomersActivityIndex.get_root_path() + '/tags.sql'

    def get_tickets_with_iterations_path() -> str:
        return (
            CustomersActivityIndex.get_root_path()
            + '/tickets_with_iterations.sql'
        )
