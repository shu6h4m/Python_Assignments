'''
Program to print different Patterens.
Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''
s = int(input('Enter Number of Rows You Want To Print: ')) #Takes input form user

print("_______________________________________")
print("(a) First Patteren")
print("_______________________________________")

i= 1
while i<=s:
    j=1
    while j<=i:
        print(j, end="")
        j=j+1
    print()
    i=i+1

print("_______________________________________")
print("(b) 2nd Patteren")
print("_______________________________________")

for i in range(1,s+1):
    for j in range(1,s-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j, end="")
    for j in range(2,i+1):
        print(j, end="")
    print()    

print("_______________________________________")
print("(c) 3rd Patteren")
print("_______________________________________")

for i in range (s,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
    

print("_______________________________________")
print("(g) 7th Patteren")
print("_______________________________________")

for i in range(s):
    for j in range(s):
        print("*", end=" ")
    print()
    
print("_______________________________________")
print("(h) 8th Patteren")
print("_______________________________________")

for i in range(1,s+1):
    for j in range(1,s-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print("*", end="")
    for j in range(2,i+1):
        print("*", end="")
    print() 
    