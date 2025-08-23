'''
Factorial Calculation using Recursion:
Write a recursive Python function called `factorial` that takes a non-negative integer 
as input and returns its factorial.
'''

def factorial(n):
    if n < 0:
        return "Invalid input! Enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from the user
num = int(input("Enter a non-negative integer: "))

# Call the function and print the result
result = factorial(num)
print(f"The factorial of {num} is: {result}")