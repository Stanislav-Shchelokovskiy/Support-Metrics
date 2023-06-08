from collections.abc import Mapping
from toolbox.sql_async import AsyncQueryDescriptor
from toolbox.sql import MetaData
from sql_queries.index import (
    CustomersActivitySqlPathIndex,
    CustomersActivityDBIndex,
)
from sql_queries.meta import (
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
class TicketsTypes(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsTypesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_types_name(),
            'filter_group_limit_clause': '',
        }


class TicketsTags(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsTagsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_tickets_tags_name(),
            'filter_group_limit_clause': f'ORDER BY {TicketsTagsMeta.name}',
        }


class Frameworks(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return FrameworksMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_frameworks_name(),
            'filter_group_limit_clause': f'ORDER BY {FrameworksMeta.name}',
        }


class OperatingSystems(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return OperatingSystemsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_operating_systems_name(),
            'filter_group_limit_clause': f'ORDER BY {OperatingSystemsMeta.name}',
        }


class Builds(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return BuildsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_builds_name(),
            'filter_group_limit_clause': f'ORDER BY {BuildsMeta.name} DESC',
        }


class Severity(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return SeverityMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_severity_name(),
            'filter_group_limit_clause': '',
        }


class TicketStatuses(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketStatusesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_ticket_statuses_name(),
            'filter_group_limit_clause': '',
        }


class IDEs(AsyncQueryDescriptor):

    def get_path(self, kwargs: Mapping) -> str:
        return CustomersActivitySqlPathIndex.get_general_select_path()

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return IDEsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'columns': ', '.join(self.get_fields(kwargs)),
            'table_name': CustomersActivityDBIndex.get_ides_name(),
            'filter_group_limit_clause': f'ORDER BY {IDEsMeta.name}',
        }
