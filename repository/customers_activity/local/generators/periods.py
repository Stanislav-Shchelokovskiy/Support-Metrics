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
