"""
CISC 499 Project
"""

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

domestic_path = 'data/Domestic'
domestic_files = glob.glob(domestic_path + "/*.csv")

international_path = 'data/International'
international_files = glob.iglob(international_path + "/*.csv")

domestic_df = pd.concat((pd.read_csv(f) for f in domestic_files), ignore_index=True)
international_df = pd.concat((pd.read_csv(f) for f in international_files), ignore_index=True)


print(domestic_df.loc[[0]])
print(international_df.loc[[0]])