'''
Greatest Common Divisor (GCD) Calculator:
Write a Python function called `gcd` that takes two integers as input 
and returns their greatest common divisor. Test the function with different pairs of numbers.
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
num1, num2 = 48, 18
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}.")

# Another test
num3, num4 = 56, 98
print(f"The GCD of {num3} and {num4} is {gcd(num3, num4)}.")