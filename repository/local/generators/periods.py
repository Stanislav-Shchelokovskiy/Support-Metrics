import toolbox.sql.generators.sqlite.periods_generator as periods_generator
from repository.local.aggs import is_csi
from sql_queries.meta import (
    TicketsWithIterationsMeta,
    BaselineAlignedModeMeta,
    CSIMeta,
)


def generate_group_by_period(kwargs: dict) -> str:
    format = kwargs['group_by_period']

    if kwargs['use_baseline_aligned_mode']:
        return generate_bam_group_by_period(
            format=format,
            field=BaselineAlignedModeMeta.days_since_baseline,
        )

    return periods_generator.generate_group_by_period(
        format=format,
        field=_get_field(kwargs),
    )


def generate_bam_group_by_period(format: str, field: str) -> str:
    period = {
        '%Y-%m-%d': 1.0,
        '%Y-%W': 7.0,
        '%Y-%m': 30.0,
        '%Y': 365.0,
    }[format]
    return f'CAST(CEILING(IIF({field} = 0, 1, {field}) / {period}) AS INT)'


def _get_field(kwargs: dict):
    if is_csi(kwargs.get('metric', None)):
        return CSIMeta.date
    return TicketsWithIterationsMeta.creation_date
