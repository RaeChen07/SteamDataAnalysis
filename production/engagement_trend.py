"""
This script analyzes achievement completion and playtime based on when
a game is released
Outputs two figures, ach_avg_montly.png and playtime_avg.png
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def _get_time(string):
    """
    helper method which takes string of YYYY-MM-DD format, removes dashes so
    relative times can be compared for plotting
    also removes day, so we have data split by months
    """
    string = string[0:7]  # Drop day
    return string.replace("-", "")


def main():
    g1 = pd.read_csv("data/common_games.csv")
    g2 = pd.read_csv("data/not_so_common_games.csv")

    achieve = pd.read_csv("data/common_games_avg_achievement_percentages.csv")
    playtime = pd.read_csv("data/not_so_common_games_total_play_time.csv")

    # Create average achievement plot
    achieve = achieve.dropna()  # a lot of games do not have achievements
    achieve = g1.merge(achieve, left_on="app_id",
                       right_on="app_id", how="inner")
    # print(achieve.head())
    time = achieve["release_date"].apply(_get_time)
    achieve = achieve.assign(time=time)
    achieve = achieve[achieve["time"] != "197001"]  # invalid date
    avg_ach_mth = \
        achieve.groupby("time")["average_achievement_percentage"].mean()
    # print(type(avg_ach_mth))
    avg_ach_mth = pd.DataFrame(avg_ach_mth).reset_index()
    # Convert string dates to integer
    avg_ach_mth["time"] = avg_ach_mth["time"].apply(int)
    # print(avg_ach_mth.columns, type(avg_ach_mth))

    sns.lmplot(x="time", y="average_achievement_percentage",
               data=avg_ach_mth)

    plt.title("Average Achievement Percentage over Time")
    plt.xlabel("Release Month (YYYYMM)")
    plt.ylabel("Average Achievement Percentage")
    plt.savefig("output/ach_avg_monthly.png", bbox_inches="tight")

    # Create total play time plot
    playtime = g2.merge(playtime, left_on="app_id",
                        right_on="app_id", how="inner")
    # print(playtime.head())
    time = playtime["release_date"].apply(_get_time)
    playtime = playtime.assign(time=time)
    playtime = playtime[playtime["time"] != "197001"]
    playtime = playtime.loc[:, ["time", "sum(CGS.total_play_time)"]]
    playtime["sum(CGS.total_play_time)"] = \
        playtime["sum(CGS.total_play_time)"] / 60  # put the values in hours

    avg_play_mth = playtime.groupby(
                                    "time",
                                    )["sum(CGS.total_play_time)"].mean()
    avg_play_mth = pd.DataFrame(avg_play_mth).reset_index()
    avg_play_mth["time"] = avg_play_mth["time"].apply(int)
    # print(type(avg_play_mth))

    sns.relplot(x="time", y="sum(CGS.total_play_time)",
                data=avg_play_mth, kind="line")

    plt.title("Average Playtime of Steam Games")
    plt.xticks(rotation=30)
    plt.xlabel("Release Month (YYYYMM)")
    plt.ylabel("Total Playtime (hours)")
    plt.savefig("output/playtime_avg.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
