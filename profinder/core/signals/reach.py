import pandas as pd


def reach_signal(df: pd.DataFrame) -> pd.Series:
    """
    v0: raw average reach.
    """
    return df["avg_reach"].fillna(0.0)
