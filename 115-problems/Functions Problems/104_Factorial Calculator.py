'''
Factorial Calculator:
Write a Python function called `factorial` that takes an integer as input 
and returns its factorial. Test the function with different values.
'''

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
num = int(input("Enter a number to calculate factorial: "))
print(f"The factorial of {num} is {factorial(num)}")