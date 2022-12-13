from pandas import DataFrame
from toolbox.sql.repository import Repository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import (
    CustomersGroupsMeta,
    TicketsTagsMeta,
    TicketsWithIterationsMeta,
    TicketsTypesMeta,
    ReplyTypesMeta,
    ComponentsFeaturesMeta,
)


class GroupsRepository(Repository):
    """
    Loads groups we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_customers_groups_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return CustomersGroupsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return CustomersGroupsMeta.get_values()


class TagsRepository(Repository):
    """
    Loads tags we use to filter customers by.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tags_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return TicketsTagsMeta.get_attrs()

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsTagsMeta.get_values()


class RepliesTypesRepository(Repository):
    """
    Loads CAT reply types.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_replies_types_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **ReplyTypesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ReplyTypesMeta.get_values()


class ComponentsFeaturesRepository(Repository):
    """
    Loads CAT components and features.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_components_features_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **ComponentsFeaturesMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return ComponentsFeaturesMeta.get_values()


class TicketsWithIterationsRepository(Repository):
    """
    Loads customers with their tickets and iterations.
    """

    def get_main_query_path(self, kwargs: dict) -> str:
        return CustomersActivitySqlPathIndex.get_tickets_with_iterations_path()

    def get_main_query_format_params(self, kwargs: dict) -> dict[str, str]:
        return {**kwargs, **TicketsWithIterationsMeta.get_attrs()}

    def get_must_have_columns(self, kwargs: dict) -> list[str]:
        return TicketsWithIterationsMeta.get_values()


class TicketsTypesRepository(Repository):

    def get_data(self, **kwargs) -> DataFrame:
        return DataFrame(
            data={
                TicketsTypesMeta.id: [1, 2, 3, 4, 5, 6, 7, 8, 11, 122],
                TicketsTypesMeta.name:
                    [
                        'Question',
                        'Bug',
                        'Suggestion',
                        'KB',
                        'Example',
                        'Breaking Change',
                        'LSC',
                        'Security Advisory',
                        'Redirect',
                        'Internal request',
                    ]
            }
        )
