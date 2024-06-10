from toolbox.sql.generators.filter_clause_generator_factory import FilterParameterNode


def generate_percentile_filter(
    alias: str,
    percentile: FilterParameterNode,
) -> str:

    def validate_percentile(val: int | None):
        if val is not None:
            if val < 0:
                val = 0
            if val > 100:
                val = 100
        else:
            val = 100
        return val

    if percentile.include:
        return f'{alias} <= {validate_percentile(percentile.value)}'
    return f'{alias} > {validate_percentile(percentile.value)}'
