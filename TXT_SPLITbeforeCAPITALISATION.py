# script to split plain text before words that have 3 capital letters or more, excluding Roman numbers and archival abbreviations
# use case: identifying biography entries for individual people in larger file listing early modern academics

import csv
import re

infile="C:\\###\\profs.txt"
outfile="C:\\###\\profs.csv"

exclude_list=["III", "VII", "VIII", "XVI", "XII" "XIII", "XIV", "NDB", "HDM", "ADB", "NDB"] # words not to be considered person names
delimiter_list=[]
delimiter_dict={}
person_list=[]
count=-1
with open(infile, 'r', encoding="utf-8") as fp:
    text=fp.read()                                                        
    pattern=r'\b[A-Z]{3,}\b' # FIND WORDS WITH AT LEAST THREE CAPITAL LETTERS
    uppercase = re.findall(pattern, text)
    #print(type(uppercase))
    for u in uppercase:
        if u in exclude_list:
            continue
        else:
            delimiter_list.append(u)
            v=('# '+str(u))
            delimiter_dict.update({u: v})
            
    print(delimiter_dict)
                
# function to replace all old names by "# + name" to split file on "#" in next step

    for key, value in delimiter_dict.items():
        text=text.replace(key, value)
        
# use new delimiter "#" to split text             

    persons=text.split("#")
    print(text)
    for p in persons:
        count += 1
        print(count) # 1056 professors
        person_list.append(p)

# write individual biographic notes to one row in CSV each

with open(outfile, 'a', encoding="utf-8") as f: 
    writer = csv.writer(f, dialect="excel")
    for i in person_list:
        writer.writerow([i])

f.close()
print("done")
