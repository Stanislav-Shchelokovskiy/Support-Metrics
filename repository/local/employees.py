from collections.abc import Mapping
from toolbox.sql_async import GeneralSelectAsyncQueryDescriptor
from toolbox.sql import MetaData
from toolbox.sql.generators.utils import build_multiline_string_ignore_empties
import repository.local.generators.filters_generators.employees as EmployeesSqlFilterClauseGenerator
import sql_queries.meta.employees as employees


class Positions(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return employees.Positions

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': employees.Positions.get_name(),
            'where_group_limit': f'ORDER BY {employees.Positions.name}',
        }


class EmpTribes(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return employees.EmpTribes

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': employees.EmpTribes.get_name(),
            'where_group_limit': f'ORDER BY {employees.EmpTribes.name}',
        }


class EmpTents(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return employees.EmpTents

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': ', '.join(self.get_fields(kwargs)),
            'from': employees.EmpTents.get_name(),
            'where_group_limit': f'ORDER BY {employees.EmpTents.name}',
        }


class Roles(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return employees.Roles

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        return {
            'select': employees.Roles,
            'from': employees.Roles.get_name(),
            'where_group_limit': f'ORDER BY {employees.Roles.name}',
        }


class Employees(GeneralSelectAsyncQueryDescriptor):

    def get_fields_meta(self, kwargs: Mapping) -> MetaData:
        return employees.Employee

    def get_format_params(self, kwargs: Mapping) -> Mapping[str, str]:
        filter = EmployeesSqlFilterClauseGenerator.generate_positions_tribes_tents_roles_filter(
            position_ids=kwargs['position_ids'],
            tribe_ids=kwargs['tribe_ids'],
            tent_ids=kwargs['tent_ids'],
            roles=kwargs['roles'],
        )
        return {
            'select': f"DISTINCT {', '.join(self.get_fields(kwargs))}",
            'from': employees.Employees.get_name(),
            'where_group_limit':
                build_multiline_string_ignore_empties(
                    (
                        filter,
                        f'ORDER BY {employees.Employee.name}',
                    )
                )
        }
