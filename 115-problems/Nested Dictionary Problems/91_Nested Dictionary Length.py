'''
Nested Dictionary Length: Write a Python program to calculate and print 
the total number of key-value pairs in a nested dictionary.
'''

#Sample nested dictionary
students = {
    "S001": {"name": "Alice", "age": 21, "address": "New York"},
    "S002": {"name": "Bob", "age": 22, "address": "Los Angeles"},
    "S003": {"name": "Charlie", "age": 20, "address": "Chicago"}
}

#Count total key-value pairs
total_pairs = 0
for key in students:
    total_pairs += len(students[key])   #count inner dictionary items

print("Total number of key-value pairs in nested dictionary:", total_pairs)