'''
Set Union: Given two sets A and B, write a Python program to find their 
union and print all the distinct elements from both sets.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())

#Find union
union_set = A | B   # or A.union(B)

#Print result
print("Set A:", A)
print("Set B:", B)
print("Union (All Distinct Elements):", union_set)