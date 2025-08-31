'''
Even Number Printer:
Write a Python program to print all even numbers from 1 to 20.
Use a for loop and continue to skip odd numbers.
'''

for i in range(1, 21):   # Loop from 1 to 20
    if i % 2 != 0:       # If number is odd
        continue         # Skip odd numbers
    print(i)             # Print even numbers