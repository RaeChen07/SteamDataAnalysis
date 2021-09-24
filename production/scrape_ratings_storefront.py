"""
Webscraping script which takes a .csv with steam appid's in one column
and adds a new column of steam user percent positive rating
This is user rating, as opposed to the metacritic score in the original
dataset
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd


def main():
    print("Starting")

    games = pd.read_csv("100_games.csv")
    ratings2021 = list()

    for app_id in games["appid"]:
        print(app_id)
        source = requests.get(
                             f"https://store.steampowered.com/app/{app_id}"
                             ).text
        html_soup = BeautifulSoup(source, "lxml")
        html_soup.prettify()

        page = html_soup.find("div", class_="responsive_page_content")
        review_block = page.find("div", class_="user_reviews")
        if review_block:
            reviews = review_block.find_all("span",
                                            class_="nonresponsive_hidden "
                                            "responsive_reviewdesc")
        else:
            reviews = list()

        if reviews:  # sometimes there are no reviews

            # if reviews has two (all time and most recent) it will index to 1,
            # the second and the all time value, if there are only one,
            # then it is of all time, and will index to zero, the first
            # and only value
            percentage = reviews[len(reviews) - 1].text

            start = percentage.index("-") + 2
            # sometimes Steam doesn't have enough reviews
            try:
                ratings2021.append(int(percentage[start:start+2]))
            except ValueError:
                ratings2021.append(-1)
        else:
            ratings2021.append(-1)

    games = games.assign(ratings2021=pd.Series(ratings2021))
    games.to_csv("games_with_steam2021.csv")
    print("Completed")


if __name__ == "__main__":
    main()
