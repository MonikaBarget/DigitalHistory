# Script written to assign students to supervision groups
# Supervisors accept a different amount of students each between 1 and 6
# Students indicate a different amount of preferences between 1 and 4 which are not ranked
# Students indicate preferences by putting their names in the "student" column of spreadsheet

# importing the modules
import random
import pandas as pd
import os
import operator

# reading the files

master="C:\\Users\\###\\Desktop\\Supervisor-matching.xlsx"
path="C:\\Users\\###\\Desktop\\BA DS student preferences 2023" # filepath for input files
frame_list=[]

df_master=pd.read_excel(master)

for item in os.listdir(path):
    file=os.path.join(path, item)
    df_file = pd.read_excel(file) # ignore_index=False, sort=False
    frame_list.append(df_file)
stud_no=len(frame_list)
print("Number of students registered: ", stud_no)
    
# merge all student columns in one dataframe

counter=0
for frame in frame_list:
    counter+=1
    try:
        stud_col=frame["Student"].squeeze() # read as SERIES, not as NP ARRAY
        student_id = "Student.{}".format(counter)
        df_master[student_id] = stud_col
        df_master.to_excel("C:\\Users\\mobarget\\Desktop\\Preferences_all.xlsx", index = True)
    except KeyError:
        print(frame, " has no column for students!")
        continue

# read new EXCEL file as dataframe
infile="C:\\Users\\mobarget\\Desktop\\Preferences_all.xlsx" 
df=pd.read_excel(infile)
student_df=df.filter(like='Student')

def getdata(student_df):
    global teachers_to_match
    global students
    # iterate over all columns with students names and call tolist() method
    students_array=[]
    for i in list(student_df):
        students_col=student_df[i].tolist()
        students_array.append(students_col)

    # flatten list of lists and keep unique values
    students_NaN = {x for l in students_array for x in l}
    students=[y for y in students_NaN if str(y) != 'nan'] # removing empty cell values
    #print(students) # show full list of participating students

    # read all supervisor names to list
    teachers=df['Name'].values.tolist()
    
    #print(teachers) # show full list of available teachers
    
    # write row count for each teacher to a dictionary to identify the least contested matches
    teacher_count={}
    for p in teachers:
        students_per_p=df.loc[df['Name']==p, ["Student.1", "Student.2", "Student.3", "Student.4", "Student.5",
                                      "Student.6", "Student.7", "Student.8", "Student.9", "Student.10", "Student.11",
                                      "Student.12", "Student.13", "Student.14", "Student.15", "Student.16", "Student.17",
                                      "Student.18", "Student.19", "Student.20", "Student.21", "Student.22", "Student.23",
                                      "Student.24", "Student.25", "Student.26", "Student.27", "Student.28", "Student.29",
                                      "Student.30", "Student.31", "Student.32", "Student.33", "Student.34", "Student.35",
                                      "Student.36", "Student.37", "Student.38", "Student.39", "Student.40", "Student.41",
                                      "Student.42", "Student.43", "Student.44", "Student.45", "Student.46", "Student.47",
                                      "Student.48", "Student.49", "Student.50", "Student.51", "Student.52", "Student.53",
                                      "Student.54", "Student.55", "Student.56", "Student.57", "Student.58", "Student.59",
                                      "Student.60", "Student.61", "Student.62", "Student.63", "Student.64", "Student.65",
                                      "Student.67", "Student.68", "Student.69", "Student.70", "Student.71", "Student.72",
                                      "Student.73", "Student.74", "Student.75", "Student.76", "Student.77", "Student.78",
                                      "Student.79", "Student.80", "Student.81", "Student.82", "Student.83"
                                      #"Student.84",
                                      #"Student.85", "Student.86", "Student.87", "Student.89", "Student.90", "Student.91"
                                      ]].values[0].tolist()
        t_count=len([z for z in students_per_p if str(z) != 'nan']) # removing empty cell values
        teacher_count[p]=t_count # add new value to dictionary
        
    # sort values in dictionary in ascending order to create least contested matches first
    sorted_teachers = dict(sorted(teacher_count.items(), key=operator.itemgetter(1))) # use reverse=True for descending order
    # get ranked list of teachers from dictionary
    teachers_to_match=sorted_teachers.keys() 
    
# match students with teachers
# each teacher is matched with "n" number of students who have indicated a preference for their group
# "n" is read from "no. of theses" column in EXCEL file

def matching(teachers_to_match):
    global matches_list
    matches_list=[]
    #random.shuffle(teachers) function to call teacher names randomly
    for t in teachers_to_match:
        theses_no=df.loc[df['Name'] == t,'No. of theses'].values[0]
        try:
            students_pref=df.loc[df['Name'] == t, ["Student.1", "Student.2", "Student.3", "Student.4", "Student.5",
                                                  "Student.6", "Student.7", "Student.8", "Student.9", "Student.10", "Student.11",
                                                  "Student.12", "Student.13", "Student.14", "Student.15", "Student.16", "Student.17",
                                                  "Student.18", "Student.19", "Student.20", "Student.21", "Student.22", "Student.23",
                                                  "Student.24", "Student.25", "Student.26", "Student.27", "Student.28", "Student.29",
                                                  "Student.30", "Student.31", "Student.32", "Student.33", "Student.34", "Student.35",
                                                  "Student.36", "Student.37", "Student.38", "Student.39", "Student.40", "Student.41",
                                                  "Student.42", "Student.43", "Student.44", "Student.45", "Student.46", "Student.47",
                                                  "Student.48", "Student.49", "Student.50", "Student.51", "Student.52", "Student.53",
                                                  "Student.54", "Student.55", "Student.56", "Student.57", "Student.58", "Student.59",
                                                  "Student.60", "Student.61", "Student.62", "Student.63", "Student.64", "Student.65",
                                                  "Student.67", "Student.68", "Student.69", "Student.70", "Student.71", "Student.72",
                                                  "Student.73", "Student.74", "Student.75", "Student.76", "Student.77", "Student.78",
                                                  "Student.79", "Student.80", "Student.81", "Student.82", "Student.83"
                                                  #"Student.84",
                                                  #"Student.85", "Student.86", "Student.87", "Student.89", "Student.90", "Student.91"
                                                  ]].values[0].tolist()
        except KeyError:
            print("KeyError: correct student columns for teacher", t)
            continue
 
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
    global num_left
    matches_list.sort()
    print((len(matches_list)), "students have been matched so far!")
    left_list=list(set(students) - set(matches_list))           
    print("Students not matched: ", left_list)
    num_left=len(left_list)

# main function
                
def main():
    getdata(student_df) # call first function
    matching(teachers_to_match) # call second function
    not_matched(matches_list) # call third function
    
    # repeat until matches with acceptable number of "left-over" students are found
    while num_left>4:
        getdata(student_df) # call first function
        matching(teachers_to_match) # call second function
        not_matched(matches_list) # call third function
        if num_left<=4:
            break
main()
