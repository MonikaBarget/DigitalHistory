# Import CSV for Python

import csv

# Open CSV file and count lines

with open('TestLibrary.csv', 'r', encoding="utf-8") as f:
    data=csv.reader(f, delimiter=',')
    #data.encode("utf-8")
    line_count = 0

    for row in data:
        line_count+=1

# Print number of lines in CSV file        
        
print(line_count)
