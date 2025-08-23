'''
Sum of Digits using Recursion:
Write a recursive Python function called `sum_of_digits` that takes an integer as input 
and returns the sum of its digits.
'''

def sum_of_digits(n):
    n = abs(n)  # Ensure the number is non-negative
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Taking input from the user
num = int(input("Enter an integer to find the sum of its digits: "))

# Call the function and print the result
result = sum_of_digits(num)
print(f"The sum of digits of {num} is: {result}")