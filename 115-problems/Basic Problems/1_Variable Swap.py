'''
1.Variable Swap: Write a Python program to swap the values
of two variables without using a temporary variable.
'''


a, b = map(int, input("Enter your given number : ").split())

a, b = b, a
print(a, b)