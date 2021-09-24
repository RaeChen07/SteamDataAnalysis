"""
Author: Jack Sui
Date: March 16 2021

Queries the Steamworks API for game user ratings.
API used: https://partner.steamgames.com/doc/store/getreviews
"""

import os
import sys

from requests.sessions import Session
import pandas as pd

APP_ID_COL = "app_id"

STEAM_API_ENDPOINT = "https://store.steampowered.com/appreviews/"

STEAM_API_PARAMS = {
    "json": 1,
    "language": "all",
    "nums_per_page": 0
}


def _fetch_rating_counts(ses: Session, app_id: int) -> "tuple[int, int, int]":
    """
    Fetches the total positive and total negative review counts
    for the specified game using Steamworks API.
    If an API error occurs, both counts are returned as -1.

    Args:
        ses (Session): A requests Session object.
        app_id (int): The app ID of the game to fetch.

    Returns:
        tuple[int, int]:
            A tuple of app ID, total positive, and negative review counts.
    """
    resp = ses.get(STEAM_API_ENDPOINT + str(app_id), params=STEAM_API_PARAMS)
    data = resp.json()
    if data["success"] != 1:
        print(f"Error calling API for app {app_id}.")
        return (-1, -1)
    else:
        summary = data["query_summary"]
        return (app_id, summary["total_positive"], summary["total_negative"])


def scrape(file_name: str):
    # Read data and verify
    df = pd.read_csv(file_name)
    if APP_ID_COL not in df:
        print(f"Error: dataset is missing {APP_ID_COL} column.")
        sys.exit(1)

    # Counters
    total = len(df)
    done = 0

    # Work the magic
    print(f"Fetching review counts for {total} games")
    app_ids = df[APP_ID_COL]
    rv_counts = []
    ses = Session()
    for app_id in app_ids:
        if done % 50 == 0:
            # Progress report
            perc = done / total * 100
            print(f"{perc:.2f}% done", end="\r")
        rv_counts.append(_fetch_rating_counts(ses, app_id))
        done += 1
    print("\nSaving dataset")

    # Got all ratings, merge it to dataset on app ID
    df_rv = pd.DataFrame(
        rv_counts, columns=["app_id", "total_positive", "total_negative"])
    output = df.merge(df_rv, on="app_id")
    output.to_csv(os.path.splitext(file_name)[0] + "_scraped.csv", index=False)
    print("Done")


if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count == 1:
        # File not specified, print help
        print("Usage: python3 scrape_steam_ratings_api.py <csv_file>")
        print("Where csv_file is the path to the CSV game dataset.")
    else:
        # Take file path
        csv_file = sys.argv[1]
        if not os.path.isfile(csv_file):
            print(f"Error: specified file {csv_file} does not exist.")
            print("To get help, run the script without parameters.")
        else:
            # File exists, go ahead
            scrape(csv_file)
