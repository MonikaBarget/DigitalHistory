# PyPDF2
# https://pythonhosted.org/PyPDF2/PageObject.html

# get INDEX words from CSV file, find page numbers in PDF, replace synonyme words and combine page numbers

import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import pdftotext
import os
from collections import defaultdict

CSV_FILE='C:\\Users\\mobarget\\Desktop\\Publications BACKUP\\BRILL_INDEX\\BRILL_INDEX_DAVID.csv'

with open(CSV_FILE, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, sep=";")
    words=data['WORD'].values
    print(len(words))
    
# define INDEX words

index_words=words

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
            for page in pdf:
                count+=1
                if i in page:
                    page_list.append(count) # CLASS = LIST
                else:
                    continue
# replace word found in text for final index word
            try:
                df=DataFrame(data)
                df_count=(len(page_dict))
                print("POSITION IN DATAFRAME:", df_count)
                new_word=df.loc[df.WORD == i, 'MAP TO'] # read new word from data frame with index
                print("WORD IN DATAFRAME:", new_word)
                nw=new_word[df_count] # get new word as string by data frame index
                print("FINAL INDEX WORD", nw) # print final index word
# check if nw as key already exists in dict and add OR update values
                if nw in page_dict.keys():
                    page_dict[nw].extend(page_list)
                    print(page_dict)
                else:
                    page_dict[nw]=page_list
                    print(page_dict)
# write original word to dictionary if mapping to new word fails
            except:
                page_dict[i]=page_list
                print(page_dict)
                
 # write dictionary of lists to new .TXT files
   
            with open('C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\BRILL\\BRILL_book.txt', 'w', encoding="utf-8") as outfile:
                outfile.write(str(page_dict))
                outfile.close()
                
# write each dictionary to one row in new .CSV file

            with open('C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\BRILL\\BRILL_book.csv', 'w', encoding="utf-8") as x:
                writer = csv.writer(x)
                for key, value in page_dict.items():
                    writer. writerow([key, value])
                    f.close()
                       
# iterate through all PDF files in directoy        

if __name__ == '__main__':
    path = 'C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\BRILL\\BRILL_IN-FILE'
    for p in os.listdir(path):
        filename=(os.path.join(path, p))
        extract_information(filename)
        
print("Done")
