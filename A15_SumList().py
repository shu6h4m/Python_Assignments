'''
Assignment 15
Given the following code, complete the defination of function sumList():
The purpose of sumList() is to take two lists as input ,
add the respective elements of the list and return the list containing sum.
'''

def sumTwoNum(x, y):#Function to return sum of two numbers
    z = x+y
    return z

def sumList(l1, l2):
    '''
    Function to return sum of all elements
    Taking input as two lists l1 and l2
    Returning the sum to l3
    '''
    l3 = [] #empty list to append elements after adding
    for i in range(len(l1)): #Run a loop for all the indexes
        l3.append(sumTwoNum(l1[i], l2[i])) 
    return l3

def main(): #Defining main Function 
    l1 = input("Enter Elements of 1st list : ").split()
    l2 = input("Enter Elements of 2nd list : ").split()

    l1 = [int(i) for i in l1]
    l2 = [int(i) for i in l2]

    l3 = sumList(l1, l2)
    print(l3)

#Driver Code
if __name__ == "__main__":
    main()