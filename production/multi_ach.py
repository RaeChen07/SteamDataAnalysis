"""
Script for analyzing how multiplayer content affects achievement completion
percentage
Outputs a graph to multiplayer_achievement.png
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(6, 8), sharey=True)

    df = pd.read_csv('data/100_games_play_time_1.csv')
    df['dummy'] = 0
    sns.stripplot(x='dummy', y='avg_achievement_percentage',
                  data=df, hue='is_multiplayer', ax=ax[0])

    df2 = pd.read_csv("data/common_games.csv")
    achieve = pd.read_csv("data/common_games_avg_achievement_percentages.csv")
    df2 = df2.merge(achieve, left_on="app_id", right_on="app_id", how="inner")
    df2['dummy'] = 0
    sns.stripplot(x='dummy', y='average_achievement_percentage',
                  data=df2, hue='is_multiplayer', ax=ax[1])

    plt.suptitle('How Multiplayer Content affects Achievement Completion')
    ax[0].set_title("small sample")
    ax[1].set_title("common games")
    ax[0].set_ylabel('Average Achievement Completion Percentage')
    ax[1].set_ylabel("")
    ax[0].set_xlabel("")
    ax[1].set_xlabel("")

    plt.savefig('output/multiplayer_achievement.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
