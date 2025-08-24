'''
Tuple Membership Test: Write a Python program that takes an element as input and 
checks if it exists in a given tuple
'''

#define a tuple
t = (10, 20, 30, 40, 50)

# user input for element to check
x = int(input("Enter an element to check: "))

# membership test
if x in t:
    print(f"{x} exists in the tuple.")
else:
    print(f"{x} does not exist in the tuple.")