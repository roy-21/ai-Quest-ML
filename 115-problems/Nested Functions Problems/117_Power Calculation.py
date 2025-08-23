'''
Power Calculation using Recursion:
Write a recursive Python function called `power` that takes two positive integers, base and exponent,
and returns the value of base raised to the exponent.
'''

def power(base, exponent):
    if exponent == 0:
        return 1  # base^0 is 1
    else:
        return base * power(base, exponent - 1)

# Taking input from the user
base = int(input("Enter the base (positive integer): "))
exponent = int(input("Enter the exponent (positive integer): "))

# Call the function and print the result
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")