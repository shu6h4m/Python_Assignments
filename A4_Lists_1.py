
'''
4th assignment (a)

This programmes takes a list of values as input parameters
and returns another list without any duplicates.

IDE Used https://www.onlinegdb.com/
'''

def remove_dup(dup_list): #This function is designed to remove duplicate elements within a list
    updated_list=[]#Creates an empty list in which we store elements without duplicacy
    for i in dup_list: #Loops over duplicate list
        if i not in updated_list :#Checks whether ith element is not in updated list 
            updated_list.append(i)#Appends ith element to updated list 
    return updated_list #Returns list without any duplicates

def main(): # Defining main function
    list=[] #Creating an empty list
    n=int(input("Enter Number of Elemnts in The List : ")) #Taking user input
    for i in range(n): #Looping n times to input n elements in ist from user
        ele=int(input("Enter Element : "))
        list.append(ele)
    print("Entered List: ",list)#Printing Entered list by user
    print("List Without Duplicates Values : ",remove_dup(list))#Calling function to remove duplicates and prints new list without duplicates.

# Calling main function
if __name__ == "__main__":
    main()
