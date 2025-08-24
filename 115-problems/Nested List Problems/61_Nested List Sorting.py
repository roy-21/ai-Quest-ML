'''
Nested List Sorting: Given a nested list containing lists of integers, write a Python program 
to sort the sublists based on their lengths.
'''

#user input
nested_list = []
n = int(input("Enter number of sublists: "))
for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1} separated by space: ").split()))
    nested_list.append(sublist)

# Sorting sublists based on their lengths
nested_list.sort(key=len)
print("Sorted nested list by length:", nested_list)