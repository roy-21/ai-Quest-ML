'''
Set Difference: Given two sets A and B, write a Python program to find the 
difference between set A and set B (i.e., elements present in A but not in B) 
and print the result.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())

#difference (A - B)
difference_set = A - B   # or A.difference(B)

#result
print("Set A:", A)
print("Set B:", B)
print("Difference (A - B):", difference_set)