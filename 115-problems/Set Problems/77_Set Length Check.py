'''
Set Length Check: Write a Python program that takes a set as input and 
prints the number of elements in the set.
'''

user_set = set(input("Enter elements of the set separated by space: ").split())

#Print the number of elements
print(f"The number of elements in the set is: {len(user_set)}")