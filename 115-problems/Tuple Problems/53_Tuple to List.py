'''
Tuple to List: Write a Python program to convert a tuple into a list. 
'''

#input
t = tuple(input("Enter elements of the tuple separated by space: ").split())
# convert tuple to list
lst = list(t)
print("Converted list:", lst)