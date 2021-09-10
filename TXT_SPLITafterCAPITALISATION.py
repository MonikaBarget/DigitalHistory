#!/usr/bin/env python
# coding: utf-8

# In[57]:


import csv
import re

infile="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Universitätsmatrikeln\\profs.txt"
outfile="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Universitätsmatrikeln\\profs.csv"

exclude_list=["III", "VII", "VIII", "XVI", "XII" "XIII", "XIV", "NDB", "HDM", "ADB", "NDB"]
delimiter_list=[]
person_list=[]
count=0
with open(infile, 'r', encoding="utf-8") as fp:
    text=fp.read()
    #print(text)                                                         
    pattern=r'\b[A-Z]{3,}\b'
    uppercase = re.findall(pattern, line)
    #print(type(uppercase))
    for u in uppercase:
        if u in exclude_list:
            print("excluded")
            continue
        else:
            print(u)
            delimiter_list.append(u)
            
                
# create regular expression dynamically
    persons=re.split(re.compile("|".join(delimiter_list)), text)
    #print(persons)
    for p in persons:
        count += 1
        print(count)
        person_list.append(join.str(delimiter_list[int(count)], p))

with open(outfile, 'a', encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in person_list:
        writer.writerow(i)
f.close()


# In[ ]:





# In[ ]:





# In[ ]:




