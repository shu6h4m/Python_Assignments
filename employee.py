'''
Assignment 9 (b) Program on classes
Program to Create a class employee with following attributes:
1. Name
2. EmpID
3. Designation: Worker/ Supervisor/Manager
4. Salary
5. Experience

Define all getter and setter methods + show method+__str__()
Calculate Salary according to Designation and experience
BaseSalary+AddSal+HRA
BaseSalary is
{10000, 15000, 20000} for Worker, Supervisor, Manager resp
AddSal=%age experience of BaseSalary
HRA=5% of BaseSalary

Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''

class employee: #class employee with atrributes name,EmpId,Designation,Salary,Experience
    
    def __init__(self,n,e,d,ex): #initializing values using contructor
        self.name=n
        self.EmpId=e
        self.Designation=d
        self.Experience=ex
        self.salary=self.get_salary(ex,d)

#getter methods for accessing values of attributes
    def get_salary(self,ex,d):
        '''
        Calculating salaries of Worker, Manager, Supervisior by mean of if else statement
        '''
        if d=="Worker":
            return 10000+(ex/100)*10000+(0.05*10000)
        elif d=="Supervisor":
            return 15000+(ex/100)*15000+(0.05*15000)
        elif d=="Manager":
            return 20000+(ex/100)*20000+(0.05*20000)

    def get_name(self):
        return self.name
    def get_empid(self):
        return self.EmpId
    def get_Designation(self):
        return self.Designation
    def get_exper(self):
        return self.Experience

# setter methods to update values     
    def set_name(self,n):
        self.name=n
    def set_empid(self,e):
        self.EmpId=e
    def set_designation(self,d):
        self.Designation=d
    def set_exp(self,ex):
        self.Experience=ex
    def set_salary(self):
        self.salary=self.get_salary(self.Experience,self.Designation)


    def __str__(self): #str function to Print all Attributes
        return "\nName: "+self.name +" || Employee ID: " +self.EmpId + " || Designation: "+ self.Designation +" || Experience: " +str(self.Experience) +" Years || Salary: " +str(self.salary)
       
    def show(self): #show function to display Data 
        print("\nName of Employee is:",n)
        print("Employee ID of Employee is:",e)
        print("Designation of Employee is:",self.Designation)
        print("Experience of Employee is:",self.Experience,"Years")
        print("Salary of Employee is:  INR",self.salary)
        
if __name__ == '__main__':
    n = input("Enter Name of the Employee: ")   # take name from user as input  
    e = input("Enter Employee id: ")     # take empid from user as input
    print("\n      ******* Hurray *******")
    print("This Employee id Belongs to Manager !!")

o1=employee(n,e,"Manager",2) #creating object of employee class
o1.show() #calling show() function
print(o1)