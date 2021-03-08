# Script for analysing data in ZOTERO using data from the DIGIKAR project
# Python library is available on github 
# documentation: https://pyzotero.readthedocs.io/en/latest/

# Script for analysing data in ZOTERO using data from the DIGIKAR project

from pyzotero import zotero 
import json
import time

time.process_time() # use time.perf_counter or time.process_time

libnumber='' # add ID of "geohumanities" group library
libtype='group' # “user” or “group”
libapikey='' # add your own ZOTERO API key generated in your account settings (cf. "feeds-api")
collectionID='' # add ID of collection within library you want to analyse 

# access your library
zot=zotero.Zotero(libnumber, libtype, libapikey) 

# count number of top-level items in ZOTERO and print result
print("There are", zot.num_items(), "items in your selected library.") 

# count number of items in selected sub-collection
my_collection=zot.collection(collectionID)
num_entries=my_collection.get('meta', {}).get('numItems')

print("The number of items in the sub-collection is: ", num_entries)

# function to repeat on each set of 100 items

tag_list=[]

def item_details(var):
    print("\n\nALL ITEMS IN COLLECTION:\n\n")
    for item in all_items:
        try:
            item_tags=item['data']['tags']
            print('\n\n Title: %s | Date: %s | Tags: %s' % (item['data']['title'], item['data']['date'], item['data']['tags']))
            for i in item_tags:
                one_tag=i['tag']
                #print("\n\n THIS IS A SINGLE TAG: ", one_tag)
                tag_list.append(one_tag)
        except KeyError:
            print("\n\n This item is a WEBPAGE SNAPSHOT: ", item['data']['key'])
    
# get all items

items=zot.collection_items(collectionID) #  get first 100 items
all_items=zot.everything(items)
item_details(all_items)
     
# show tags for selected sub-collection

select_tags=["Mainz (Stadt)", "Rhein (Fluss)"] # select tags to be counted

tags=zot.collection_tags(collectionID)
all_tags=zot.everything(tags)

for t in all_tags:
    print("Tag no. ", all_tags.index(t), ": ", t) # index and display all tags

#print("\n\n THIS IS THE TAG LIST: ", tag_list)

freq_dict={} # create dictionary to count frequency of tags
for a in tag_list:
    b=tag_list.count(a)
    freq_dict[a] = eval(str(b))

#print(freq_dict) # display dictionary
    
print("\n\n FREQUENCY OF THE SELECTED TAG:")    
for select_tag in select_tags: # show frequency of selected tags
    try:
        print(select_tag, " : ", freq_dict[select_tag])
    except KeyError:
        print(select_tag, " : ", 0)
        continue

print("\n\n Run time: ", time.process_time(), "seconds") 
print("DONE")

