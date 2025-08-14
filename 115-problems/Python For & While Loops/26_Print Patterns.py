'''
26. Print Patterns: Write a Python program using nested for loops to print 
various patterns, such as a right-angled triangle, an inverted right-angled
triangle, and so on.
'''

# Right-angled triangle pattern

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()




# Inverted right-angled triangle pattern
# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



#Right-Aligned Triangle Pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end=" ")
    for star in range(i):
        print("*", end=" ")
    print()
