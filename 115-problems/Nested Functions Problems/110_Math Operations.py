'''
Math Operations with User Input:
Write a Python function called `math_operations` that takes three numbers 
and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). 
The function should return the result of the specified operation on the three numbers. 
Implement the math operations as nested functions and take input from the user.
'''

def math_operations(a, b, c, operation):
    
    # Nested functions for each operation
    def add(x, y, z):
        return x + y + z
    
    def subtract(x, y, z):
        return x - y - z
    
    def multiply(x, y, z):
        return x * y * z
    
    def divide(x, y, z):
        # Handle division by zero
        if y == 0 or z == 0:
            return "Division by zero error"
        return x / y / z
    
    # Choose the operation
    if operation == 'add':
        return add(a, b, c)
    elif operation == 'subtract':
        return subtract(a, b, c)
    elif operation == 'multiply':
        return multiply(a, b, c)
    elif operation == 'divide':
        return divide(a, b, c)
    else:
        return "Invalid operation"

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
op = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Call the function and print the result
result = math_operations(num1, num2, num3, op)
print("Result:", result)