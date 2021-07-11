'''
Assignment 16
Today Ms. GOOFY has to send a message to her friend but in a secure manner. She designed her own way of encoding and decoding messaging. 
Foe encoding, she assumed the following:
Given any number, she returns the corresponding text in words but in reverse order.
If it is a character, then take its ASCII value and reversed it.
Also, inserted a space between each encoded o/p.
For any special character, take it as it is

e.g. if input is : 3AD$2a
o/p:  eerht 56  86 $ owt 79

For decoding, the reverse of above is conducted.
i.e. input: eerht 56  86 $ owt 79
output: 3AD$2a
'''
numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def encode(msg):
    '''
    Function to encode the message
    Takes a string as input
    Returns the encoded message 
    '''
    msgEncode = ""    #Empty string to store encoded message
    for x in msg: #Running a loop for all the characters in a string

        # if x is numeric character, change the digit in word and reverse the word (using global tuple - numbers)
        # append " " after it
        if x.isnumeric():
            msgEncode = msgEncode + numbers[int(x)][::-1] + " "

        # if x is alphabet, take its ascii value, change it into string and reverse it
        # append " " after it
        elif x.isalpha():
            msgEncode = msgEncode + str(ord(x))[::-1] + " "

        # if x is a space, append it as it is
        elif x.isspace():
            msgEncode = msgEncode + x

        # else it must be a special character. add it to msgEncode as it is
        # append " " after it
        else:
            msgEncode = msgEncode + x + " "

    # return the encoded message
    return msgEncode

def decode(msg):
    '''
    To decode given message
    Takes a string as an input
    Returns decoded message
    '''

    msgDecode = ""    # empty string to store decoded message
    z = msg.split(" ") #If msg happens to have a two consecutive spaces, it will add empty string to the list.

    for x in z: #iterate through all the elements of list

        # if x is a number, then originally it must be an alphabet.
        # reverse x, type cast it into int and take character value corresponding to that integer
        # add that character value to msgDecode string
        if x.isnumeric():
            n = x[::-1]
            msgDecode += chr(int(n))

        # if x is string of alphabets, then originally it must be a digit
        # reverse x and compare with elements of numbers tuple.
        # add the str of index value when comparison is true
        elif x.isalpha():
            for y in range(9):
                if x[::-1] == numbers[y]:
                    msgDecode += str(y)
                    break

        # if x is empty string, then originally it must be a space
        # add space to msgDecode string
        elif not x:
            msgDecode += " "

        # else it must be a special character
        # add it as it is
        else:
            msgDecode += x

    # return decoded message string
    return msgDecode

def main():
    print("_________________________________________________")
    print("\nWhat you want to do ? \n1.Encode a message \n2.Decode a message")
    choice = int(input("\nEnter 1 or 2 : ")) #Takeing choice from user
    if choice==1:
        message = input("Enter Your Message: ")
        encoded_message = encode(message)
        print("Encoded Message Is : ",encoded_message)
        print("_________________________________________________")
    elif choice == 2:
        message = input("\nEnter Your Message: ")
        decoded_message = decode(message)
        print("Decoded Message Is : ",decoded_message)
        print("_________________________________________________")
    else:
        print("You Entered Invalid Choice !!") #if 1 or 2 not selected

if __name__ == "__main__":
    main()
'''
OutPut:
_________________________________________________

What you want to do ?
1.Encode a message
2.Decode a message

Enter 1 or 2 : 1
Enter Your Message: hello
Encoded Message Is :  401 101 801 801 111
_________________________________________________
C:\Users\Shu6h4m>
'''