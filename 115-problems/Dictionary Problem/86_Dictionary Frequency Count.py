'''
Dictionary Frequency Count: Write a Python program that takes a string as input 
and creates a dictionary containing each character as a key and its frequency as the value.
'''

#input
text = input("Enter a string: ")

#Initialize empty dictionary
freq_dict = {}

#Count frequency of each character
for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

#Print the frequency dictionary
print("Character Frequency Dictionary:")
print(freq_dict)
