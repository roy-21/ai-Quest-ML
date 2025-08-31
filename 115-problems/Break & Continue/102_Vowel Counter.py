'''
Vowel Counter:
Write a Python program that takes a string as input and counts the number 
of vowels (a, e, i, o, u) in it. Use a `for` loop and `continue` to skip 
counting non-vowel characters.
'''

# Take input from the user
text = input("Enter a string: ")

# Initialize vowel count
vowel_count = 0

# Loop through each character in the string
for char in text.lower():
    if char not in "aeiou":
        continue
    vowel_count += 1

print(f"Number of vowels in the string: {vowel_count}")