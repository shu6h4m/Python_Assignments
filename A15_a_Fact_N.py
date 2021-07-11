'''
Assignment 15 (a)

Write a programme to find factorial of a number N
1. Without recursion

Submitted by: Shubham Sharma
IDE Used: Visual Studio Code with Python 3.5.0 
'''

def factorial(n):
    '''
    Objective: To compute factorial of a number
    Input: Takes n as numeric value
    Return: fact as result after computing
    '''
    fact = 1 
    assert n >= 0
    for i in range(1, n+1): # for i between 1 and n, multiply fact with i
        fact *= i
    return fact     # return factorial stored in fact

def main():
    print("_____________________________________")
    n = int(input("\nEnter the value of N : ")) #Takes input from user and Type_Cast it into integer
    fact = factorial (n)
    print("\nFactorial of ",n ,"is ",fact)
    print("_____________________________________")
if __name__ == "__main__":
    main()
