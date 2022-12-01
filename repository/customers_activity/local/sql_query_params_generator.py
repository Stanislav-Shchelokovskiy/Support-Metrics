from sql_queries.customers_activity.meta import TicketsWithIterationsMeta


# tickets_types: list[int]
#     tickets_tags: list[int]
#     tribes: list[str]
class TicketsWithIterationsAggregatesSqlParamsGenerator:

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
        if not tribe_ids:
            return ''
        res = f'AND {TicketsWithIterationsMeta.tribe_id} IN ('
        res += ','.join([f"'{tribe_id}'" for tribe_id in tribe_ids])
        res += ')'
        return res
