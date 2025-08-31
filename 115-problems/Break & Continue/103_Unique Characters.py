'''
Unique Characters:
Write a Python program that takes a string as input and checks if it contains 
all unique characters (no character repeats). Use a `for` loop and `break` 
when a character repeats.
'''

# Take input from the user
text = input("Enter a string: ")

# Initialize a set to store seen characters
seen_chars = set()
is_unique = True

# Loop through each character
for char in text:
    if char in seen_chars:
        is_unique = False
        print(f"Character '{char}' is repeated. String does not have all unique characters.")
        break
    seen_chars.add(char)

if is_unique:
    print("All characters in the string are unique.")
