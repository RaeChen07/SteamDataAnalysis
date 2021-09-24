"""
This script analyzes data to answer research question 2, comparing how whether
or not a game is multiplayer affects the total playtime of players playing
that game
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(6, 8), sharey=True)

    # This dataset is limited, use as left side plot
    pt1 = pd.read_csv('data/100_games_play_time_1.csv')
    pt1['dummy'] = 0
    sns.stripplot(x='dummy', y='playtime_forever',
                  data=pt1, hue='is_multiplayer', ax=ax[0])

    # Create the second plot with a larger dataset
    g2 = pd.read_csv("data/not_so_common_games.csv")
    playtime = pd.read_csv("data/not_so_common_games_total_play_time.csv")
    pt2 = g2.merge(playtime, left_on="app_id", right_on="app_id", how="inner")
    pt2['dummy'] = 0
    sns.stripplot(x='dummy', y='sum(CGS.total_play_time)',
                  data=pt2, hue='is_multiplayer', ax=ax[1])

    # Export the plot
    plt.suptitle("How Multiplayer affects Overall Playtime")
    ax[0].set_title('small sample')
    ax[1].set_title('common games')
    ax[0].set_xlabel('')
    ax[1].set_xlabel('')
    ax[0].set_ylabel('Total Playtime')
    ax[1].set_ylabel('')

    plt.savefig('output/multiplayer_playtime.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
