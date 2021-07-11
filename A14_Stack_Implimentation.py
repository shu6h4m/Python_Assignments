'''
Assignment 14
    Create a class Stack, to hold records of Student class, having following methods:
    1. To push an element on the top of the stack
    2. Pop element and display the popped element
    3. Peek the top element of the stack 
    4. Total elements in the stack

    Note: 
    1. Push is possible only when stack is not full
    2. Pop operation can be performed when stack is not empty 

Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)   
'''

class Student:
    '''
    constructor:name,course,marks,per(parameters)
    '''
    def __init__(self,name,course,marks,per = 0):
        self.name = name
        self.course = course
        self.marks = marks
        self.percentage = per

    def compute(self): #Calculating percentage
        self.percentage = sum(self.marks)/len(self.marks) 

    def __str__(self): #to return the proper format of records of student
        return f" Name: {self.name}\nCourse: {self.course}\nMarks: {self.marks}\nPercentage: {self.percentage} "

class Stack:
    '''
    Defining Stack class having following functions
    1. isEmpty()
    2. isFull()
    3. push()
    4. poop()
    5. peek()
    '''
    def __init__(self,size):
        self.stackList = []
        self.top = -1 #Assigning top element
        self.size = size 
    def isempty(self):
        if self.top == -1: #in case stack is empty
            return True
        else: #Not Empty then
            return False
    def isfull(self):
        if self.top == self.size: #in case stack is full
            return True
        else:
            return False #Not full then
    def push(self,record):
        if self.isfull():
            return f"Stack is full.Can't Add more records."
        else:
            self.stackList.append(record) #appending items to the list
            self.top=self.top+1 #adding one position to top
    def pop(self):
        if self.isempty(): 
            return f"Stack is already empty.Nothing to pop."
        else:
            pelt = self.stackList.pop() #popping the top element
            self.top=self.top-1 #decreasing top by 1
            return pelt #return popped elt
    def peek(self):
        if self.isempty(): 
            return f"Stack is empty.No peek element." #if empty
        else:
            return self.stackList[self.top] #if not returns the peek element
    def numOfElements(self):
        return self.top+1 #returns the no. of element
if __name__ == "__main__":
    stu1 = Student("ABC","MCA",[55,54,44,65,98]) #creating instance of class Student
    stu1.compute() #calling compute function

    stu2 = Student("XYZt","MCA",[08,87,44,55,98]) 
    stu2.compute() 

    myStack = Stack(5)
    myStack.push(stu1) #calling push() function
    print("-----Stack status-----")
    for i in myStack.stackList:
        print(i) #printing the elements of stack
    myStack.push(stu2) 
    print("-----Stack status-----")
    for i in myStack.stackList:
        print(i) #printing the elements of stack
    print("No. of elements in stack:",myStack.numOfElements()) 
    print("-----Popped Element-----\n",myStack.pop())
    print("-----Peek Element-----\n",myStack.peek())
    print("-----Popped Element-----\n",myStack.pop())
    print("-----Popped Element-----\n",myStack.pop())
    print("-----Peek Element-----\n",myStack.peek())
    print("-----Popped Element-----\n",myStack.pop())

    #The End