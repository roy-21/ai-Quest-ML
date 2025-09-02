'''
Nested Dictionary Key Search:
Write a Python program that takes a key as input and searches for it 
in a nested dictionary. If found, print the corresponding value, otherwise, print “Key Not Found.”
'''

#Sample nested dictionary
student = {
    "id": 101,
    "name": "Rahim",
    "details": {
        "age": 21,
        "address": "Dhaka",
        "department": "CSE"
    }
}

# Function to search key in nested dictionary
def search_key(nested_dict, key):
    if key in nested_dict:   # Direct key match
        return nested_dict[key]
    for value in nested_dict.values():   # Search inside nested dictionaries
        if isinstance(value, dict):
            result = search_key(value, key)
            if result is not None:
                return result
    return None

# Take input from user
key_to_search = input("Enter the key to search: ")

# Search and print result
result = search_key(student, key_to_search)
if result is not None:
    print(f"Key Found! Value = {result}")
else:
    print("Key Not Found.")