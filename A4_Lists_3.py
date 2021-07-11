
'''
4th assignment (c)

This programmes takes an integer number 'n' and creates a list of n lists
such that ith list contains first five multiples of i.
'''

def create_list(n):
    ''' Purpose: This function is designed to creates a list of n lists 
        Input: 
            n: Takes an integer value as an input 
        Output: 
            Returns a list of n lists where ith list contains first five multiples of i.

        e.g.
        
        I/P: n = 5
        O/P: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
    '''
    new_list=[] # Creates an empty list
    p=0 #Intialize variable p to 0 bcz this is used for inserting elements in new_list 
    for i in range(1,n+1): #Looping for n lists
        new_list.insert(p,[]) #Insert an empty list to pth position of new_list
        q=0 #Intialize variable q to 0 bcz this is used for inserting elements in pth element of new_list
        for j in range(1,6): #Looping over ith list
            k=i*j #Storing multiple of i in k
            new_list[p].insert(q,k) #Insert multiple of i at qth position of pth element of new_list
            q=q+1 #Incrementing position for insertion in pth element of new_list
        p=p+1 #Incrementing p to insert new empty list
    return new_list #Returns a list of n lists
   
def main(): # Defining main function
    
    n=int(input("Enter A Number to See Magic : ")) # Taking user input
    print("Required List is : ",create_list(n)) #Calling function to create list of n lists and printing the list

if __name__ == "__main__": # Calling main function
    main()
    