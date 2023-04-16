# Script for creating a book index
# get INDEX words from CSV file, find page numbers in PDF, replace synonyme words and combine page numbers
# workflow documentation: https://insulae.hypotheses.org/307

# import packages

import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import pdftotext
import os
from collections import defaultdict

# define path for mapping file

CSV_FILE='C:\\#######\\BRILL_keywords.csv' # file containing original keywords and mapping to final index words

# sample file: https://github.com/MonikaBarget/DigitalHistory/blob/master/BRILL_INDEX_12lines.csv

with open(CSV_FILE, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, sep=";")
    words=data['WORD'].values
    print(len(words))
    
# define INDEX words

index_words=words

# exclude pages containing only bibliographies and endnotes

excluded_pages=[14, 15, 16, 17, 35, 51, 52, 53, 71, 72, 73, 89, 90, 91, 92, 93, 111, 114, 158, 159, 160,
                161, 162, 163, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 216, 218, 236, 237, 238,
               239, 257, 258, 259, 260, 284, 285, 286, 287, 288, 308, 309, 310, 311, 312, 313, 314]

# open PDF file

def extract_information(filename):
    with open(filename, 'rb') as f:
# create dictionary of lists for final results 
        content_all={}
# read PDF file
        pdf = pdftotext.PDF(f)
        print("The document has", len(pdf), "pages.")
        
# get PDF content and check index words page by page
        page_dict={}
        for i in index_words:
            print("TRYING TO FIND", i, ":")
            content_all[i]=[]
            page_list=[] # create list for page results per word
            count=0
            j=(str(i)+"'s") # join strings to get keyword in genitive
            
            for page in pdf:
                count+=1
                if count in excluded_pages:
                    continue
                else:
                    if i in page:
                        page_list.append(count) # CLASS = LIST
                    if j in page:
                        page_list.append(count) # CLASS = LIST
                    else:
                        continue
# replace word found in text for final index word
            try:
                df=DataFrame(data)
                df_count=int(df[df["WORD"]== i].index.values) # get index number as integer
                print("POSITION IN DATAFRAME:", df_count)
                nw=df.at[df_count, 'MAP TO'] # get new word as string
                print("INDEX WORD:", nw) # print final index word
# check if nw as key already exists in dict and add OR update values
                if nw in page_dict.keys():
                    page_dict[nw].extend(page_list) # extend function creates duplicates
                    print(page_dict)
                else:
                    page_dict[nw]=page_list
                    print(page_dict)
# write original word to dictionary if mapping to new word fails
            except:
                page_dict[i]=page_list
                print(page_dict)
                
 # write dictionary of lists to new .TXT files
   
            with open('C:\\####\\BRILL_index.txt', 'w', encoding="utf-8") as outfile:
                outfile.write(str(page_dict))
                outfile.close()
                
# write each dictionary to one row in new .CSV file

            with open('C:\\####\\BRILL_index.csv', 'w', encoding="utf-8") as x:
                writer = csv.writer(x)
                for key, value in page_dict.items():
# remove bibliography pages, de-depulicate and sort results
                    writer.writerow([key, sorted(set(value))])
                    f.close()
                       
# iterate through all PDF files in directoy        

if __name__ == '__main__':
    path = 'C:\\####\\BRILL_IN-FILE'
    for p in os.listdir(path):
        filename=(os.path.join(path, p))
        extract_information(filename)
        
print("Done")
