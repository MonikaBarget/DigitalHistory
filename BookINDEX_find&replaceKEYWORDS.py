# PyPDF2
# https://pythonhosted.org/PyPDF2/PageObject.html

# get INDEX words from CSV file, find page numbers in PDF, replace synonyme words and combine page numbers

import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import pdftotext
import os

CSV_FILE='####.csv'

with open(CSV_FILE, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, sep=";")
    words=data['WORD'].values
    print(len(words))
    print(words[:10])
    
# define INDEX words

index_words=words

# open PDF file

def extract_information(filename):
    with open(filename, 'rb') as f:

# read PDF file content
        try:
            pdf = pdftotext.PDF(f)
            print("The document has", len(pdf), "pages.")
        
# get PDF content and check index words page by page
            page_dict={}
            for i in index_words[:100]:
                print("TRYING TO FIND", i, ":")
    
                page_list=[] # create list for page results per word
                count=0
                for page in pdf:
                    count+=1
                    if i in page:
                        print(i, ",", count)
                        page_list.append(count) # CLASS = LIST
                    else:
                        continue
# replace word found in text for final index word according to mapping in CSV file
                df=DataFrame(data)
                df_count=(len(page_dict))
                print(df_count)
                new_word=df.loc[df.WORD == i, 'MAP TO'] # read new word from data frame with index
                print(new_word)
                nw=new_word[df_count] # get new word as string by data frame index
                print(nw) # print final index word to replace old synonymes
# check if nw as key already exists in dict and add OR update values
                if nw in page_dict():
                   page_dict.update({nw: page_list}) # update values if key exists # PRODUCES ERROR: 'dict' object is not callable
                else:
                    page_dict[nw]=page_list # add values for new key
                print(page_dict)
                         
# write dictionary of lists to new .TXT files
   
            with open('C:\\#####') as outfile:
                outfile.write(str(page_dict))
                outfile.close()
                
# write each list in dictionary to one row in new .CSV file

            with open('C:\\#####') as x:
                writer = csv.writer(x)
                for key, value in page_dict.items():
                    writer. writerow([key, value])
                    f.close()
               
   # exception handling for malformed PDFs
                    
        except Exception as error:
            print(error)
            pass
        
# iterate through all PDF files in directoy        

if __name__ == '__main__':
    path = 'C:\\######'
    for p in os.listdir(path):
        filename=(os.path.join(path, p))
        extract_information(filename)
        
print("Done")
