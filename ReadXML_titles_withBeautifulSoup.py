#!/usr/bin/env python
# coding: utf-8

# In[19]:


from bs4 import BeautifulSoup
import os
from os.path import dirname, join
directory=("C:\\Users\\mbarg\\Documents\\corpus")

results=[]
for infile in os.listdir(directory):
    filename=join(directory, infile)
    indata=open(filename,"r", encoding="utf-8", errors="ignore") 
    contents = indata.read()
    soup = BeautifulSoup(contents,'xml')
    titles = soup.find_all('title')
    for title in titles:
        print(title.get_text())
        results.append(title.get_text())
print(results)
        


# In[ ]:





# In[ ]:





# In[ ]:




