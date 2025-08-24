'''
Tuple Sorting: Write a Python program to sort a tuple of integers in ascending 
order.
'''

t = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))

# convert tuple to list
lst = list(t)

# sort the list
lst.sort()

# convert back to tuple if needed
sorted_tuple = tuple(lst)
print("Sorted tuple:", sorted_tuple)