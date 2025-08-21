# Taking matrix dimensions from user
r1, c1 = map(int, input("Enter rows and columns of Matrix A:").split())
r2, c2 = map(int, input("Enter rows and columns of Matrix B:").split())

# Matrix multiplication possible only if columns of A == rows of B
if c1 != r2:
    print("Matrix multiplication not possible! Columns of A must equal rows of B.")
else:
    # Input Matrix A
    print("Enter elements of Matrix A:")
    A = []
    for i in range(r1):
        row = list(map(int, input().split()))
        A.append(row)

    # Input Matrix B
    print("Enter elements of Matrix B:")
    B = []
    for i in range(r2):
        row = list(map(int, input().split()))
        B.append(row)

    # Initialize result matrix with zeros
    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result of Matrix Multiplication:")
    for row in result:
        print(*row)
