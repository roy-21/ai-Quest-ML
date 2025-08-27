'''
Set Operations: Given three sets A, B, and C, write a Python program to find and print 
the intersection of A and B, the union of B and C, and the difference between C and A.
'''

A = set(input("Enter elements of Set A separated by space: ").split())
B = set(input("Enter elements of Set B separated by space: ").split())
C = set(input("Enter elements of Set C separated by space: ").split())

#Intersection of A and B
intersection_AB = A & B  # or A.intersection(B)

#Union of B and C
union_BC = B | C  # or B.union(C)

#Difference between C and A
difference_CA = C - A  # or C.difference(A)

#Print results
print("Set A:", A)
print("Set B:", B)
print("Set C:", C)
print("Intersection of A and B:", intersection_AB)
print("Union of B and C:", union_BC)
print("Difference between C and A:", difference_CA)