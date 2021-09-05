#!/usr/bin/env python
# coding: utf-8

# Script to read KEYWORDS from CSV, find them in PDF and store the page numbers in a dictionary of lists.

# PyPDF2
# https://pythonhosted.org/PyPDF2/PageObject.html

# get INDEX words from CSV file

import csv
import pandas as pd
import numpy as np

CSV_FILE='[PATH TO LOCAL CSV FILE]'

with open(CSV_FILE, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, sep=";")
    words=data['WORD'].values
    print(len(words))
    print(words[:10])
    
# extract_doc_info.py

from PyPDF2 import PdfFileReader
from PyPDF2 import utils
import os

# define INDEX words

index_words=words

# open PDF file

def extract_information(filename):
    with open(filename, 'rb') as f:
        #print(f)
        
        # create dictionary of lists for final results 
        content_all={}
        
        
# read PDF file
        try:
            pdf=PdfFileReader(filename)
            print(pdf)
            information=pdf.getDocumentInfo()
            print(information)
            number_of_pages=pdf.getNumPages()
            print("Number of pages:", number_of_pages, "\n\n")

        
# get PDF content and check index words page by page
          
            for i in index_words[:5]:
                print("TRYING TO FIND", i, ":")
                content_all[i]=[]
                i_list=[] # create list for page results per word
                
                for n in range(0, number_of_pages):
                    print("Page to check:", n, "\n\n")
                    page = pdf.getPage(n)
                    content=page.extractText()
                    if i in content:
                        print("WORD FOUND:", i, "on page", n)
                        i_list.append(n)
                    else:
                        continue
                content_all[i].append(i_list) # add list to dict
                
                        
# write dictionary of lists to new .TXT files
   
            with open(os.path.join('[PATH TO TXT FILE]'), 'w', encoding="utf-8") as outfile:
                outfile.write(str(content_all))
                outfile.close()
                
# exception handling for malformed PDFs
                    
        except utils.PdfReadError:
            print("error")
            

        
# iterate through all PDF files in directoy        

if __name__ == '__main__':
    path = '[PATH TO DIRECTORY WHERE PDF FILES ARE STORED'
    for p in os.listdir(path):
        filename=(os.path.join(path, p))
        print(filename)
        extract_information(filename)
        
print("Done")

