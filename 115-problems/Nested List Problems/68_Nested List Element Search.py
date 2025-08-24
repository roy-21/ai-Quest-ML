'''
Nested List Element Search: Write a Python program to search for a specific element 
in a nested list and return its position (row and column indices).
'''

#Sample nested list
nested_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

#Element to search
target = int(input("Enter the element to search: "))

#Flag to check if found
found = False

#Search through nested list
for i in range(len(nested_list)):          #rows
    for j in range(len(nested_list[i])):   #columns
        if nested_list[i][j] == target:
            print(f"Element {target} found at position: Row {i}, Column {j}")
            found = True
            break
    if found:
        break

if not found:
    print(f"Element {target} not found in the nested list.")