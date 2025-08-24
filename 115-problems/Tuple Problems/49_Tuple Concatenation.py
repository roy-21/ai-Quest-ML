'''
Tuple Concatenation: Write a Python program to concatenate two tuples and create 
a new tuple.
'''

# User input
t1 = tuple(map(int, input("Enter elements of first tuple: ").split()))
t2 = tuple(map(int, input("Enter elements of second tuple: ").split()))

# Concatenation
result = t1 + t2
print("Concatenated Tuple:", result)