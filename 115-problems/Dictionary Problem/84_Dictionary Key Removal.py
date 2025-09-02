'''
Dictionary Key Removal: Given a dictionary of items and their quantities, 
write a Python program to remove a specific item from the dictionary based on user input.
'''

#Sample dictionary
items = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "mango": 12
}

#Input key to remove
key_to_remove = input("Enter the item name to remove: ")

#Remove the key if it exists
if key_to_remove in items:
    del items[key_to_remove]
    print(f"Updated dictionary after removing '{key_to_remove}': {items}")
else:
    print(f"Item '{key_to_remove}' not found in the dictionary.")