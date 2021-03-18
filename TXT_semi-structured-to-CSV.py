# SCRIPT TO READ SEMI-STRUCTURED BIBLIOGRAPHIC DATA FROM TXT AND WRITE THEM TO CSV

#!/usr/bin/env python
# coding: utf-8

import os
import os.path
from os.path import dirname, join
import re
import csv

delimiters=["Geburtsbrief für ", "Aussteller: ", "S. "] # Keywords that indicate a new type of information
in_file="C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\9_INSULAE\\SignaturTitel_GeburtsbriefeMainz_1-100.txt"
out_directory="C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\9_INSULAE"
out_file=os.path.join(out_directory, "geburtsbriefe_1-99.csv")   

regexPattern= '|'.join(map(re.escape, delimiters)) # regex needed because split cannot handle variables from list
print(regexPattern)
print(type(regexPattern)) # the correct type of the regexPattern has to be a string

with open(in_file, "r", encoding="utf-8", errors="ignore") as f:
    data=f.read()

results=data.split("G /")

tobe_added_list = []
for result in results: # extracts different information from each result
    result_stripped=result.strip() # removes empty lines and whitespace at the end of each result
    if result_stripped: 
        result_string=str(result_stripped) # reads valid result as string
        result_clean=result_string.replace("\n", "").replace(",", "/").replace(";","/") # removes empty lines and replace special characters that mess up CSV
        chunks=re.split(regexPattern, result_clean) # extracts different information types from result by Regex defined above
        tobe_added_list.append(chunks)

with open(out_file, 'w', newline='', encoding="utf-8") as csvoutput: # adds data without overwriting existing content
    writer=csv.writer(csvoutput, dialect="excel")
    writer.writerows(tobe_added_list) # writes each set of bibliographic information per result to a new row
