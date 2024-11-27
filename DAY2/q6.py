#Write a program that repeatedly asks the user for a positive number until they enter one.
# Print "Valid input received" after breaking out of the loop.

while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break
print("Valid input received")
