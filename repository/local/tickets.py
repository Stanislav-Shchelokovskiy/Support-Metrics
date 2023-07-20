from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
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
import sql_queries.index.db as DbIndex


# yapf: disable
class TicketsTypes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsTypesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.tickets_types,
            'where_group_limit': '',
        }


class TicketsTags(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketsTagsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.tickets_tags,
            'where_group_limit': f'ORDER BY {TicketsTagsMeta.name}',
        }


class Frameworks(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return FrameworksMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.frameworks,
            'where_group_limit': f'ORDER BY {FrameworksMeta.name}',
        }


class OperatingSystems(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return OperatingSystemsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.operating_systems,
            'where_group_limit': f'ORDER BY {OperatingSystemsMeta.name}',
        }


class Builds(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return BuildsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.builds,
            'where_group_limit': f'ORDER BY {BuildsMeta.name} DESC',
        }


class Severity(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return SeverityMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.severity,
            'where_group_limit': '',
        }


class TicketStatuses(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TicketStatusesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.ticket_statuses,
            'where_group_limit': '',
        }


class IDEs(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return IDEsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.ides,
            'where_group_limit': f'ORDER BY {IDEsMeta.name}',
        }
