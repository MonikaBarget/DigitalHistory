#!/usr/bin/env python
# coding: utf-8

# In[18]:


# script to read primary titles from RIS files exported from the Polish National Library
# results are written to CSV
# please note that rispy is the follow-up version of RISparser
# download and documentation: https://pypi.org/project/rispy/

import os
from pprint import pprint
import rispy

# define file path for local RIS files
filepath='C:\\Users\\mobarget\\Google Drive\\RIS_export_PolishNationalLibrary'

# define filepath as directory containing iterable files and read each file

titles=[]
for f in os.listdir(filepath): 
    print(f) # return file names, e.g. Primo_RIS_Export.ris
    f_path=os.path.join(filepath, f)
    with open(f_path, 'r', encoding="utf-8") as bibliography_file:      
        print(bibliography_file)
        
        entries=rispy.load(bibliography_file)

# entries are called based on standard RIS format
# for files deviating from this format, you may need to use a tag-key-mapper
# check rispy documentation for further details

        for entry in entries:
            title=entry['primary_title']
            print(title) # special characters are shown correctly in Jupyter notebook
            titles.append(title)
                    
outpath='C:\\Users\\mobarget\\Google Drive\\'            
out=open(os.path.join(outpath, 'ris_out.csv'), 'w', encoding="utf_8_sig") # force BOM to correctly display Polish special characters in EXCEL   
for t in titles:
    out.write(t) 
    out.write('\n')
out.close()       


# In[ ]:





# In[ ]:




