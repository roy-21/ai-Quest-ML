'''
Set Superset Check: Given two sets A and B, write a Python program to check if 
set A is a superset of set B and print the result.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())

#Check if A is a superset of B
if A.issuperset(B):
    print("Set A is a superset of Set B")
else:
    print("Set A is not a superset of Set B")