import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_dataframes_inter(bound1,bound2):
    international_path = 'data/International/'
    international_files = [international_path + str(i) + ".csv".format(i) for i in range(bound1, bound2+1)]
    international_df = pd.concat((pd.read_csv(f) for f in international_files), ignore_index=True)
    return(international_df)

def get_dataframes_dom(bound1, bound2):
    domestic_path = 'data/Domestic/'
    domestic_files = [domestic_path + str(i) + ".csv".format(i) for i in range(bound1, bound2 + 1)]
    domestic_df = pd.concat((pd.read_csv(f) for f in domestic_files), ignore_index=True)
    return(domestic_df)



