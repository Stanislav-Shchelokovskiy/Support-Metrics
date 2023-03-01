from typing import Iterable
from toolbox.sql.repository_queries import RepositoryQueries
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.customers_activity.meta import (
    TicketsTagsMeta,
    TicketsTypesMeta,
    FrameworksMeta,
    OperatingSystemsMeta,
    BuildsMeta,
    SeverityMeta,
    TicketStatusesMeta,
    IDEsMeta,
)


# yapf: disable
class TicketsTypes(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_types_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsTypesMeta.get_values()


class TicketsTags(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_tags_name(),
            'filter_group_limit_clause': f'ORDER BY {TicketsTagsMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketsTagsMeta.get_values()

class Frameworks(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_frameworks_name(),
            'filter_group_limit_clause': f'ORDER BY {FrameworksMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return FrameworksMeta.get_values()


class OperatingSystems(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_operating_systems_name(),
            'filter_group_limit_clause': f'ORDER BY {OperatingSystemsMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return OperatingSystemsMeta.get_values()


class BuildsRepositoryQueries(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_builds_name(),
            'filter_group_limit_clause': f'ORDER BY {BuildsMeta.id} DESC',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return (BuildsMeta.id,)


class Severity(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_severity_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return SeverityMeta.get_values()


class TicketStatuses(RepositoryQueries):


    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_ticket_statuses_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return TicketStatusesMeta.get_values()


class IDEs(RepositoryQueries):

    def get_main_query_path(self, **kwargs) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, **kwargs) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(**kwargs)),
            'table_name': CustomersActivityDBIndex.get_ides_name(),
            'filter_group_limit_clause': f'ORDER BY {IDEsMeta.name}',
        }

    def get_must_have_columns(self, **kwargs) -> Iterable[str]:
        return IDEsMeta.get_values()
