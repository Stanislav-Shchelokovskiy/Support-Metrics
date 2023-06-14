import toolbox.sql.generators.sqlite_periods_generator as periods_generator
from sql_queries.meta import (
    TicketsWithIterationsMeta,
    BaselineAlignedModeMeta,
)


def generate_group_by_period(kwargs: dict) -> str:
    format=kwargs['group_by_period']
    field=BaselineAlignedModeMeta.days_since_baseline if kwargs['use_baseline_aligned_mode'] else TicketsWithIterationsMeta.creation_date
    
    if kwargs['use_baseline_aligned_mode']:
        return generate_bam_group_by_period(
            format=format,
            field=field,
        )
    return periods_generator.generate_group_by_period(
        format=format,
        field=field,
    )


def generate_bam_group_by_period(format: str, field: str) -> str:
    period = {
        '%Y-%m-%d': 1.0,
        '%Y-%W': 7.0,
        '%Y-%m': 30.0,
        '%Y': 365.0,
    }[format]
    return f'CAST(CEILING(IIF({field} = 0, 1, {field}) / {period}) AS INT)'
