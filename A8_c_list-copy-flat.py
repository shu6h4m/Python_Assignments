'''
Assignment 8 (c)
Following Program is Related to Lists and Perfom following Tasks
1. Copy a list
2. Flatten a list 
Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''

def ListCopy(input_List,copy_List):
    ''' Purpose: This recursive function is designed to create a copy of list. 
        Input: 
            input_List : Takes a list of values as input.
            copy_List : Takes an empty list as input in which copy of input_List is stored.
        Output: 
            Returns "copy_List" i.e. copy of "input_List"

        e.g.
        
        I/P: input_List :  [1, 2, [9, 8, [0, 5]], [3, 4]]
        O/P: copy_List :  [1, 2, [9, 8, [0, 5]], [3, 4]]
    '''
    if input_List == []:  #If input_List is empty, it will return input_List i.e. a empty list.
        return input_List

    else:#This else block is executed when "input_List" is not empty.
        copy_List.append(input_List[0])#Append the first element of "input_List" to the "copy_List"   
        ListCopy(input_List[1:],copy_List) #Recursive call for the rest of the elements of the "input_List".
    
    return copy_List#Returns the "copy_List" i.e. the copy of "input_List"

def ListFlatten(input_List,result_List):  
    '''
        I/P: input_List :  [1, 2, [3, 4, [0, 5]], [2, 4]]
        O/P: result_List :  [1, 2, 3, 4, 0, 5, 2, 4]
    '''
    
    for i in input_List:#Loop over each element in "input_List"
        if (type(i) is not list):
            '''
            First we find the type of element "i" using type() function then checks if this is equal to "list" type,
            if "if statement" evaluates to true this means that element "i" is not a list.
            '''
            result_List.append(i)#Append the element "i" to the "result_List"
        else:
            ListFlatten(i,result_List)#Element "i" is list so call ListFlatten() function to flatten list "i" also.
    
    return result_List #Returns the "result_List" i.e. the flattened list of "input_List"

# Defining main function
def main():
    input_List = eval(input("Enter a List : ")) #Taing a list as input from user.
    copy_List=[] #Declaring empty list so that we can pass it to copy_List_Recusive() function to store copied list.
    print("\nInput List is  : ",input_List)#Printing the "input_List" inputted by user.
    #Calling the ListCopy() function and Printing the returned result.
    print("\nCopy of given list is : ",ListCopy(input_List,copy_List))
    #Declaring an empty list so that we can pass it ListFlatten() function to store flattened list.
    result_List=[]
    print("\nFlatten List is : ",ListFlatten(input_List,result_List))


if __name__ == "__main__": #Calling main function
    main()

#The End