import csv

# define topics for analysis and result list

topics = [',', 'men', 'man', 'husband', 'wife', 'father', 'mother', 'son', 'daughter', 'woman', 'women', "women's", 'nurse', 'soldier', 'monk', 'priest', 'nun']
letter_list=[]
occurrence_list=[]
result_counter=0

# read file

with open('Letters1.txt', 'r') as f:
    collection = f.read()

# split file

    letter=collection.split('element') # Number of items stays the same no matter what delimiter I choose!?!?

    for letter in collection:
        letter_list.append(letter)

print(collection)
print(letter)
print(len(letter_list))
        
# count occurence of selected tags

for tag in topics:
        if tag in letter_list:
            result_counter +=1    
            occurrence=(len(tag))
            occurrence_list.append(occurrence)
        else: occurrence_list.append(0)
        continue

print(occurrence_list)
print(result_counter) # This is to double-check results!

# write results into table    

with open('TagCounter.csv','w') as g:
    writer = csv.writer(g)
    writer.writerow(topics)
    writer.writerow(occurrence_list)
    
g.close()



