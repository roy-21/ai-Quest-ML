'''
Odd Number Finder:
Write a Python program to find the first odd number from a list of integers. 
Use a `for` loop and `break` to stop the loop when the first odd number is found.
'''

# Sample list of integers
numbers = [2, 4, 8, 10, 15, 18, 21]

# Flag to check if an odd number is found
found = False

for num in numbers:
    if num % 2 != 0:
        print(f"The first odd number is: {num}")
        found = True
        break

if not found:
    print("No odd numbers found in the list.")