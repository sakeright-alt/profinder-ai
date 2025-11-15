import pandas as pd


def story_signal(df: pd.DataFrame) -> pd.Series:
    """
    v0: just return raw story views.
    """
    return df["avg_story_views"].fillna(0.0)
