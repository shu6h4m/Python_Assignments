'''
Assignment 8 (b)
Following Program is Related to Strings and performs following tasks:
1. Count the number of elements in a string
2. Reverse of a string
3. To check whether a given string is palindrome or not
Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''

def StringLength(str):
    ''' Function to count the number of elements in a string.
        Input: 
            str : Takes a string value as input.
        Output: 
            Returns the count of number of elements in a string.
    '''
    if (str==''): #Checks whether the string "str" is empty or not.
        return 0 #If string is empty then return 0 as length of string.
    
    else: #If string "str" is not empty then execute the else code block.
        '''
        Returns the length of string by adding 1 to the
        returned result from recursive function call on string "str" 
        from (start plus one  = 1) to (end) i.e. function call on str[1:]
        '''
        return 1 + StringLength(str[1:])
        
def StringReverse(str):
    ''' Function to find the reverse of string.
        Input: 
            str : Takes String input.
        Output: 
            Returns the Reversed String.
    '''
    if (str==''): #Checks whether the string "str" is empty or not.
        return '' #If string is empty then return reverse of string as empty string.
    
    else: #Block to execute If string "str" is not empty
        '''
        Returns the reverse of string by appending the
        returned result from recursive function call on string "str" 
        from (start) to (end -1) i.e. function call on str[:-1] to last character of string i.e. str[-1]
        '''
        return str[-1] + StringReverse(str[:-1])        

def StringPalindrom(str):
    '''
    Function to check 
    whether a given string is palindrome or not using recursion
    '''
    if (str==''): #Checks whether the string "str" is empty or not.
        return True #If string is empty then return True because empty string is always a palindrome.
    
    elif (str[0]==str[-1]) and StringPalindrom(str[1:-1]):
        '''
        Checks whether the first and last charcter of string are same or not ,
        if same then recursively call function on string from (start+1 = 0+1 = 1) to (end-1) i.e. str[1:-1] to
        check the left over characters of string by comparing first and last character of remaining string.
        '''
        return True #If condition of elif is satisfied then string is palindrome so return True.
    
    else: #If above conditions are not satisfied then execute the else code block.
        return False #All above condition are not satisfied then string is not palindrome so return False    

def main(): #Defining main function
    str = input("Enter String or Word : ") #Taking input from user for string
    #Calling function to count length of string and reverse the string. 
    print("\nLength of string \"{}\" is : ".format(str),StringLength(str))
    print("\nReverse of string ",str," is : ",StringReverse(str))
        
    result = StringPalindrom(str)
    
    if (result == True) : #Checks whether variable "result" is equal to True or not.
        print("\n",str,"is a palindrome.") #If variable "result" is True then string is palindrome.
    else : #If variable "result" is not True then execute the else code block
        print("\n",str,"is not a palindrome.") #If variable "result" is False then string is not palindrome.
    
if __name__ == "__main__": #Calling main function
    main()
    
    
#The End 