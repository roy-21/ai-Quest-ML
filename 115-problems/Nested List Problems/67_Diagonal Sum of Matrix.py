'''
Diagonal Sum of Matrix: Given a square matrix represented as a nested list, 
write a Python program to calculate the sum of the elements in the main diagonal.
'''

#User input size of square matrix
n = int(input("Enter size of square matrix (n x n): "))

#Taking matrix input
matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix.append(row)

#Calculate diagonal sum
diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]  # main diagonal => same row & column index

#result
print("Sum of main diagonal elements:", diagonal_sum)