#Write a program that checks if a given string is a palindrome. T ake input from the user.

text = input("Enter a string: ")
if text == text[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")