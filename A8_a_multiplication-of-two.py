'''
Assignment 8 (a)
Programme to multiply two numbers without using multiplication operator.
It uses recursion to multuply two numbers.
Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''
def find_Product(p,q):  
    ''' Purpose: Function to multiplys two numbers without using multiplication operator. 
        Input: 
            p,q : Takes two numbers as input
        Output: 
            Returns product of numbers p and q
    '''    
    if (p==0 or q == 0): #Checks if p is 0 or q is 0 then return their product as 0
        return 0 #If any number is zero then return their product as zero.
    
    elif q == 1: #Checks if second q is equal to 1 or not.
        return p #If q is 1 then their product is equal to p so simply return p.
    
    else: #If above conditions are not satisfied so execute the else part statements.
        #This part simply adds the  p number q times i.e. product = p + p + p + ... + p (q times summision of p)
        return p+ find_Product(p,q-1) #Returns the sum of p with recursively calling function on p and q-1


def main(): #Defining main function
    p=int(input("Enter 1st Number : "))
    q=int(input("Enter 2nd Number : ")) 
    
    x=abs(p) #find absolute value of p
    y=abs(q) #find absolute value of q
    
    
    if (x<y): #function to call product function on absolute values of p and q
        '''
        Here we check wheter the negative or positive
        '''
        result=find_Product(y,x)
    else :  
        result=find_Product(x,y)
    if(p<0 and q<0):
        # If both numbers are negative then their product is positive no need to append any sign to result.
        print("\nProduct of ",p," and ",q," is : ",result)#Printing the returned result.
    elif (p<0 or q<0):
        # If any one of number is negative then their product is negative so append negative sign to result.
        print("\nProduct of ",p," and ",q," is : ",-result)#Printing the returned result.
    else:
        #As Both numbers are positive their product is also positive so no need to append any sign.
        print("\nProduct of ",p," and ",q," is : ",result )#Printing the returned result.


if __name__ == "__main__": #Calling main function
    main()