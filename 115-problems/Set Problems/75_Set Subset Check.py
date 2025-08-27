'''
Set Subset Check: Given two sets A and B, write a Python program to check if 
set A is a subset of set B and print the result.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())

#Check if A is a subset of B
if A.issubset(B):
    print("Set A is a subset of Set B")
else:
    print("Set A is not a subset of Set B")