#Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# a. EnCoding: if the word contains at least 3 characters, 
# remove the first letter and  append it at the end 
# now append three random characters at the starting and the end 
# else: simply reverse the string

# b. Decoding: i. if the word contains less than 3 characters, reverse it 
# else: remove 3  random characters from start and end. 
# Now remove the last letter and append it to the beginning

import random as r


message = input("Enter the message : ")
choice = int(input("\nChose the choice : \n1 for Encoding \n2 for Decoding\n\nEnter your choice : "))




def encoder(message):
    random1=""
    random2=""
    if (len(message) >= 3) :
        first_letter = message[0]
        message = message[1: len(message)]
        message = message + first_letter
        for i in range(3):
            random1=random1+chr(r.randint( 97 , 122))
        for j in range(3):
            random2=random2+chr(r.randint( 97 , 122))
        message = random1 + message +random2
        print("Encoded message is : " +message)
    

    else : 
        message = message[::-1]
        print("Encoded Message is : " +message)



def decoder(message):
    if (len(message) < 3) :
        message = message[::-1]
        print("Decoded message is " +message)
    else:
        message = message[3: len(message)-3]
        message = message[-1] + message[0:len(message)-1]
        print(f"Decoded message is {message}")


match (choice) :
    case 1: encoder(message)
    case 2: decoder(message)




