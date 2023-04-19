
# Script for creating a ranges of page numbers from lists of individual pages
# This script can be used to refine a book index.
# The script identifies consecutive page numbers in a CSV file and combines them.

import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import pdftotext
import os
from collections import defaultdict
import itertools

CSV_FILE='C:\\Users\\####\\Index_no-range.csv' # input file with lists of individual page numbers in each row

new_pages=[]
with open(CSV_FILE, encoding="ANSI", errors="ignore") as f: # file is ANSI encoded to be compatible with EXCEL
    data = pd.read_csv(f, sep=";")
    pages=data['PAGES'].values # get values from pages column in file
    
    for p in pages:
        #print(p)
        #print(type(p))
        if len(p.split(", "))>1:
            str_list=p.split(", ")
            int_list = [eval(y) for y in str_list]
            print(int_list)
            p_list=[]
            try:
                def ranges(i):
                    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
                        b = list(b)
                        yield b[0][1], b[-1][1]

                pages_list=(list(ranges(int_list))) # Output: [(0, 4), (7, 9), (11, 11)]
                #print("Input pages: ", pages_list)
            
                for l in pages_list:
                    print(p)
                    if l[0]==l[1]:
                        new_range=l[0]
                        p_list.append(new_range)
                    else:
                        new_range="–".join([str(l[0]), str(l[1])])
                        #print("Range: ", new_range)
                        p_list.append(new_range)
            
            except Exception as e:
                print(e)
                
        else:
            p_list=[p]
            
        new_pages.append(p_list)
    
    data['NEW PAGES']=new_pages
    
    display(data) # show dataframe with new pages column

 # write to new .TXT files
   
    with open('C:\\Users\\####\\Index-with-range.txt', 'w', encoding="ANSI") as outfile:
        dfAsString = data.to_string(header=False, index=False)
        outfile.write(dfAsString)

# write to new .CSV file

    with open('C:\\Users\\####\\Index-with-range.csv', 'w', encoding="ANSI") as x:
        data.to_csv(x)  
        
print("Done")

                                     


# In[ ]:





# In[ ]:





# In[ ]:




