'''
24. Fibonacci Sequence: Write a Python program using a for loop to generate 
the Fibonacci sequence up to a given limit N.
'''

N = int(input("Enter the number:"))

a, b = 0, 1
print("Fibonacci Sequence:")

for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
