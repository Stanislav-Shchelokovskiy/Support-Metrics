from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
import sql_queries.meta.tickets as tickets


# yapf: disable
class TicketsTypes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.TicketsTypes

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.TicketsTypes.get_name(),
            'where_group_limit': '',
        }


class TicketsTags(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.TicketsTags

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.TicketsTags.get_name(),
            'where_group_limit': f'ORDER BY {tickets.TicketsTags.name}',
        }


class Frameworks(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.Frameworks

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.Frameworks.get_name(),
            'where_group_limit': f'ORDER BY {tickets.Frameworks.name}',
        }


class OperatingSystems(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.OperatingSystems

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.OperatingSystems.get_name(),
            'where_group_limit': f'ORDER BY {tickets.OperatingSystems.name}',
        }


class Builds(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.Builds

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.Builds.get_name(),
            'where_group_limit': f'ORDER BY {tickets.Builds.name} DESC',
        }


class Severity(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.Severity

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.Severity.get_name(),
            'where_group_limit': '',
        }


class TicketStatuses(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.TicketStatuses

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.TicketStatuses.get_name(),
            'where_group_limit': '',
        }


class IDEs(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tickets.IDEs

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tickets.IDEs.get_name(),
            'where_group_limit': f'ORDER BY {tickets.IDEs.name}',
        }
