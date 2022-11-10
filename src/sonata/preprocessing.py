"""Functions for preprocessing text data and coordinates"""

import pandas as pd
import re
from bs4 import BeautifulSoup
import requests


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans text from punctuation, changes double spaces into single onse,
    converts strings to all lowercase.

    Args:
        data (pd.DataFrame): A pandas dataframe.

    Returns:
        pd.DataFrame: An input dataframe with cleaned text in the specified column.
    """

    df = data.replace(r"[^\w\s]+", "")
    df = df.apply(lambda x: re.sub(" +", " ", str(x)))
    df = df.apply(lambda x: str(x).lower())

    return df


def lattitude(url: str):
    """
    Extracts the lattitude coordinate from pleaides webpage.

    Args:
        url (str): A pleaides url.

    Returns:
        Lattitude coordinate found on webpage.
    """

    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    coordinates = soup.find("span", {"id": "representative-point"}).text

    return cleanCoordinates(coordinates)[0]


def longitude(url: str):
    """
    Extracts the longitude coordinate from pleaides webpage.

    Args:
        url (str): A pleaides url.

    Returns:
        Longitude coordinate found on webpage.
    """

    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    coordinates = soup.find("span", {"id": "representative-point"}).text

    return cleanCoordinates(coordinates)[1]


def cleanCoordinates(txt: str) -> str:
    """
    Removes all characters that are not numbers, commas, or points
    of lattitude and longitude coordinates found on pleaides webpage.

    Args:
        txt (str): Extracted coordinates from webpage.

    Returns:
        str: Cleaned coordinates.
    """

    txt = re.sub("[^0-9,.]", "", txt)
    txt = txt.split(",")

    return txt
