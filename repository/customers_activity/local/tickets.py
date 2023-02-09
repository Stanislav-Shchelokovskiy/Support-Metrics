from toolbox.sql.repository import SqliteRepository
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
class TicketsTypesRepository(SqliteRepository):
    """
    Interface to a local table storing tickets types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_types_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTypesMeta.get_values()


class TicketsTagsRepository(SqliteRepository):
    """
    Interface to a local table storing tickets tags.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_tags_name(),
            'filter_group_limit_clause': f'ORDER BY {TicketsTagsMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTagsMeta.get_values()

class FrameworksRepository(SqliteRepository):
    """
    Interface to a local table storing frameworks.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_frameworks_name(),
            'filter_group_limit_clause': f'ORDER BY {FrameworksMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return FrameworksMeta.get_values()


class OperatingSystemsRepository(SqliteRepository):
    """
    Interface to a local table storing operating systems.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_operating_systems_name(),
            'filter_group_limit_clause': f'ORDER BY {OperatingSystemsMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return OperatingSystemsMeta.get_values()


class BuildsRepository(SqliteRepository):
    """
    Interface to a local table storing builds.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_builds_name(),
            'filter_group_limit_clause': f'ORDER BY {BuildsMeta.id} DESC',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return [BuildsMeta.id]


class SeverityRepository(SqliteRepository):
    """
    Interface to a local table storing bug severity values.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_severity_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return SeverityMeta.get_values()


class TicketStatueseRepository(SqliteRepository):
    """
    Interface to a local table storing ticket statuses values.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_ticket_statuses_name(),
            'filter_group_limit_clause': '',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketStatusesMeta.get_values()


class IDEsRepository(SqliteRepository):
    """
    Interface to a local table storing ides.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {
            'columns': ', '.join(self.get_must_have_columns(kwargs)),
            'table_name': CustomersActivityDBIndex.get_ides_name(),
            'filter_group_limit_clause': f'ORDER BY {IDEsMeta.name}',
        }

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return IDEsMeta.get_values()