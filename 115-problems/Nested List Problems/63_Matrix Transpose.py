```python
'''
Matrix Transpose: Write a Python program to transpose a given matrix represented as a nested list.
'''

# User input for matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

#Input matrix
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix.append(row)

#Transpose matrix
transpose = []
for j in range(cols):
    trans_row = []
    for i in range(rows):
        trans_row.append(matrix[i][j])
    transpose.append(trans_row)

#output
print("Transposed Matrix:")
for row in transpose:
    print(row)
