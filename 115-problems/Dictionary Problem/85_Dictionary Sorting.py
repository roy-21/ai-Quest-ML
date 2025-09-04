'''
Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, 
write a Python program to sort the dictionary based on age in ascending order.
'''

#Sample dictionary
ages = {
    "Alice": 25,
    "Bob": 22,
    "Charlie": 30,
    "David": 28
}

#Sort dictionary by values (ages) in ascending order
sorted_ages = dict(sorted(ages.items(), key=lambda item: item[1]))

#Print sorted dictionary
print("Dictionary sorted by age (ascending):")
print(sorted_ages)