'''
Set Intersection: Given two sets A and B, write a Python program to find their 
intersection and print the common elements.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())

#Find intersection
intersection = A & B   # or A.intersection(B)

#Print result
print("Set A:", A)
print("Set B:", B)
print("Intersection (Common Elements):", intersection)