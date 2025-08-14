'''
29. Reverse String: Write a Python program using 
a while loop to reverse a given string.
'''


text = input("Enter a string: ")

i = len(text) - 1
reversed_str = ""

while i >= 0:
    reversed_str += text[i]
    i -= 1

print("Reversed string:", reversed_str)
