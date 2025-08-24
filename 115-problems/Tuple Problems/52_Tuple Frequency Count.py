'''
Tuple Frequency Count: Given a tuple containing various elements, write a Python 
program to count the frequency of a specific element in the tuple.
'''

t = tuple(input("Enter elements of the tuple separated by space: ").split())

# user input for element to count
element = input("Enter the element to count: ")

# count frequency
freq = t.count(element)
print(f"The element '{element}' appears {freq} times in the tuple.")