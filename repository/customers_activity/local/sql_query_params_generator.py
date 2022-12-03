from typing import Callable, Any
from sql_queries.customers_activity.meta import TicketsWithIterationsMeta


class SqlFilterClauseGenerator:

    def generate_in_filter(
        self,
        col: str,
        values: list,
        filter_prefix: str,
        values_converter: Callable[[Any], str] = None,
    ) -> str:
        values_converter = values_converter or str

        def filter_func():
            res = f'{col} IN ('
            res += ','.join([values_converter(val) for val in values])
            res += ')'
            return res

        return self._generate_filter(
            values=values,
            filter_prefix=filter_prefix,
            get_filter=filter_func
        )

    def generate_like_filter(
        self,
        col: str,
        values: list,
        filter_prefix: str,
    ):

        def filter_func():
            res = '('
            res += ' OR '.join([f"{col} LIKE '%{value}%'" for value in values])
            res += ')'
            return res

        return self._generate_filter(
            values=values,
            filter_prefix=filter_prefix,
            get_filter=filter_func
        )

    def _generate_filter(
        self,
        values: list,
        filter_prefix: str,
        get_filter: Callable[[], str],
    ) -> str:
        if not values:
            return ''
        actual_filter = get_filter()
        return filter_prefix + actual_filter


class TicketsWithIterationsAggregatesSqlFilterClauseGenerator:

    @staticmethod
    def generate_customer_groups_filter(customer_groups: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_like_filter(
            col=TicketsWithIterationsMeta.user_groups,
            values=customer_groups,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_ticket_types_filter(tickets_types: list[int]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.ticket_type,
            values=tickets_types,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_ticket_tags_filter(tickets_tags: list[int]) -> str:
        return SqlFilterClauseGenerator().generate_like_filter(
            col=TicketsWithIterationsMeta.ticket_tags,
            values=tickets_tags,
            filter_prefix='AND ',
        )

    @staticmethod
    def generate_tribes_filter(tribe_ids: list[str]) -> str:
        return SqlFilterClauseGenerator().generate_in_filter(
            col=TicketsWithIterationsMeta.tribe_id,
            values=tribe_ids,
            values_converter=lambda val: f"'{val}'",
            filter_prefix='AND ',
        )
