'''
List Element Frequency: Given a nested list containing lists of integers, 
write a Python program to count the frequency of each element in the 
entire nested list.
'''

from collections import Counter
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item)) 
        else:
            flat.append(item)
    return flat

nested_list = eval(input("Enter a nested list of integers: "))

flat_list = flatten_list(nested_list)
frequency = Counter(flat_list)

print("Element Frequencies:")
for key, value in frequency.items():
    print(f"{key}: {value}")