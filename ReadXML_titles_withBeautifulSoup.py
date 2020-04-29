#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import os
from os.path import dirname, join
directory=("C:\\Users\\mbarg\\Documents\\corpus") # location of XML files on local drive

results=[] # create result list
for infile in os.listdir(directory):
    filename=join(directory, infile)
    indata=open(filename,"r", encoding="utf-8", errors="ignore") # UTF-8 encoding errors are ignored
    contents = indata.read()
    soup = BeautifulSoup(contents,'xml')
    titles = soup.find_all('title') # get item titles
    for title in titles:
        print(title.get_text())
        results.append(title.get_text())
print(results) # result list is shown on screen
