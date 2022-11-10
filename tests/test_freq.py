import sys

sys.path.append("../src")
from calculation import freq_per_year, sum_freq_per_year
import pytest
import pandas as pd


def test_year_freq():

    data = {
        "Type": ["spatheia"],
        "Lower_date": [375.0],
        "Upper_date": [700.0],
        "Frequency": [2.0],
    }

    df = pd.DataFrame(data)

    year_freq = freq_per_year(
        data=df, lower_date="Lower_date", upper_date="Upper_date", freq="Frequency"
    )

    for value in year_freq["Freq_per_year"]:

        assert isinstance(value, float)

        assert value == 0.006153846153846154


def test_sum_freq():

    data = {
        "Type": ["spatheia"],
        "Lower_date": [375.0],
        "Upper_date": [700.0],
        "Frequency": [2.0],
        "Provenance": ["Africa"],
    }

    df = pd.DataFrame(data)

    df_freq = df.groupby(["Provenance", "Type", "Lower_date", "Upper_date"])[
        "Frequency"
    ].sum()
    df_freq = df_freq.reset_index()
    df_freq = df_freq.rename(columns={"Frequency": "Summed_freq"})

    df_freq_year = sum_freq_per_year(
        data=df_freq,
        sum_freq="Summed_freq",
        lower_date="Lower_date",
        upper_date="Upper_date",
    )

    for value in df_freq_year["Sum_freq_per_year"]:

        assert isinstance(value, float)

        assert value == 0.006153846153846154
