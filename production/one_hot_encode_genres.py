"""
Joins the game info dataset with the game genres dataset
and one-hot encodes all genres.
"""

import pandas as pd


def main():
    """
    Joins games and genres datasets, then one-hot
    encodes all genres.
    """
    games = pd.read_csv("data/game_info.csv")
    games = games[["app_id"]]
    genres = pd.read_csv("data/game_genres.csv")
    df = games.merge(genres, how="left", on="app_id")
    genres_1hot = pd.get_dummies(df["genre"])
    df = df[["app_id"]].join(genres_1hot).groupby("app_id") \
        .max().reset_index()
    df.to_csv("data/game_genres_onehot.csv", index=False)


if __name__ == "__main__":
    main()
