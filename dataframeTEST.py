"""
CISC 499 Project
"""

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_dataframes(bound1,bound2):
    international_path = 'data/International/'
    international_files = [international_path + str(i) + ".csv".format(i) for i in range(bound1, bound2+1)]
    international_df = pd.concat((pd.read_csv(f) for f in international_files), ignore_index=True)
    international_df.to_pickle('international.pkl')

    domestic_path = 'data/Domestic/'
    domestic_files = [domestic_path + str(i) + ".csv".format(i) for i in range(bound1, bound2 + 1)]
    domestic_df = pd.concat((pd.read_csv(f) for f in domestic_files), ignore_index=True)
    domestic_df.to_pickle('domestic.pkl')



