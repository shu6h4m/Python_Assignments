

'''
Assignment 6 (a)
This program takes a number as input and find the sum of squares of its individual digits
and store the sum in variable 'sqdNumber_result'. 
E.g. if the number is 234, the sum is computed as (2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29)
Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''


def sumOfDigits(sqdnumber): #function to find the sum of squares of individual digits of a number.
    '''
    Input: 
            sqdnumber : Takes an integer input. 
    Output: 
            sqdNumber_result : Returns the sum of squares of individual digits of given integer.
            
    Input :   sqdnumber : 69
    Output:   sqdNumber_result : 117 (6^6 + 9^9 = 36+81 = 117)
    '''
    sqdNumber_result=0 #Declaring & Initiallizing Variable to store squared sum
    
    while(sqdnumber>0): #Checks whether the sqdnumber is greater than 0 or not
        indi = sqdnumber%10
        sqdnumber = int(sqdnumber/10)
        sqdNumber_result = sqdNumber_result + indi**2 
        
    return sqdNumber_result #Returns sum of squares of individual digits of a sqdnumber.
        

def main(): # Defining main function
    print("Program to find Sum of Squares of the Digits of the Number You Enter \U0001f600 ")
    sqdnumber = int(input("Enter Number : ")) # Taking user input
    # Calling function to find the sum of squares of individual digits of a sqdnumber and printing the returned result
    print("The Sum of Squares of Individual Digits of ",sqdnumber," is : ",sumOfDigits(sqdnumber)) 
    
# Calling main function
if __name__ == "__main__":
    main()


