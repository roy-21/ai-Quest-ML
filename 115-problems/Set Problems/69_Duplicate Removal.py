'''
Write a Python program that takes a list of elements as input 
and creates a new set containing only the unique elements from the list.
'''

#input from user
elements = input("Enter elements separated by space: ").split()

#Convert list to set to remove duplicates
unique_set = set(elements)

print("Original list:", elements)
print("Unique elements set:", unique_set)