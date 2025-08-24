'''
Given a list of nested lists, write a Python program 
to concatenate all the sublists into a single flat list.
'''

#User input
n = int(input("Enter number of sublists: "))

nested_list = []
for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1} separated by space: ").split()))
    nested_list.append(sublist)

#Concatenate all sublists
flat_list = []
for sub in nested_list:
    flat_list.extend(sub)

#output
print("Concatenated Flat List:", flat_list)