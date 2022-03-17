"""
CISC 499 Project
"""

import glob
from sys import intern
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Total_Counts

def get_dataframes():
    domestic_path = 'data/Domestic'
    domestic_files = glob.glob(domestic_path + "/*.csv")

    international_path = 'data/International'
    international_files = glob.iglob(international_path + "/*.csv")

    domestic_df = pd.concat((pd.read_csv(f) for f in domestic_files), ignore_index=True)
    international_df = pd.concat((pd.read_csv(f) for f in international_files), ignore_index=True)

    domestic_df = domestic_df.loc[:,:'CLASS']
    international_df = international_df.loc[:,:'CLASS']

    domestic_df.to_pickle('domestic.pkl')
    international_df.to_pickle('international.pkl')



""" 
print(domestic_df.loc[[0]])
print(international_df.loc[[0]])
print(domestic_df.columns)
"""


if __name__ == '__main__':
    
    try:
        domestic = pd.read_pickle('domestic.pkl')
        international = pd.read_pickle('international.pkl')
    except FileNotFoundError:
        get_dataframes()
        domestic = pd.read_pickle('domestic.pkl')
        international = pd.read_pickle('international.pkl')
    

    # Covid
    print(international)

    