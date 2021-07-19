'''     
This program implements the following steps using FILE HANDLING in python.
    Step 1 : Creating a file containing records of the students Marks in each subject.
    Step 2 : Read the file created in step 1, generate the marksheets of individual student and save it in a file named <studentName_rollno>.
    Step 3 : Also generate a file containing Name of students scoring highest Marks subject-wise.
 Submitted by Shubham Sharma !
'''

import os       #Importing OS module 
import pickle   #Importing pickle module

def allStudentFile(n,listSubjects): # Implementing Step 1
    '''
       Objective:   To create a file containg details of students like Roll no,Name, Marks in various subjects. 
        Input   :   Takes Total no. of students as integer
        listSubjects : Takes a list containing Name of all subjects as input
        Output :       Returns the Name of file which is created by the function that contain student's details.( file_name )
    '''

    dictStudent=dict()     #Creating an empty dictionary to store details of all students.
    for i in range(n):      #Looping n times to get details of all students.
        stu_dict=dict()     #Creating empty dictionary to store the detail of "ith" student.
        print("\nEnter details of student",i+1,":")     #Prints a statement.
        roll_no=int(input("\tEnter Roll number : "))      #Taking user input for Roll number of student.
        Name=input("\tEnter student Name : ")             #Taking user input for Name of student.
        stu_dict["Name"]=Name                           #Adding an item to the "stu_dict" dictionary with "Name" as key and assigning variable "Name" as value to it.
        print("\tMarks for each subject should be in between 0 to 100.")   #Prints a statement.
        for j in (listSubjects):                           #Looping over "listSubjects" list.
            print("\tEnter Marks for ",j," : ",end='')    #Prints a statement.
            Marks=int(input())  #Taking user input for Marks for subject "j" and type casting input to integer.
            stu_dict[j]=Marks   #Adding an item to the "stu_dict" dictionary with "j" i.e. subject-Name as key and assigning variable "Marks" as value to it.
        
        dictStudent[roll_no]=stu_dict  #Adding an item to the "dictStudent" dictionary with variable "roll_no" as key and assigning "stu_dict" dictionary as value to it.

    file_name = "All_Students_File.txt" #Creating a variable and assign the file's Name to it,the Name with which we wants to create the file.

    ''' Opens a file named in variable "file_name" in 'wb' mode and stores the returned file object in variable named "file_object".
        "w" : This Mode Opens file for writing.If file does not exist, it creates a new file. If file exists it truncates the file.
        "b" : This Mode Opens file in binary mode.
    '''
    file_object = open(file_name,"wb")
    
    pickle.dump(dictStudent, file_object)  #Serializing dictionary :translates "dictStudent" dictionary object into a serialized byte stream that can be written to "file_object". 
   
    file_object.close()     #Closing the file 

    print("\nContent successfully written to file named as --> ",os.getcwd()+"\\\""+file_name+"\"") #Printing the absolute path where the file is created.
    
    return file_name #Returns the Name of file which is created by the function that contain student's details.


def read_file(file_name):
    '''
        Purpose :   This function is designed to read a file. 
        Input   :   file_name : Takes a string value as input value i.e. the Name of the file whose contents are to be read.
        Output :    Returns the python object that contains the the contents of file.
    '''
    
    with open(file_name, 'rb') as handle:   #Opens file in "rb" mode where "r" stands for read mode and "b" stands for binary mode.
        data = handle.read()                #Reading the data from the file  
    d = pickle.loads(data)                  #Unpickling file using pickle.loads() and storing the contents of file in "d"

    return d    #Returning python object got from unpickling.


# Step 2 -> Implementation
def create_Marksheet_file(data):
    '''
        Purpose :   This function is designed to create the marksheets of individual student and save it in a file named <studentName_rollno>. 
        Input   :   data : Takes a dictionary object as input value that contains the details of all students.
        Output :    Returns nothing but creates marksheet file for each student.
    '''
    
    for i in data: #Looping over  object "data" , "data" is of type dictionary, "i" is list of all keys of dictionary which are Roll nos of students. 
        
        j=data.get(i)           #Get the value of key "i" and stored it in j which is also a dictionary.
        student_name=j['Name']  #Retrieving the Name of student for Roll no "i"
        
        stu_file_name = student_name+"_{}".format(i)+".txt" #Defining the Name of file as <studentName_rollno> to save marksheet.
    
        val_str="\n!!!*** ANNUAL MARKSHEET ***!!!\n\nStudent details and Marks in each subject are shown below :\n\n\nRoll no. = {}\n\n".format(i)
    
        for k in j: #Retrieving key-value pair for student having Roll no "i"
            val_str=val_str+k+" = {}".format(j.get(k))+"\n\n" #Appending the details to val_str to save it in file.

        stu_marksheet_file_object = open(stu_file_name,'w') #Opens a file named in variable "stu_file_name" in 'write' mode and storing the returned file object.
        stu_marksheet_file_object.write(val_str)            #Writing contents of val_str to file.
        stu_marksheet_file_object.close()                   #Closing the file
        
        #Printing the absolute path for each student where the student marksheet file is created.
        print("\nMarksheet for student with : Name =",student_name,":: Roll No =",i,"is created with file named as --> ",os.getcwd()+"\\\""+stu_file_name+"\"") 

   
# Step 3 -> Implementation
def create_Highest_Marks_subject_wise_file(data,listSubjects):
    '''
        Purpose :   This function is designed to create the file containing Name of students scoring highest Marks subject-wise. 
        Input   :   data : Takes a dictionary object as input value that contains the details of all students.
                    listSubjects : Takes a list of values as input i.e. list containing Name of all subjects.
        Output :    Returns nothing but creates a file that contains Name and Roll no. of students scoring highest Marks subject-wise.
    '''
    val_str="\n!!!*** SUBJECT WISE HIGHEST MARKS DETAILS ***!!!\n\n\n"

    for s in listSubjects: #Looping over "listSubjects" list.
        max_marks = 0               #Defining maximum Marks as 0 for subject "j".
        stu_detail_list = []        #Declaring an empty list that will be used to store Name and Roll no of students having highest Marks in subject "j".
        
        for i in data:              #Looping over  object "data" , "data" is of type dictionary, "i" is list of all keys of dictionary which are Roll nos of students. 
            j=data.get(i)           #Get the value of key "i" and stored it in j which is also a dictionary.
            if(j[s]>=max_marks):    #Checks the Marks of each student j for subject s are more or equal to max_marks or not.
                max_marks=j[s]      #If Marks of current student is more than max_marks then asssign j[s] to max_marks.
            
        for i in data:              #Looping over  object "data" , "data" is of type dictionary, "i" is list of all keys of dictionary which are Roll nos of students. 
            j=data.get(i)           #Get the value of key "i" and stored it in j which is also a dictionary.
            if(j[s]==max_marks):    #Checks the Marks of each student j for subject s are equal to max_marks or not. 
                #This for loop is used to find out the students who got highest Marks. If more than one student has highest Marks so we need to add Name of all those students.
                detail="Roll_no. = {} : ".format(i)+"Name = "+j['Name'] #String that contains Name and Roll no of student who got highest Marks.
                stu_detail_list.append(detail)  #Append Name and Roll no of student who got highest Marks to "stu_detail_list".

        val_str=val_str+"Subject : "+s+"\n\tDetails of students who got highest Marks : "+str(stu_detail_list)+"\n\tHighest Marks : "+" = {}".format(max_marks)+"\n\n"
    
        
    file_obj = open("Highest_Marks_subject_wise_file.txt",'w') #Opens a file named in variable "Highest_Marks_subject_wise_file.txt" in 'write' mode and storing the returned file object.
    file_obj.write(val_str) #Writing contents of val_str to file.
    file_obj.close()   #Closing the file

    #Printing the absolute path where the highest-Marks-subject-wise file is created.
    print("\nFile containing details of students scoring highest-Marks-subject-wise is created and named as --> ",os.getcwd()+"\\\"Highest_Marks_subject_wise_file.txt\"\n") 

    
# Defining main function
def main():
    
    # Declare a variable "no_of_students" that represnts total no.of students.
    no_of_students = int(input("\nEnter the total number of students : ")) #Taking user input and type casting string into integer type using int() function.

    # Declare a variable "no_of_subj" that represnts total no.of subjects.
    no_of_subj = int(input("\nEnter the total number of subjects : "))#Taking user input and type casting string into integer type using int() function.

    # Declare an empty list "listSubjects" that contains Name of all subjects.
    listSubjects=[]
    
    for i in range(no_of_subj): #Looping "no_of_subj" times to input subject names from user
        print("\tEnter subject",i+1,"Name : ",end='')
        listSubjects.append(input()) #Taking user input and appending it to list named "listSubjects"
        
    file_name = allStudentFile(no_of_students,listSubjects) #Calling function to input all student's details & creating file for the same & storing the returned Name of created file.

    data = read_file(file_name) #Calling read_file() function to read the contents of file and storing the returned object in variable "data".
    print("\n\"Contents of file are\" --> ",data) #Printing the contents of file.

    create_Marksheet_file(data) #Calling function to create marksheet for each student and passing variable "data" which contains details of all students.

    #Calling function to create file that contains subject wise highest Marks details and passing variable "data" which contains details of all students and "listSubjects" for subject names.
    create_Highest_Marks_subject_wise_file(data,listSubjects) 
    
# Calling main function
if __name__ == "__main__":
    main()
