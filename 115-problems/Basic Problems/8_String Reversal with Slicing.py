'''
8. String Reversal with Slicing: Write a Python function 
to reverse a given string using slicing.
'''

def reverse_string(x):
    return x[::-1]

user_input = input("Enter a string: ")
print("Reversed string:", reverse_string(user_input))
