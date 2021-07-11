'''
Assignment_3
Program to perform following tasks:
1) Takes input from user and save it to n
2) Print Prime Numbers and their count between 1 and n.
3) Print Even And Odd Numbers between 1 to n.
Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''


def printp(n): #Defining function to print prime numbers
   
    '''
    Purpose : To print prime numbers between 1 and n
    
    Input: 
            n : Takes an integer value as an input. 
    Output: 
            Print prime numbers between 1 And n and there count.
    '''
    
    count = 0 #Declare variable count to keep track of total no.of prime numbers between 1 and n
    print("Prime numbers between 1 and ",n, " are :- ",end="");
 
    
    for i in range(2, n + 1): # Skip 1 as it is neither prime nor composite
 
        # Declare flag variable to tell if i is prime number or not
        flag = 1;
         
        #Run for loop from j = 2 to half of i and then divide i by j and if remainder is 0 then i is not prime.
        for j in range(2, ((i // 2) + 1), 1):
            if (i % j == 0): # Division to check for not prime
                flag = 0;# Set flag variable to 0 to tell that i is not prime
                break; # Loop is terminated using the break statement
 
        # flag = 1 means i is prime and flag = 0 means i is not prime
        if (flag == 1):
            print(i, end = "  "); # Prints the prime number i
            count = count + 1 #Increment count by 1 when i is prime
    
    print() # Move control to next line
    print("Total Prime numbers between 1 and ",n, " are :- ",count);
    print('''
---------------------------
    ''')
    
# Defining function to print even and odd numbers
def print_e_o(n):
    
    '''
    Purpose : This function is designed to print even and odd numbers between 1 and n
    
    Input: 
            n : Takes an integer value as an input. 
    Output: 
            Prints even and odd numbers.
    '''
    
    # Print display message
    print("Even numbers between 1 and ",n, " are :> ",end="");
 
    for i in range(1, n + 1): #Traversing each number from 1 to n with the help of for loop
        if (i % 2 == 0): # Division to check for number i is even number
            print(i, end = "  "); # Prints the even number i
                
    print() # Move control to next line
    
    # Print display message
    print("Odd numbers between 1 and ",n, " are :> ",end="");
 
    for i in range(1, n + 1): #Traversing each number from 1 to n with the help of for loop
        if (i % 2 != 0): # Division to check for number i is odd number
            print(i, end = "  "); # Prints the odd number i
 
# Defining main function
def main():
    n = int(input("Enter Any Number n :")) # Taking user input
    printp(n) # Calling function to print prime numbers
    print_e_o(n) # Calling function to print even and odd numbers
    
# Calling main function
if __name__ == "__main__":
    main()
