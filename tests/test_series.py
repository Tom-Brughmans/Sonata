import sys

sys.path.append("../src")
from plot import create_series
import pytest
import pandas as pd


def test_series():

    data = {"Tom": 5, "Sarah": 8, "Jack": 10}

    series_df = create_series(data=data, name="Names", index_name="Name")

    assert isinstance(series_df, pd.Series)
