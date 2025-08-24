'''
Nested List Element Access: Given a nested list, write a Python program to access 
and print specific elements from it.
'''

nested_list = []

rows = int(input("Enter number of rows in nested list: "))

for i in range(rows):
    row = list(map(int, input(f"Enter elements for row {i+1}, separated by space: ").split()))
    nested_list.append(row)

# access specific element
row_index = int(input("Enter row index to access: "))
col_index = int(input("Enter column index to access: "))
print("Accessed element:", nested_list[row_index][col_index])
