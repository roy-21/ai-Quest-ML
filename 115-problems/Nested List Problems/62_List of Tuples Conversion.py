'''
List of Tuples Conversion: Given a nested list containing tuples of (x, y) 
coordinates, write a Python program to convert it into a list of x-coordinates
and a list of y-coordinates.
'''

#User input
nested_list = []
n = int(input("Enter number of tuples: "))
for i in range(n):
    x, y = map(int, input(f"Enter tuple {i+1} (x y): ").split())
    nested_list.append((x, y))

#Extract x-coordinates and y-coordinates
x_coords = [t[0] for t in nested_list]
y_coords = [t[1] for t in nested_list]

print("X-coordinates:", x_coords)
print("Y-coordinates:", y_coords)
