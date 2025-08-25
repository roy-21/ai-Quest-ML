'''
Even or Odd Checker:
Write a Python function called `even_or_odd` that takes an integer as input 
and returns "Even" if the number is even and "Odd" if the number is odd. 
Test the function with different numbers.
'''

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = int(input("Enter a number to check if it is even or odd: "))
print(f"The number {num} is {even_or_odd(num)}.")