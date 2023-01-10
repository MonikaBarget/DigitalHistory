# Script written to assign students to supervision groups
# Supervisors accept a different amount of students each between 1 and 6
# Students indicate a different amount of preferences between 1 and 4 which are not ranked
# Students indicate preferences by putting their names in the "student" column of spreadsheet

import random
import pandas as pd

infile="C:\\Users\\###\\Supervisor-matching.xlsx" # file with supervisor and student names

# read EXCEL file as dataframe
df=pd.read_excel(infile)
student_df=df.filter(like='Student')

def getdata(student_df):
    global teachers
    global students
    # iterate over all columns with students names and call tolist() method
    students_array=[]
    for i in list(student_df):
        students_col=student_df[i].tolist()
        students_array.append(students_col)

    # flatten list of lists and keep unique values
    students_NaN = {x for l in students_array for x in l}
    students=[y for y in students_NaN if str(y) != 'nan'] # removing empty cell values
    print(students) # show full list of participating students

    # read all supervisor names to list
    teachers=df['Name'].values.tolist()
    
    print(teachers) # show full list of available teachers

# match students with teachers
# each teacher is matched with "n" number of students who have indicated a preference for their group
# "n" is read from "no. of theses" column in EXCEL file

def matching(teachers):
    global matches_list
    matches_list=[]
    for t in teachers:
        theses_no=df.loc[df['Name'] == t,'No. of theses'].values[0]
        students_pref=df.loc[df['Name'] == t, ["Student", "Student.1", "Student.2", "Student.3", "Student.4", "Student.5"]].values[0].tolist()
        students_to_match=[z for z in students_pref if str(z) != 'nan'] # removing empty cell values
        
    # make sure that each student is only assigned to a supervisor once
        for m in students_to_match[:]:
            if m in matches_list:
                students_to_match.remove(m)
          
    # exception handling for cases where sample larger than population or negative
        try:
            matches=random.sample(list(students_to_match), int(theses_no)) # randomisation
        except ValueError:
            matches=students_to_match

    # add newly assigned students to matches list so that they won't be matched again
        for m in matches:
            if str(m) in matches_list:
                continue
            else:
                matches_list.append(str(m))

        print("MATCH: ", t, theses_no, matches)
        
# show names of students who did get none of their indicated preferences

def not_matched(matches_list):
    
    left_list=[]
    matches_list.sort()
    print("Students matched so far: ", matches_list)
    for x in matches_list:
        if str(x) in students:
            continue
        else:
            left_list.append(x)
    print("Students not matched: ", left_list)

# main function
                
def main():
    getdata(student_df) # call first function
    matching(teachers) # call second function
    not_matched(matches_list) # call third function

main()
