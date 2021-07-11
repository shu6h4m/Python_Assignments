'''
Assignment 15 (b)

Write a programme to find factorial of a number N
2. With Recursion 
     a) print factorial of all number from 1 to N
      b) print factorial of number from  N to 1.

Submitted by: Shubham Sharma
IDE Used: Visual Studio Code with Python 3.5.0     
'''
fac_list = []
def facto(N):
    '''
    Objective: To calculate Factorial of numbers Recursively
    Take an integer input as an argument
    Prints Factorials
    '''
    if N==0:
        return 1    #As Factorial of 0 is 1
    else:
        fact = N*facto(N-1)
        print("     Factorial of ",N," = ", fact) #Printing Factorials from 1 to N
        fac_list.append(fact)  # Appending the result in list to print in N to 1 order later
        return fact

def main():
    
    N = int(input("Enter the value of N : "))  #Taking user input
    print("_____________________________________")
    print("\n***** Factorials from 1 to ",N," *****")
    print("_____________________________________\n")
    facto(N) #Calling function to print factorial from 1 to N

    print("_____________________________________")
    print("\n***** Factorials from ",N," to 1 *****")  #Printing factorials in Reverse Order
    print("_____________________________________\n")
    for x in range(len(fac_list)):
        print("     Factorial of ",N-x," = ",fac_list[N-x-1])

if __name__ == "__main__":
    main() #Calling main function

'''
OutPut:

Enter the value of N : 3
_____________________________________

***** Factorials from 1 to  3  *****
_____________________________________

     Factorial of  1  =  1
     Factorial of  2  =  2
     Factorial of  3  =  6
_____________________________________

***** Factorials from  3  to 1 *****
_____________________________________

     Factorial of  3  =  6
     Factorial of  2  =  2
     Factorial of  1  =  1

C:\Users\Shu6h4m>
'''