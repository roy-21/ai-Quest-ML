'''
Dictionary Keys and Values: Write a Python program that takes a dictionary as input 
and prints all the keys and values in separate lines.
'''

#Sample dictionary input
n = int(input("Enter number of key-value pairs: "))
user_dict = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

#Print keys
print("Keys:")
for key in user_dict.keys():
    print(key)

#Print values
print("Values:")
for value in user_dict.values():
    print(value)