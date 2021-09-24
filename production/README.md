# CSE 163 Final Project

By Rae Chen, Jason Gao, Jack Sui

[Project report](https://docs.google.com/document/d/1JVQuonFcXAL_nfpaa36mhjOVBeMgKBe6PBgygRQgXxQ/edit?usp=sharing)

## How to run

To run this project, first make sure that all the scripts are in the same directory,
with a subdirectory named 'data' containing all the .csv files. This should already
be done if downloaded alongside everything.
Each .py file is a script and can be run individually. Running main.py will just run
all of the scripts.
Run main.py from the console with `python main.py`

## Outputs

Outputs should appear in the same directory as the scripts. `machine_learning.py` has no output,
it only trains a model and reports on its training accuracy. Seeing the accuracy,
there is no reason to export the model for actual use. More details in the report.

## Dependencies

The project runs within an Ed workspace and is tested with Python 3.7.9.

Data analysis dependencies: `seaborn`, `pandas`, `matplotlib`, `sklearn`

The review score scraping script requires extra libraries.

Scraper dependencies: `beautifulsoup4`, `lxml`, `request`

## Other notes

`scrape_steam_rating` is a script that scrapes ratings and adds to .csv files. It is
not necessary to run this script, all the data used should be included. This can be
run if one wishes to use steam user percent scores instead of the metacritic scores
in the data.

For example, one may wish to look at user rating with the ML model in ML.py. The
user percent scores have been scraped into common_games_with_steam2021 and a new
column with the name ratings2021 is added. Substituting these as inputs in ML.py
will work to change the ML model to look at user rating (it does worse).

Lastly, the original dataset is linked in the report, and .sql files for organizing
that data should also be included.
