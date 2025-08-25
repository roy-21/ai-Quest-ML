'''
Palindrome Checker:
Write a Python function called `is_palindrome` that takes a string as input 
and returns True if it is a palindrome and False otherwise. 
Test the function with different words.
'''

def is_palindrome(word):
    # Remove spaces and convert to lowercase for uniform checking
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Test the function
test_word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(test_word):
    print(f"'{test_word}' is a palindrome.")
else:
    print(f"'{test_word}' is not a palindrome.")
