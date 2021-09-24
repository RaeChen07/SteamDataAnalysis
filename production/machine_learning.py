"""
Explores Research Question 1.
Loads the game info and rating dataset and uses a number of labels
to predict two kinds of game review scores using a tree model.
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def _run_model(data, title):
    """
    Runs a DecisionTreeRegressor model using the specified data
    and outputs accuracy statistics under the specified title.

    Args:
        data (tuple): Split test and train data from the output
                      of test_train_split.
        title (str): A header to print model outputs under.
    """
    feat_train, feat_test, lab_train, lab_test = data
    model = DecisionTreeRegressor()
    model.fit(feat_train, lab_train)

    train_pred = model.predict(feat_train)
    train_err = mean_squared_error(lab_train, train_pred)

    test_pred = model.predict(feat_test)
    test_err = mean_squared_error(lab_test, test_pred)

    print(title + ":")
    print(f"\tTrain error\t{train_err}")
    print(f"\tTest error\t{test_err}")
    print("\tPricey prediction\t", model.predict([[100, 1, 1]]))
    print("\tFree prediction\t\t", model.predict([[0, 1, 1]]))


def main():
    """
    Loads the dataset, computes SteamDB review scores,
    and trains tree models that predict Metacritic and SteamDB scores
    from a number of labels.
    """
    # Read data and drop unused columns
    data = pd.read_csv("data/game_info_scraped.csv")
    data = data[["price", "release_date", "rating", "is_multiplayer",
                 "total_positive", "total_negative"]]

    # Compute release month, which is more useful than year
    data['release_month'] = \
        data['release_date'].astype(str).str[5:7].astype(int)

    # Compute SteamDB review score on a 0-100 scale
    data["_total"] = data["total_positive"] + data["total_negative"]
    data["_score"] = data["total_positive"] / data["_total"]
    data["_log"] = -np.log(data["_total"] + 1)
    data["_pow"] = data["_log"].rpow(2)
    data["steamdb_rating"] = 100 * \
        (data["_score"] - (data["_score"] - 0.5) * data["_pow"])

    # Prepare data for Metacritic (drop -1 ratings)
    df_mc = data[data["rating"] > -1]
    feat_mc = df_mc[["price", "is_multiplayer", "release_month"]]
    lab_mc = df_mc["rating"]
    metacritic = train_test_split(feat_mc, lab_mc, test_size=0.3)

    # Prepare data for SteamDB (need to dropna)
    df_db = data.dropna()
    feat_db = df_db[["price", "is_multiplayer", "release_month"]]
    lab_db = df_db["steamdb_rating"]
    steamdb = train_test_split(feat_db, lab_db, test_size=0.3)

    # Create and train models
    _run_model(metacritic, "Prediction of Metacritic Score")
    _run_model(steamdb, "Prediction of SteamDB Score")


if __name__ == '__main__':
    main()
