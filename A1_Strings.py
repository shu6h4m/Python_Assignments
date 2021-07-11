'''
Following Assignment will Perform following operations:
1. Take a string from user and reverse it.
2. Count Number of words in the given string.
3. Count vowels,Consonents and special Charaters in the given string.
4. Reverse each word of the given string.
5. Return Largest word of the string.
Submitted by Subham Sharma IDE Used:- https://www.onlinegdb.com/ :)
'''

#1. This function takes input from user and reverse it.

s = input("Please Enter a Sentance: ") # initializing string 
print("1. ",s[::-1])

#2. This function takes input from user and count the number of the words.

u = len(s.split())    #using split() to count words in string
print ("2.  The number of words in string are : " + str(u))


#3.This Function will Count vowels,Consonents and special Charaters in the given string

b = 0;   #b for vowel
h = 0;   #h for Consonents
a = 1;   #a for special charater
for i in range(0,len(s)):   
    #Checks whether a character is a vowel  
    if s[i] in ('a',"e","i","o","u"):  
        b = b + 1;  
    elif (s[i] >= 'a' and s[i] <= 'z'):  
        h = h + 1;
print("3.  Total number of vowel are:",b,"Total Consonents are:",h,"Total Special Character are:",a,".")


#4.This Function Reverse each word of the given string.

print("4.  Reverse words of this string are:")
print("    ",s[::-1])


#5.This Part Return The Largest word of the string.

sentence = s
m = max(sentence.split(), key=len) #Finding longest word
print("5.  Longest word is: ", m) #Displaying longest word

''' Mam, Im really very Sorry for late submission :(
    Due to Some Medical Emergency i was not able to attend the classes for last two weeks. 
    Just Started To Learn Python'''
    