# code to find page titles for Wikidata IDs with Python Wikimapper

# adapted from code snippets on https://pypi.org/project/wikimapper/

# index_enwiki-20190420.db file was separately downloaded from Wikipedia: use latest release if possible

from wikimapper import WikiMapper
import os.path

# Map Wikidata ID to Wikipedia page title

# ingest list of Wikidate entity IDs as infile

infile=("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\10_Data analysis_PhD\\Entity_list.txt")

# read infile

ID_list=[]
file = open(infile, "rt", encoding="utf-8", errors="ignore")
entities = file.readlines()
for e in entities:
    ID_list.append(e[:-1])
    
print(ID_list)
print(type(ID_list))

# path for database file

BASE_DIR="D:\\"
db_path = os.path.join(BASE_DIR, "index_enwiki-20190420.db")

# get titles

titles_result=[]
for ID in ID_list:
    try:
        mapper = WikiMapper(db_path)
        title = mapper.id_to_titles(ID)
        print(title)
        titles_result.append(title)
    except ID=="#":
        print("no entity")
        titles_result.append("#")
print(titles_result)
