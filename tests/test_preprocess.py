import sys

sys.path.append("../src")
from preprocessing import preprocess
import pytest
import pandas as pd
import datatest as dt


def test_preprocess():

    df = pd.read_csv(
        "../Sonata_data/SonataDataNewNew.csv",
        usecols=[
            "Amphora_type",
            "Amphora_type_upper_date",
            "Amphora_type_lower_date",
            "Site",
            "Provenance",
        ],
    )

    df = preprocess(df)
    dt.validate(df["Site"], str)
    dt.validate.regex(df["Site"], r"[^\w\s]+")
