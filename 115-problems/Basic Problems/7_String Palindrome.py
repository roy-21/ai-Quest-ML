'''
7. String Palindrome: Write a Python function to check 
if a given string is a palindrome or not.
'''


def is_palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
