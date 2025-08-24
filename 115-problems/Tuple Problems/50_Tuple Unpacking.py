'''
Tuple Unpacking: Given a tuple with three elements (x, y, z), write a Python program
to unpack the tuple and assign the values to three variables.
'''
# user input
t = tuple(map(int, input("Enter 3 elements of the tuple: ").split()))

# tuple unpacking
x, y, z = t

print("x =", x)
print("y =", y)
print("z =", z)