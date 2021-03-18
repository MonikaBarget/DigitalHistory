import csv

IN_FILE='C:\\Users\\mobarget\\Documents\\Zedlers_Reallexikon_IMG&OCR_Einleitung und Inhalt\\Zedler_bsb10765064.txt' # define input file

searchterms=['Land', 'Landt'] # define searchterms 
result_list=[] # create result list

with open(IN_FILE, 'r', encoding='utf-8') as f: # read file
    data = f.read()
    lines = data.split("\n") # split the file into individual lines
    
print(len(lines)) # print overall number of lines in TXT file
    
for line in lines: # look for searchterms in all lines
    for i in searchterms:
        if i in line:
            result_list.append(line) # add lines with matches to result list
        else: continue

print(len(result_list)) # print number of matching lines

with open('C:\\Users\\mobarget\\Documents\\Zedlers_Reallexikon_IMG&OCR_Einleitung und Inhalt\\ResultTable.csv','w', encoding='utf-8') as g:
    writer = csv.writer(g) # create new CSV table for results
    writer.writerows(result_list) # write each result into a new line
    
g.close() # close new CSV file


