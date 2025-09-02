'''
Dictionary Merging: Given two dictionaries, write a Python program to 
merge them into a single dictionary and print the result.
'''

#Input first dictionary
n1 = int(input("Enter number of elements in first dictionary: "))
dict1 = {}
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

#Input second dictionary
n2 = int(input("Enter number of elements in second dictionary: "))
dict2 = {}
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

#Merge dictionaries
merged_dict = {**dict1, **dict2}

#Print result
print("Merged Dictionary:", merged_dict)