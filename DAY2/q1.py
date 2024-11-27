#Write a program to check if a number is even or odd. If the number is even, print "Even Number"
#If it’s odd, print "Odd Number".Also add another condition to check if the .Also add another condition to check if the
#number is zero.

num = int(input("Enter a number: "))
if num == 0:
    print("Number is zero")
elif num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")