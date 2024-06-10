import sql_queries.meta.tribes_tents as tribes_tents
from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData


class Tribes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tribes_tents.Tribes

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tribes_tents.Tribes.get_name(),
            'where_group_limit': f'ORDER BY {tribes_tents.Tribes.name}',
        }


class Tents(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return tribes_tents.Tents

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': tribes_tents.Tents.get_name(),
            'where_group_limit': f'ORDER BY {tribes_tents.Tents.name}',
        }
