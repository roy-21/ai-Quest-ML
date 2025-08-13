'''
15. Vowel or Consonant: Write a Python program that takes a single 
character as input and determines whether it is a vowel or a consonant.
'''



ch = input("Enter a single character: ")

ch = ch.lower()

if len(ch) == 1 and ch.isalpha():
    if ch in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input. Please enter a single alphabet character.")
