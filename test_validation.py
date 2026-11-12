import pandas as pd
import pytest
from trade_corridor.validation import YearWalkForwardSplit, validate_panel

def test_folds_never_share_years():
    years = pd.Series([2000,2000,2001,2001,2002,2002,2003,2003,2004,2004])
    splits = list(YearWalkForwardSplit(n_splits=3).split(years))
    assert len(splits) == 3
    for tr, va in splits:
        assert set(years.iloc[tr]).isdisjoint(set(years.iloc[va]))
        assert max(years.iloc[tr]) < min(years.iloc[va])

def test_panel_contract():
    df = pd.DataFrame({'year':[2020,2021], 'corridor':['A','A'], 'trade_value_bn_usd':[1,2]})
    assert validate_panel(df)
    with pytest.raises(ValueError):
        validate_panel(pd.concat([df,df.iloc[[0]]],ignore_index=True))
    with pytest.raises(ValueError):
        validate_panel(df.assign(trade_value_bn_usd=[-1,2]))
