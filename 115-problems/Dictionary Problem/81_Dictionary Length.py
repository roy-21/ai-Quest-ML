'''
Dictionary Length: Write a Python program to calculate and print the number of 
key-value pairs in a given dictionary.
'''

#Sample dictionary input
n = int(input("Enter number of key-value pairs: "))
user_dict = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

#Print length of dictionary
print(f"Number of key-value pairs in the dictionary: {len(user_dict)}")