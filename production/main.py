"""
Main script, will run all the other scripts and generate all the graphs
"""

import os

import multi_playtime
import multi_ach
import machine_learning
import engagement_trend


def main():
    if not os.path.isdir("output"):
        # Create folder for plot outputs
        os.mkdir("output")

    multi_playtime.main()
    multi_ach.main()
    machine_learning.main()
    engagement_trend.main()


if __name__ == "__main__":
    main()
