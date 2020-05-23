#!/usr/bin/env python
# coding: utf-8

# In[45]:


import os
import os.path
from os.path import dirname, join
import re
chunk_count=0
page_range=range(1, 1495)
delimiters=[]
results=[]
search_terms=["insul", "insel", "insuln", "inseln", "insula", "insulae"]
in_file="C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\Insularity in early modern Europe\\Hederich_SchulLexikon_cleaned.txt"
out_directory="C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\Insularity in early modern Europe\\Hederich_Lexikon_chunks"
  
with open(in_file, encoding="utf-8", errors="ignore") as f:
    data = f.read()
    print(type(data))
    for x in page_range:
        delimiter=' '.join(['----- ', str(x),' / 1494 ----- '])
        delimiters.append(delimiter)
        
# Alternative solution for creating delimiters:    
#delimiters=[f'----- {page} / 1494 ----- ' for page in range(1,1495)]
#delimiters[:5]

    print(delimiters[:5]) # looks fine
    print(type(delimiters)) # class is a list
    
def split_text(delimiters, data, maxsplit=1495):
    regexPattern = '|'.join(map(re.escape, delimiters)) # regex needed because split cannot handle variables from list
    print(regexPattern) # this output looks correct but the following function produces an empty list
    print(type(regexPattern)) # the type is a string, which is correct
    chunks=re.split(regexPattern, data) # here is where it gets stuck?  
    
def create_chunks():
    for chunk in chunks:
        chunk_count+=1
        for term in search_terms:
            if term in chunk:
                results.append(chunk)
            else:
                continue
                
print(chunk_count)                          
print("These pages contains at least one search term:", results[:15]) # script does not break but output is empty
                
        #cleanr = re.compile('-')
        #cleantext = re.sub(cleanr, '', chunk_ID)
       # print(cleantext)
        #out_file_name=os.path.join(out_directory, str(cleantext)+".txt")     
        #out_file=open(out_file_name, "w", encoding="utf-8")
       # toFile=str(chunk)
       # out_file.write(toFile)
       # out_file.close()


# In[ ]:




