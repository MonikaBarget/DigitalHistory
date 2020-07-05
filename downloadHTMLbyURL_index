# Script to download HTML files by URL with consecutive index numbers

# example: get newspapers data from Irish news archive website

# import packages

import requests
import urllib.request
import shutil
import os

# URL to be called

NLI="http://www.nli.ie/en/NewspapersDetails.aspx?IndexNo="

# define range of index numbers

itemIDs=range(20000)

# open files and save on drive

for ID in itemIDs:
    print(ID)
    url="http://www.nli.ie/en/NewspapersDetails.aspx?IndexNo=%s" % ID
    print(url)
    html=urllib.request.urlopen(url)
    file_name=str(ID)
    with open(os.path.join("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\10_Data analysis_PhD", file_name), 'wb') as f:
        shutil.copyfileobj(html, f)
        print("File no.", ID, "downloaded!")
                    
print("Done")
