import csv
import pandas as pd
import numpy as np

CSV_FILE='C:\\Users\\mobarget\\Documents\\IslandsZOTERO.csv' # define input file
CSV_OUTPUT='C:\\Users\\mobarget\\Documents\\ZOTERO_selection.csv' # define output file

with open(CSV_FILE, encoding="utf-8") as f: # open input file
    data = pd.read_csv(f, sep=",") # read data in input file as CSV
    data_selected=data[data.Place == 'Konstanz'] # select all rows in CSV table containing "Konstanz" in the "place" column
    data_selected.to_csv(CSV_OUTPUT) # write selected rows to output file
