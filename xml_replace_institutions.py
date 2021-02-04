# -*- coding: cp1252 -*-
#
# Created by Pádraig Mac Carron
#
################################
#Import Libraries
from __future__ import print_function
import os
################################

'''This script was written on the 28 August 2018

In the xmls need to replace all the incorrect institutions

'''


#################################

mapping = {
'"Medical Missionaries of Mary"':"Medical Missionaries of Mary",
"Allen Library":"Military Archives of Ireland",
"American Irish Historical Society ":"American Irish Historical Society",
"American Irish Historical Society":"American Irish Historical Society",
"Irish Capuchin Provincial Archive":"Irish Capuchin Provincial Archives",
"Kerry Library Archive":"Kerry Library, Local History & Archives Department",
"Kerry Library, Tralee":"Kerry Library, Local History & Archives Department",
"Longford County Museum":"Longford County Archives Service",
"Longford Museum":"Longford County Archives Service",
"Military Archives if Ireland":"Military Archives of Ireland",
"Military Archives of Ireland.":"Military Archives of Ireland",
"Mooney family papers":"Mooney Family Papers",
"National Archive of Ireland ":"National Archives of Ireland",
"National Archive of Ireland":"National Archives of Ireland",
"National Archives Ireland":"National Archives of Ireland",
"National Archives of Ireland ":"National Archives of Ireland",
"National Archives Of Ireland":"National Archives of Ireland",
"National Archives":"National Archives of Ireland",
"National Library Ireland":"National Library of Ireland",
"National Library of Ireland ":"National Library of Ireland",
"National Library of Ireland,":"National Library of Ireland",
"National Library of Ireland.":"National Library of Ireland",
"Pubic Records Office Northern Ireland":"Public Record Office of Northern Ireland",
"Public Record Office Northern Ireland":"Public Record Office of Northern Ireland",
"Public record office of Northern Ireland":"Public Record Office of Northern Ireland",
"Public Record Office of Northern Ireland,":"Public Record Office of Northern Ireland",
"Public record,Nothern Ireland":"Public Record Office of Northern Ireland",
"Royal College of Physicians Ireland ":"Royal College of Physicians of Ireland",
"Royal College of Physicians Ireland":"Royal College of Physicians of Ireland",
"Royal College of Physicians of Ireland ":"Royal College of Physicians of Ireland",
"Royal College of Pysicians of Ireland":"Royal College of Physicians of Ireland",
"Royal College of Surgeons in Ireland":"Royal College of Surgeons in Ireland",
"Royal College of Surgeons":"Royal College of Surgeons in Ireland",
"The American Irish Historical Society":"American Irish Historical Society",
"Trinity College Dublin ":"Trinity College Dublin",
"Trinity College, Dublin ":"Trinity College Dublin",
"Trinity College, Dublin":"Trinity College Dublin",
"UCC Library, University College Cork":"UCC Library Special Collections and Archives",
"UCC Library, University College Cork":"UCC Library Special Collections and Archives",
"University College Dublin ":"University College Dublin Archives",
"University College Dublin Archives ":"University College Dublin Archives",
"University College Dublin":"University College Dublin Archives",
"University College Dublin, Archives":"University College Dublin Archives"
}

##################################
path = 'ALL LETTERS NEW TAGS/'

xmls = os.listdir(path)

#print(len(xmls))

################
def recurse():
    ans = raw_input("\ny or n?\n")
    if ans != 'y' and ans != 'n':
        recurse()
    if ans == 'y' or ans == 'n':
        return ans
#################

done = []
outpath = 'ALL LETTERS NEW INSTITUTIONS/'
try:
    os.mkdir('ALL LETTERS NEW INSTITUTIONS')
#except FileExistsError:
except WindowsError:
    done = os.listdir(outpath)



for xml in xmls:
    if xml in done:
        continue
    output = open(outpath+xml,'w')
    with open(path + xml) as f:
        for line in f:
            if '<repository ' in line:
                if '</repository>' not in line:
                    line = line.strip() + ' ' + f.readline().strip()
                tag = line.split('>')[1].split('<')[0]
                if tag in mapping:
                    print(xml)
                    ans = raw_input("Replace:\n\t" + tag + "\nwith:\n\t" + mapping[tag] + "\nin line:\n"+line.strip()+"\n\nYes(y) / No(n)?\n")
                    if ans != 'y' and ans != 'n':
                        ans = recurse()
                    if ans == 'y':
                        line = line.replace(tag,mapping[tag])
                        print("New line:\n",line.strip())
                    if ans == 'n':
                        pass
                    print('\n----------------------------------------\n')
            output.write(line)
    output.close()
                        

##print(count)                


print("\n\nCompleted")



