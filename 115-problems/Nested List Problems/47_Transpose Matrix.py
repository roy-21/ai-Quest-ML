'''
Transpose Matrix: Write a Python program to transpose a given matrix 
represented as a nested list.
'''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Taking matrix input
matrix = []
print("Enter the matrix row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Transpose
transpose = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

# Output
print("Original Matrix:")
for row in matrix:
    print(row)

print("Transpose Matrix:")
for row in transpose:
    print(row)