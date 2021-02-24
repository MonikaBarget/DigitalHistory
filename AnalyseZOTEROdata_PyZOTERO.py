# Script for analysing data in ZOTERO using data from the DIGIKAR project
# Python library is available on github: https://github.com/urschrei/pyzotero 
# full PyZotero documentation: https://pyzotero.readthedocs.io/en/latest/

from pyzotero import zotero 
import urllib3
import urllib3.request
from urllib3.exceptions import HTTPError
import time
from time import sleep

libnumber='2289797' # add ID of library (in this case: Monika Barget's "geohumanities" group library)
libtype='group' # “user” or “group”
libapikey='XXXXXXXXXX' # add your own (confidential) ZOTERO API key generated in your account settings (cf. "feeds-api")
collectionID='JD5XYWJM' # add ID of sub-collection (in this case "WP3: historic maps")

# access your library
zot = zotero.Zotero(libnumber, libtype, libapikey) 

# count number of top-level items in ZOTERO and print result
print("There are", zot.num_items(), "items in your selected library.") 

# count number of items in selected sub-collection

my_collection=zot.collection(collectionID)
print("The number of items in the sub-collection is: ", my_collection.get('meta', {}).get('numItems'))

# show selected metadata for items in sub-collection

items=zot.collection_items(collectionID)

for item in items:
    if item['data'].get('date'):
        print('\n Selected metadata for sub-collection items:\n\n Title: %s | Date: %s | Tags: %s' % (item['data'].get('title', 'no title data'), item['data'].get('date', 'no date data'), item['data'].get('tags', 'no tag data')))
    else:
        continue
        
# @zotero-dev: why is this result list limited to 100?        

# show all tags for the selected sub-collection
alltags=zot.collection_tags(collectionID)
print("\n The number of tags used in the sub-collection is: ", len(alltags))
print("\n The tags currently used in the sub-collection are: ", alltags)

# @zotero-dev: why is the output limited to 100?
