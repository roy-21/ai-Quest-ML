'''
Nested List Flattening: Write a Python program to flatten a nested list and convert 
it into a single-dimensional list.
'''

nested_list = []
n = int(input("Enter number of sublists: "))

for i in range(n):
    sublist = list(map(int, input(f"Enter elements for sublist {i+1} separated by space: ").split()))
    nested_list.append(sublist)

# flattening
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Flattened list:", flat_list)
