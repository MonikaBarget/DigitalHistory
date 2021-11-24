# Script written to assign students to groups of different sizes for classroom debate
# judges group has only three members
# remaining students are to be assigned to two groups of approximately equal size

import random

infile="C:\\Users\\mobarget\\Desktop\\the_list.txt" # file with student names

with open(infile, encoding="utf-8") as f:
    names=f.readlines()
    
    the_list=[]
    for n in names:
        the_list.append(n)

    judges=random.sample(the_list, 3) # randomly select three students
    
    print("JUDGES:", judges)
    
    for t in the_list:
        if t in judges:
            #print(t)
            the_list.remove(t) # remove judges from list
        else:
            continue
        
    num=round(len(the_list)//2) # divide remaining list into two equally large groups (+/-1)
    
    pro_group=random.sample(the_list, num) # select pro group from list
    contra_group=[] 
    for x in the_list:
        if x in pro_group:
            continue
        else:
            contra_group.append(x) # assign all remaining students to contra group

    
    print("PRO GROUP:", pro_group)
    print("CONTRA GROUP:", contra_group)
