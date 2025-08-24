'''
List of Lists Concatenation: Given a list of nested lists, write a Python 
program to concatenate all the sublists into a single flat list.
'''

n = int(input("Enter number of sublists: "))
nested_list = []

for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1}: ").split()))
    nested_list.append(sublist)

# Flatten / Concatenate all sublists
flat_list = []
for sub in nested_list:
    for item in sub:
        flat_list.append(item)

# Output
print("Concatenated Flat List:", flat_list)