"""Leakage-resistant chronological cross-validation for corridor-year panels."""
import numpy as np

class YearWalkForwardSplit:
    """Expanding-window splits, holding out *entire* calendar years.

    Input: a one-dimensional year series aligned to X rows. Years must be sorted
    or unsorted; indices refer to original input order. Uses the last n_splits
    years as successive one-year validation folds.
    """
    def __init__(self, n_splits=5):
        if n_splits < 1:
            raise ValueError("n_splits must be positive")
        self.n_splits = n_splits

    def split(self, years):
        years = np.asarray(years)
        unique = np.unique(years)
        if len(unique) <= self.n_splits:
            raise ValueError("Need more unique years than validation folds")
        for year in unique[-self.n_splits:]:
            train = np.flatnonzero(years < year)
            valid = np.flatnonzero(years == year)
            if not len(train) or not len(valid):
                raise ValueError("Empty fold")
            yield train, valid

    def get_n_splits(self, *args, **kwargs):
        return self.n_splits


def validate_panel(df):
    """Fail fast on common input defects, without asserting economic validity."""
    required = {'year', 'corridor', 'trade_value_bn_usd'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df[['year','corridor']].isna().any().any():
        raise ValueError("Null corridor/year identifiers")
    if df.duplicated(['year','corridor']).any():
        raise ValueError("Duplicate corridor-year keys")
    if (df['trade_value_bn_usd'].dropna() < 0).any():
        raise ValueError("Negative trade value")
    return True
