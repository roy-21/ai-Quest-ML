'''
18. Quadratic Equation Solver: Write a Python program that takes the 
coefficients (a, b, c) of a quadratic equation as input and calculates and 
prints the real roots (if they exist) or a message indicating the complex 
roots.
'''

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Two real roots:", root1, "and", root2)
elif D == 0:
    root = -b / (2*a)
    print("One real root:", root)
else:
    print("Complex roots (no real solution)")
