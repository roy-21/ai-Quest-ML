'''
17. Triangle Type Checker: Write a Python program that takes three sides of 
a triangle as input and determines whether it forms an equilateral, 
isosceles, or scalene triangle.
'''

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")
