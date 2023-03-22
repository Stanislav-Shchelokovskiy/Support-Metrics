from toolbox.utils.converters import Object_to_JSON
from toolbox.sql.repository import SqliteRepository
from sql_queries.index import CustomersActivitySqlPathIndex
from sql_queries.customers_activity.meta import PeriodsMeta


__repository = SqliteRepository()


def get_group_by_periods_json():
    # format should contain a valid strftime string.
    # https://sqlite.org/lang_datefunc.html
    return '''[
    { "name": "Day",        "format": "%Y-%m-%d" },
    { "name": "Week-Year",  "format": "%Y-%W" },
    { "name": "Month-Year", "format": "%Y-%m" },
    { "name": "Year",       "format": "%Y" }
]
'''


def generate_group_by_period(
    format: str,
    field: str,
    use_baseline_aligned_mode: bool,
) -> str:
    if use_baseline_aligned_mode:
        return generate_bam_group_by_period(
            format=format,
            field=field,
        )
    return generate_regular_group_by_period(
        format=format,
        field=field,
    )


def generate_regular_group_by_period(format: str, field: str) -> str:
    if format == '%Y-%W':
        return f"STRFTIME('%Y-%m-%d', {field}, 'WEEKDAY 0', '-6 DAYS')"
    return f"STRFTIME('{format}', {field})"


def generate_bam_group_by_period(format: str, field: str) -> str:
    period = {
        '%Y-%m-%d': 1.0,
        '%Y-%W': 7.0,
        '%Y-%m': 30.0,
        '%Y': 365.0,
    }[format]
    return f'CAST(CEILING(IIF({field} = 0, 1, {field}) / {period}) AS INT)'


# yapf: disable
def generate_periods(
    start: str,
    end: str,
    format: str,
) -> str:
    anchor_modifier = {
        '%Y-%m-%d': "'START OF DAY'",
        '%Y-%W': "'WEEKDAY 0', '-6 DAYS'",
        '%Y-%m': "'START OF MONTH'",
        '%Y': "'START OF YEAR'",
    }[format]

    recursive_member_modifier = {
        '%Y-%m-%d': "'+1 DAYS'",
        '%Y-%W': "'+7 DAYS'",
        '%Y-%m': "'+1 MONTHS'",
        '%Y': "'+1 YEAR'",
    }[format]

    if format == '%Y-%W':
        format = '%Y-%m-%d'

    periods = __repository.get_data(
        query_file_path=CustomersActivitySqlPathIndex.get_periods_array_path(),
        query_format_params={
                **PeriodsMeta.get_attrs(),
                'anchor_expr': f"STRFTIME('%Y-%m-%d', '{start}', {anchor_modifier})",
                'anchor_expr_formatted': f"STRFTIME('{format}', '{start}', {anchor_modifier})",
                'recursive_expr': f"STRFTIME('%Y-%m-%d', {PeriodsMeta.start}, {recursive_member_modifier})",
                'recursive_expr_formatted': f"STRFTIME('{format}', {PeriodsMeta.start}, {recursive_member_modifier})",
                'recursion_cond_expr': f"{PeriodsMeta.start} < '{end}'",
            }
    ).reset_index(drop=True)[PeriodsMeta.period].values.tolist()
    return Object_to_JSON.convert(periods)
