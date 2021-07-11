
'''
4th assignment (b) 

This programmes takes a list of numbers as input from the user and produce the corresponding cumulative list where 
each element in the list at the index i is the sum of elements at index j<=i.

IDE Used https://www.onlinegdb.com/
'''

def cum_list(org_list): #function to get a cumulative list
    new_list=[]  # Creates an empty list
    j=0 #Initialize variable j to 0 this is used to calculate sum
    for i in range(0,len(org_list)): #Looping over length of org_list
        j+=org_list[i] #Calculating sum of elements at index j<=i.
        new_list.append(j) #Appending j to the new list
    return new_list #Returns a cumulative list 
 
def main(): # Defining main function
    list=[] #Creating an empty list
    n=int(input("Enter no. of elemnts in list : "))# Taking user input
    for i in range(n): #Looping n times to input n elements in ist from user
        ele=int(input("Enter element : "))
        list.append(ele)
    print("Entered list is : ",list) #Printing Entered list by user
    print("Cumulative list is : ",cum_list(list))#Calling function to create cumulative list and prints cumulative list

# Calling main function
if __name__ == "__main__":
    main()