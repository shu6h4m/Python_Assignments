'''
    Assignment 5
    Program to Perform following Tasks
    a) to count frequency of items in a given list and return the frequency.
    b) In a, also return the position of each item in the given list
    Submitted by Subham Sharma
    IDE Used:- https://www.onlinegdb.com/ :)
'''

def CountFreq(my_list): #function to count frequency of elements in a list
    '''
    Purpose: To count frequency 
        Input:
        my_list =[1, 3, 1, 3, 1, 2, 2, 2]
        Output:
        For frequency :
        Item:Frequecy:
        1 : 3
        2 : 3
        3 : 2
    '''
     
    freq = {}# Creating an empty dictionary 
    for item in my_list: #pick each item from list 
        if (item in freq): #check if that item is already in dictionary key
            freq[item] += 1 #increment if already
        else: 
            freq[item] = 1 #else add item as dictionary key and put value as 1
  
    return freq #returning dictionary


def PositionItem(my_list): #Function to return the position of each item in the given list
    '''
    Purpose: to return position of items in list
        Input: 
            my_list:the list in which frequency of items is to be counted
        Output:
            returns the dictionary with positions of each item
    '''
    freq = {} #Empty dictionary Created
    i=0
    for item in my_list: #Selecting every item from the list 
        if (item in freq): #check if the item is already in dictionary key
            freq.setdefault(item,[]).append(i) #append index in value
        else: 
            freq.setdefault(item,[]).append(i) 
        i+=1
    return freq #returning dictionary    

def main(): #main function
    my_list =[2,3,3,2,4,5,5,4,1,1,3,2,4,2] #list
    print("Output:")
    print("For frequency :")
    print("Element :  Frequecy")
    freq=CountFreq(my_list) #Calling function to count frquency of items in list
    for k, v in freq.items(): 
        print (k,":", v) 
    freq=PositionItem(my_list)#Calling function to return position of items in list on freshers day
    print("For frequency :")
    print("Element :  [Positions]")
    for k, v in freq.items(): 
        print (k,":", v) 
    
if __name__ == "__main__": #Calling main function 
    main()