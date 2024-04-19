from collections.abc import Iterable
from pandas import DataFrame, to_datetime


def transform(df: DataFrame, dtfields: Iterable[str] = None) -> DataFrame:
    if dtfields:
        for field in dtfields:
            df[field] = to_datetime(
                df[field],
                utc=True,
            )
    return df.sort_values(by=df.columns.to_list()).reset_index(drop=True)
