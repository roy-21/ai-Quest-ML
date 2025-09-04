'''
Dictionary Key Check: Write a Python program that takes a key as input and checks if 
it exists in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.
'''

#Sample dictionary
sample_dict = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22
}

#Take key input from user
key_to_check = input("Enter the key to check: ")

#Check if key exists
if key_to_check in sample_dict:
    print("Key Found")
else:
    print("Key Not Found")