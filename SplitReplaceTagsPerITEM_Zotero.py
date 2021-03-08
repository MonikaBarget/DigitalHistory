#!/usr/bin/env python
# coding: utf-8

# In[63]:


# Script by Monika Barget to manipulate tags in ZOTERO with PyZotero
# Pyzotero library is available on github 
# documentation: https://pyzotero.readthedocs.io/en/latest/

from pyzotero import zotero  
import json
import time

time.process_time() # use time.perf_counter or time.process_time

libnumber='' # add your own user ID for private library or ID in URL of group-library # islands = 2287217 
libtype='group' # “user” or “group”
libapikey='' # add your own ZOTERO API key generated in your account settings (cf. "feeds-api")
collectionID=''   # island primary sources = 8S5FKI5W

# access your library
zot=zotero.Zotero(libnumber, libtype, libapikey) 

# count number of top-level items in ZOTERO and print result
print("There are", zot.num_items(), "items in your selected library.") 

# count number of items in selected sub-collection
my_collection=zot.collection(collectionID)
num_entries=my_collection.get('meta', {}).get('numItems')

print("The number of items in the sub-collection is: ", num_entries)

# identify current ZOTERO tags using double dash and spaces as separators
oldtags=[] 
oldtags=zot.tags(q=(" -- "))
# print number of old tags
print("There are", len(oldtags), "old tags that need updating.") 
# print list of old tags
print("These are the OLD TAGS to replace: ", oldtags) 
print(type(oldtags))

# create list of new tags including repetitions
newtags=[]
# create list of unique new tags
newtags_flat=[] 

for t in oldtags:
    newtag=t.split(" -- ") # split old tags after double dash and spaces
    newtags.append(newtag)
print("This is the nested list of split tags:", newtags) # print nested list of split tags

for sublist in newtags:
    for i in sublist:
        if i in newtags_flat:
            continue # avoid adding new tags twice
        else: newtags_flat.append(i) # flatten nested list
print("\n\n This is the flattened list of new tags:", newtags_flat) # print flattened list of split tags
print(len(newtags_flat), "new tags need to be added. \n\n")

# function to repeat

def item_details(var):
    for item in all_items:
        try:
            updated_tags=[]
            item_tags=item['data']['tags']
            print('\n NEW ITEM \n Title: %s | Date: %s | Tags: %s' % (item['data']['title'], item['data']['date'], item['data']['tags']))
            for i in item_tags:
                one_tag=i['tag']
                print("\n\n THIS IS A SINGLE TAG: ", one_tag)
                if one_tag in oldtags:
                    print("\n This tags needs updating!")
                    u_tags=one_tag.split(" -- ") # split old tags after double dash and spaces
                    updated_tags.append(u_tags)
                else: 
                    print("\n This tag is OK!")
                    continue
            print("\n\n NESTED LIST OF UPDATED TAGS:", updated_tags)
            flattened = [val for sublist in updated_tags for val in sublist]
            unique = list(dict.fromkeys(flattened))
            print("\n\n FLATTENED LIST OF UNIQUE ITEMS:", unique)
            try:
                print("\n TAG TO ADD: ", unique[int(count)])
                zot.add_tags(item, unique[int(count)]) # add individual new tag to affected item   
            except IndexError:
                continue
        except KeyError:
            print("\n\n This item is a website snapshot: ", item['data']['key'])
        except StopIteration:
            print("\n\n All items retrieved.")
            main()
    print("\n END OF ROUND", count)         

# iteratively call items from collection

count=(-1)
for x in range(10):
    items=zot.collection_items(collectionID) #  get first 100 items
    all_items=zot.everything(items)
    print("\n\n NO. OF ITEMS TO CHECK INCLUDING SNAPSHOTS:", len(all_items), "\n\n")
    count=count+1
    item_details(all_items)
     
print("\n\n Run time: ", time.process_time(), "seconds") 
print("DONE")


# In[ ]:





# In[ ]:




