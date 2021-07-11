'''
Assignment 13
  Problem: Take two tables as input from the user that represents marks of students in two subjects,
  the program should return and print the sum of marks of the students

    1. Take Input from user in Subject 1 
    2. Take input from user for Subject 2
    3. Check validity of marks
    4. Add the marks to compute total marks
    5. Print the total marks obtained

Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''
def inputMarks(studentNum):
    '''
    Function to Take input from users
    i.e it will ask for Total Number of Students Whose marks are to be added
    '''
    markList=list() 
    for i in range(studentNum):
        m1=int(input("\tEnter marks for student "+str(i+1)+":  "))
        markList.append(m1) #STATEMENT 1 Implimentation
    return markList


def MarkValid(marks):
    '''
    Function to Check the input marks i.e. marks should be between 0 to 100.
    returns TRUE if list of marks is valid otherwise returns FALSE
    '''
    for i in marks: #STATEMENT 2 Implimentation
        if (i not in range(0,101)):
            return False
    return True

#Starting Main
TotalMark=[]
studentNum=int(input("\nEnter Total Number of students:")) #Taking user input and converting to integer
print("\nEnter Marks of 1st Subject: ")
Mark1=inputMarks(studentNum)
print("\nEnter Marks of 2nd Subject: ")
Mark2=inputMarks(studentNum)

if not((MarkValid(Mark1) and MarkValid(Mark2))): #STATEMENT 3 Implimentation
    print("\n Sorry, You Have Provided Invalid Marks !!\n\n  [Obatined Marks can not exceed 100]")
else: 
    for i in range(0,studentNum): #STATEMENT 4 Implimentation
        TotalMark.append(Mark1[i] + Mark2[i]) #STATEMENT 5 Implimentation
    print("\nToatl Marks of Students Are: ",TotalMark)
