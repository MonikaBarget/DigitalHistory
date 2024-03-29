# Retrieve data by keyword and retrieve line index

import csv
import pandas as pd
import numpy as np

CSV_FILE='C:\\Users\\mobarget\\Documents\\IslandsZOTERO.csv'

with open(CSV_FILE, encoding="utf-8") as f:
    data = pd.read_csv(f, sep=",")
    data_selected=data[data.Place == 'Konstanz'] # Select data by searchterm "Konstanz" in "place" column 
    print(data_selected) # Print entries that contain searchterm
    
    data_index=[] # Find line indeces for result entries
    data_index=data_selected.index.tolist()
    print(data_index) # Print indeces of result entries
    
    result_list=[] # Add lines selected by indeces to result list
    for i in data_index:
        result_list.append(data.iloc[i])
        print(result_list) # Print result list
    
with open('C:\\Users\\mobarget\\Documents\\IslandResults_new2.csv','a', encoding="utf-8") as output:
    writer = csv.writer(output)
    writer.writerow(list(data)) # Add original labels to top row of new CSV file
    writer.writerows(result_list) # Write result list to new CSV file
