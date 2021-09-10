# Script to replace keywords in TXT following a regex pattern

import re

infile="C:\\###\\students.txt"
outfile="C:\\###\\students_hashtags.txt"

exclude_list=["III", "VII", "VIII", "XVI", "XII" "XIII", "XIV", "NDB", "HDM", "ADB", "NDB"]
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
                
# function to replace all old names by "# + name"

    for key, value in delimiter_dict.items():
        text=text.replace(key, value)

with open(outfile, 'w', encoding="utf-8") as f:
    f.write(text)
    f.close()
