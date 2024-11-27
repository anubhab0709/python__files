# Define a function calculate that takes three arguments: num1, num2, and operation.
# ● Use keyword arguments to specify the operation as 'add' 'subtract' 'multiply' or 'divide'.

# ● Based on the operation, return the result of the calculation.
# Example: calculate(10, 5, operation='add') should return 15.

def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"
    
    
print(calculate(10, 5, operation='add'))