from sql_queries.customers_activity.meta import CustomersActivityMeta


class TicketsWithIterationsAggregatesSqlParamsGenerator:

    @staticmethod
    def generate_customer_groups_filter(customer_groups: list[str]) -> str:
        if not customer_groups:
            return ''
        res = 'AND ('
        res += ' OR '.join(
            [
                f"{CustomersActivityMeta.user_groups} LIKE '%{group}%'"
                for group in customer_groups
            ]
        )
        res += ')'
        return res
