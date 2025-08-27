'''
Set Symmetric Difference: Given two sets A and B, write a Python program to find the 
symmetric difference between the two sets (elements present in either A or B, but not in both)
and print the result.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())

#Find symmetric difference
sym_diff = A.symmetric_difference(B)  # or A ^ B

#result
print("Set A:", A)
print("Set B:", B)
print("Symmetric Difference (A Δ B):", sym_diff)