import csv
import pandas as pd
import numpy as np

CSV_FILE='C:\\Users\\mobarget\\Documents\\IslandsZOTERO.csv' # define variable for input file
CSV_OUTPUT='C:\\Users\\mobarget\\Documents\\just_testing_new.csv' # define variable for output file
searchterms=['Konstanz', 'Leipzig', 'Frankfurt'] # define list of searchterms

with open(CSV_FILE, encoding="utf-8") as f: # open input file
    data = pd.read_csv(f, sep=",") # read input file as CSV
    for x in searchterms:
        data_selected=data[data.Place == x] # find all searchterms in the "place" column of the CSV file
        print(data_selected) # print selected data
        data_selected.to_csv(CSV_OUTPUT) # write selected data to output file
