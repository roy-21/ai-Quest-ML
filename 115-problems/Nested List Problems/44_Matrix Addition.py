'''
Matrix Addition: Write a Python program to add two matrices represented as 
nested lists.
'''


#Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

#Input first matrix
print("Enter elements of first matrix:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

#Input second matrix
print("Enter elements of second matrix:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

#Add two matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Resultant Matrix after Addition:")
for r in result:
    print(*r)
