#!/usr/bin/env python
# coding: utf-8
# Script for manipulating tags in ZOTERO
# library is available on github 
# documentation: https://pyzotero.readthedocs.io/en/latest/

# NOTE: this script was the first attempt to replace multiple old tags by several new tags
# it does not perform well on larger libraries
# an updated script with a different iteration process has been added to this repository

from pyzotero import zotero 
import pandas as pd

libnumber='XXXXXXX' # add your own user ID for private library or ID in URL of group-library
libtype='group' # “user” or “group”
libapikey='YYYYYYYYYYYY' # add your own ZOTERO API key generated in your account settings (cf. "feeds-api")

# access your library
zot = zotero.Zotero(libnumber, libtype, libapikey) 
# count number of top-level items in ZOTERO and print result
print("There are", zot.num_items(), "items in your selected library.") 

# identify current ZOTERO tags using double dash and spaces as separators
oldtags=[] 
oldtags=zot.tags(q=(" -- "))
# print number of old tags
print("There are", len(oldtags), "old tags that need updating.") 
# print list of old tags
print("These are the outdated tags in your library:", oldtags) 

# create list of new tags including repetitions
newtags=[]
# create list of unique new tags
newtags_flat=[] 

# split old tags after double dash and spaces
for t in oldtags:
    newtag=t.split(" -- ") 
    newtags.append(newtag)
# print nested list of split tags
print("This is the nested list of all split tags:", newtags) 

# flatten nested list and avoid repetition of new tags
for sublist in newtags:
    for i in sublist:
        if i in newtags_flat:
            continue 
        else: newtags_flat.append(i) 
# print flattened list of split tags            
print("This is the flattened list of new tags:", newtags_flat) 
print(len(newtags_flat), "new tags need to be added.")

replacetags=[] # this list is a fraction of "oldtags" but necessary as "tag" in Pyzotero only permits exact matches
for newtag_flat in newtags_flat:
    replacetags=zot.tags(q=newtag_flat) # instead of looking for " -- ", we now identify tags by individual words
    for replacetag in replacetags:
        affecteditems=zot.items(tag=replacetag) # identify items whose tags contain the particular words
        for affecteditem in affecteditems:
            zot.add_tags(affecteditem, newtag_flat) # new tags are added one by one

print("Update completed")





