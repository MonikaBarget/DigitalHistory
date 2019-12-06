import csv
import pandas as pd
import numpy as np

CSV_FILE='C:\\Users\\mobarget\\Documents\\IslandsZOTERO.csv'

with open(CSV_FILE, encoding="utf-8") as f:
    data = pd.read_csv(f, sep=",")
    data_by_col=(data[['Place']]) # Retrieve data from selected column
    print(data_by_col) # Print data from selected column
