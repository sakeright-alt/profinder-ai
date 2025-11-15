import pandas as pd


def _coefficient_of_variation(series: pd.Series) -> float:
    mean = series.mean()
    if mean == 0:
        return 1.0
    return float(series.std() / mean)


def volatility_signal(df: pd.DataFrame) -> pd.Series:
    """
    v0: no time-series yet, so volatility = 0 for everyone.
    Later we plug real time-series reach here.
    """
    return pd.Series([0.0] * len(df), index=df.index)
