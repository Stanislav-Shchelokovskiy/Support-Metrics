from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from toolbox.sql.generators.utils import build_multiline_string_ignore_empties
from sql_queries.meta import (
    PositionsMeta,
    TribesMeta,
    EmployeeMeta,
    TentsMeta,
)
import repository.local.generators.filters_generators.employees as EmployeesSqlFilterClauseGenerator
import sql_queries.index.db as DbIndex


class EmpPositions(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return PositionsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.emp_positions,
            'where_group_limit': f'ORDER BY {PositionsMeta.name}',
        }


class EmpTribes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TribesMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.emp_tribes,
            'where_group_limit': f'ORDER BY {TribesMeta.name}',
        }


class EmpTents(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return TentsMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': DbIndex.emp_tents,
            'where_group_limit': f'ORDER BY {TentsMeta.name}',
        }


class Employees(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return EmployeeMeta

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = EmployeesSqlFilterClauseGenerator.generate_positions_tribes_tents_filter(
            position_ids=kwargs['position_ids'],
            tribe_ids=kwargs['tribe_ids'],
            tent_ids=kwargs['tent_ids'],
        )
        return {
            'select': f"DISTINCT {', '.join(self.get_fields(kwargs))}",
            'from': DbIndex.employees,
            'where_group_limit':  build_multiline_string_ignore_empties(
                (
                    filter,
                    f'ORDER BY {EmployeeMeta.name}',
                )
            )
        }
