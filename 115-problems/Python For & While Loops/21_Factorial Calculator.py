'''
21. Factorial Calculator: Write a Python program 
using a while loop to calculate the factorial of a given number N.
'''

N = int(input("Enter a number:"))

fact = 1
while N > 0:
    fact *= N
    N -= 1
print("Factorial:", fact)
