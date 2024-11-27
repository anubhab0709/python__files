# Write a program using a match statement to implement a menu. The user should input a
# number (1 to 4) corresponding to the following actions:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide

num = int(input("Enter a number: "))

match num:
	case 1:
		print("Add")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print(num1 + num2)
	case 2:
		print("Subtract")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print(num1 - num2)
	case 3:
		print("Multiply")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print(num1 * num2)
	case 4:
		print("Divide")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		if num2 != 0:
			print(num1 / num2)
		else:
			print("Cannot divide by zero")
	case _:
		print("Invalid input")