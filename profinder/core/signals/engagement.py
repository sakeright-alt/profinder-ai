import numpy as np
import pandas as pd


def compute_engagement_rate(df: pd.DataFrame) -> pd.Series:
    """
    (likes + comments) / followers, safe for zero followers.
    """
    followers = df["followers"].replace(0, np.nan)
    er = (df["avg_likes"] + df["avg_comments"]) / followers
    return er.fillna(0.0)

