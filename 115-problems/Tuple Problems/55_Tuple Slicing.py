'''
Tuple Slicing: Given a tuple, write a Python program to extract a slice of elements 
from it.
'''

#input
t = tuple(input("Enter elements of the tuple separated by space: ").split())

# user input for slice range
start = int(input("Enter starting index: "))
end = int(input("Enter ending index (exclusive): "))
# extract slice
sliced_tuple = t[start:end]
print("Sliced tuple:", sliced_tuple)