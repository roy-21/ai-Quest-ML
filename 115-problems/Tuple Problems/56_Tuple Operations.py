'''
Tuple Operations: Given two tuples of integers, write a Python program to perform 
element-wise addition, subtraction, and multiplication and create new tuples for 
each operation.
'''

#input
t1 = tuple(map(int, input("Enter elements of first tuple separated by space: ").split()))
t2 = tuple(map(int, input("Enter elements of second tuple separated by space: ").split()))

# check if lengths are equal
if len(t1) != len(t2):
    print("Tuples must be of the same length for element-wise operations.")
else:
    # element-wise addition
    add_tuple = tuple(t1[i] + t2[i] for i in range(len(t1)))
    
    # element-wise subtraction
    sub_tuple = tuple(t1[i] - t2[i] for i in range(len(t1)))
    
    # element-wise multiplication
    mul_tuple = tuple(t1[i] * t2[i] for i in range(len(t1)))
    
    print("Addition tuple:", add_tuple)
    print("Subtraction tuple:", sub_tuple)
    print("Multiplication tuple:", mul_tuple)