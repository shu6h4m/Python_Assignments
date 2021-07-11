'''
Assignment 9 (a) Program on Class
This program creates a laptop class and
Define all getter and setter methods + __str__()
LAPTOP
Attributes:
Brand
Processor
RAM
Color
show()

Submitted by Subham Sharma
IDE Used:- https://www.onlinegdb.com/ :)
'''


class laptop: #class laptop having attributes Brand,Processor,Ram and Color

    def __init__(self,b,p,r,c): #initializing values using contructor
        self.Brand=b
        self.Processor=p
        self.Ram=r
        self.Color=c

    #Setter methods for set the values of attributes
    def set_brand(self,b):
        self.Brand=b
    def set_processor(self,p):
        self.Processor=p
    def set_ram(self,r):
        self.Ram=r
    def set_color(self,c):
        self.Color=c

    #Getter methods to access values of attributes   
    def get_brand(self):
        return self.Brand
    def get_processor(self):
        return self.Processor
    def get_ram(self):
        return self.Ram
    def get_color(self):
        return self.Color
    
    def __str__(self): #str function defined for returning all properties
        return self.Brand+" "+self.Processor+" "+self.Ram+" "+self.Color
     
    def show(self): #function for showing all the details about laptop
         print("Brand of laptop is:",self.Brand)
         print("processor of this laptop is:",self.Processor)
         print("Ram of this laptop:",self.Ram)
         print("Color of this laptop:",self.Color,"\n")


o1=laptop("Dell","i7","12gb","Silver") #creating object of laptop cclass
o1.show() #calling show() function
o1.set_brand("lenovo") #setting new value for brand
o1.show()
print(o1)