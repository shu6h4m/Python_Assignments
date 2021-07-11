'''
Class 1:
Create a class employee with following attributes:
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
'''

# CLASS DEFINITION
class Employee:

    # class variable
    BaseSalaries = {
        'WORKER' : 10000,
        'SUPERVISOR' : 15000,
        'MANAGER' : 20000
    }

    # init method with instance variables
    def __init__(self, empid, name, designation, experience):
        self.empid = empid
        self.name = name
        self.designation = designation
        self.base_salary = self.get_base_salary()
        self.experience = experience
        self.salary = self.calculate_salary()


    '''****** GETTER METHODS ******'''
    def get_empid(self):
        return self.empid

    def get_name(self):
        return self.name
    
    def get_designation(self):
        return self.designation
    
    def get_salary(self):
        return self.salary
    
    def get_experience(self):
        return self.experience

    def get_base_salary(self):
        return Employee.BaseSalaries[self.designation]


    '''****** SETTER METHODS ******'''
    def set_empid(self, new_id):
        self.empid = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_designation(self, new_designation):
        self.designation = new_designation
    
    def set_experience(self, new_experience):
        self.experience = new_experience


    '''****** OTHER INSTANCE METHODS ******'''
    def calculate_salary(self):
        '''calculates the additional salary, HRA -> adds to base salary -> returns the sum'''
        AddSal = (self.experience/100)*self.base_salary # experience percent of base salary
        HRA = (5/100)*self.base_salary  # 5% of base salary
        return self.base_salary + AddSal + HRA

    def update_salary(self):
        '''reassigns the base salary, and re-calculate the salary'''
        self.base_salary = self.get_base_salary()
        self.salary = self.calculate_salary()

    def show_details(self):
        '''To display all the details of employee'''
        print(f"Employee Id : {self.empid}")
        print(f"Name : {self.name}")
        print(f"Designation : {self.designation}")
        print(f"Salary : {self.salary}")
        print(f"Experience : {self.experience} years")

    def __str__(self):
        '''To return well-formatted string when user prints the object'''
        return f"details : (emp id = {self.empid}, name = {self.name}, designation = {self.designation}, salary = {self.salary}, experience = {self.experience})"


# DRIVER CODE
if __name__ == '__main__':

    e_id = input("Enter Employee id: ")     # take empid from user as input
    name = input("Enter name of the employee: ")    # take name from user as input
    while True:
        # keeps asking for designation until input designation is one of ('MANAGER', 'SUPERVISOR', 'WORKER')
        designation = input("Enter the Designation: ").upper()
        if designation not in ('MANAGER', 'SUPERVISOR', 'WORKER'):
            print("Invalid Designation. Only ('MANAGER', 'SUPERVISOR', 'WORKER') are valid.")
        else: break
    experience = float(input("Enter employee's experience (in years): "))   # takes experience from user as input

    emp = Employee(e_id, name, designation, experience) # calls __init__ method to create class object

    menu = '''
    **********************************************
    1. View employee id
    2. Change employee id
    3. View name
    4. Change name
    5. View designation
    6. Change designation
    7. View experience
    8. Change experience
    9. View Salary
    10. View All the details of employee
    11. View object (Call __str__)
    12. Quit
    **********************************************
    '''
    while True:
        print(menu)
        choice = int(input("Enter Your choice: "))

        print("\n")

        # 1. View employee id
        if choice == 1:
            print(f"Employee ID : {emp.get_empid()}")

        # 2. Change employee id
        elif choice == 2:
            new_id = input("Enter New Employee ID : ")
            emp.set_empid(new_id)
            print("Updated!")

        # 3. View name
        elif choice == 3:
            print(f"Name : {emp.get_name()}")

        # 4. Change name
        elif choice == 4:
            new_name = input("Enter New Name : ")
            emp.set_name(new_name)
            print("Updated!")

        # 5. View Designation
        elif choice == 5:
            print(f"Designation : {emp.designation}")

        # 6. Change Designation
        elif choice == 6:
            new_designation = input("Enter New Designation : ").upper()
            # if designation isn't one of ('MANAGER', 'SUPERVISOR', 'WORKER'), continue execution back from menu
            if designation not in ('MANAGER', 'SUPERVISOR', 'WORKER'):
                print("Invalid Designation. Only ('MANAGER', 'SUPERVISOR', 'WORKER') are valid.")
                continue
            # update designation
            emp.set_designation(new_designation)

            # with designation updated, salary must be updated too
            emp.update_salary()
            print("Updated!")

        # 7. View Experience
        elif choice == 7:
            print(f"Experience : {emp.experience} years")

        # 8. Change Experience
        elif choice == 8:
            new_experience = float(input("Enter New Experience : "))
            emp.set_experience(new_experience)

            # with experience updated, update salary too
            emp.update_salary()
            print("Updated!")

        # 9. View salary
        elif choice == 9:
            print(f"Salary : {emp.get_salary}")

        # 10. View Employee details
        elif choice == 10:
            emp.show_details()

        # 11. View object
        elif choice == 11:
            print(emp.__str__())

        # 12. Quit
        elif choice == 12:
            break

        else:
            print("Invalid Choice! Choose again.")