# script to read only data selected by keyword from RIS files
# results are written to CSV
# please note that rispy is the follow-up version of RISparser
# download and documentation: https://pypi.org/project/rispy/

import os
from pprint import pprint
import rispy

# define file paths for local RIS files and final output
filepath='C:\\XXXXX'
outpath='C:\\XXXXX'

# define keyword and output lists    
keyword="yourstring"
titles=[]
wrong_ids=[]

# define filepath as directory containing iterable files and read each file
for f in os.listdir(filepath): 
    #print(f) # return file names, e.g. Primo_RIS_Export.ris
    f_path=os.path.join(filepath, f)
    with open(f_path, 'r', encoding="latin-1") as bibliography_file:      
        #print(bibliography_file) # returns RIS meta-information for file
        try:
            data=rispy.load(bibliography_file, strict=False) # accepts non-standard RIS if "strict=False"
            finddata(data) # get data via function
        except:
            OSError
            continue

# entries are called based on standard RIS format
# for files deviating from this format, you may need to use a tag-key-mapper
# check rispy documentation for further details

def finddata(x):
    try:
        title=x[0]['primary_title'] # get first and only item from list and dictionary data by key
        print(title)
        if keyword in title:    
            titles.append(title)
        else:
            wrong_id=x[0]['id'] # get first and only item from list and dictionary data by key
            wrong_ids.append(wrong_id)
    except:
        KeyError
        print("\n This item has no title: ", x[0]['id']) 
                
def exportfile(outpath): # export data to csv
    out=open(os.path.join(outpath, 'ris_out.csv'), 'w', encoding="utf_8_sig") # force BOM to correctly display special characters in EXCEL   
    for t in titles:
        out.write(t) 
        out.write('\n\n')
    out.close()       

# show or export results
print(titles)
print(wrong_ids)
exportfile(outpath)
print("done")

