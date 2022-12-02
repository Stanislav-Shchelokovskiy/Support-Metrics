from sql_queries.customers_activity.meta import TicketsWithIterationsMeta


class TribesSqlFilterClauseGenerator:

    def generate_in_filter(
        col: str,
        values: list[str],
        filter_prefix: str = 'WHERE ',
    ) -> str:
        if not values:
            return ''
        res = f'{col} IN ('
        res += ','.join([f"'{val}'" for val in values])
        res += ')'
        return filter_prefix + res


class TicketsWithIterationsAggregatesSqlFilterClauseGenerator:

    @staticmethod
    def generate_customer_groups_filter(customer_groups: list[str]) -> str:
        if not customer_groups:
            return ''
        res = 'AND ('
        res += ' OR '.join(
            [
                f"{TicketsWithIterationsMeta.user_groups} LIKE '%{group}%'"
                for group in customer_groups
            ]
        )
        res += ')'
        return res

    @staticmethod
    def generate_ticket_types_filter(tickets_types: list[int]) -> str:
        if not tickets_types:
            return ''
        res = f'AND {TicketsWithIterationsMeta.ticket_type} IN ('
        res += ','.join([str(ticket_type) for ticket_type in tickets_types])
        res += ')'
        return res

    @staticmethod
    def generate_ticket_tags_filter(tickets_tags: list[int]) -> str:
        if not tickets_tags:
            return ''
        res = 'AND ('
        res += ' OR '.join(
            [
                f"{TicketsWithIterationsMeta.ticket_tags} LIKE '%{ticket_tag}%'"
                for ticket_tag in tickets_tags
            ]
        )
        res += ')'
        return res

    @staticmethod
    def generate_tribes_filter(tribe_ids: list[str]) -> str:
        return TribesSqlFilterClauseGenerator.generate_in_filter(
            col=TicketsWithIterationsMeta.tribe_id,
            values=tribe_ids,
            filter_prefix='AND ',
        )
