import sys

sys.path.append("../src")
from calculation import year_freq_df, year_object_count_df
import pytest
import pandas as pd


def test_freq_df():

    data = {
        "Type": ["spatheia", "brindisi"],
        "Lower_date": [375.0, -125.0],
        "Upper_date": [700.0, -25.0],
        "Sum_freq": [2.0, 0.720000],
        "Provenance": ["adriatic italy", "adriatic italy"],
    }

    df = pd.DataFrame(data)

    df["Upper_date"] = pd.to_numeric(df["Upper_date"], errors="coerce")
    df["Lower_date"] = pd.to_numeric(df["Lower_date"], errors="coerce")
    df["Sum_freq"] = pd.to_numeric(df["Sum_freq"], errors="coerce")

    df_series = year_freq_df(
        data=df, lower_date="Lower_date", upper_date="Upper_date", sum_freq="Sum_freq"
    )

    for value in df_series:
        assert isinstance(value, float)

    assert df_series.iloc[0] == 0.72


def test_count_df():

    data = {
        "Type": ["ac1", "ac1/2"],
        "Lower_date": [1.0, 1.0],
        "Upper_date": [350.0, 350.0],
        "List_of_sites": [["alba pompeia", "verona"], ["verona"]],
        "Provenance": ["crete", "crete"],
    }

    df = pd.DataFrame(data)

    df_series = year_object_count_df(
        data=df,
        lower_date="Lower_date",
        upper_date="Upper_date",
        object_list="List_of_sites",
    )

    for value in df_series:
        assert isinstance(value, int)
        assert value == 2
