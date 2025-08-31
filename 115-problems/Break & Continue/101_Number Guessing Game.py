'''
Number Guessing Game:
Write a Python program that generates a random number between 1 and 100 
and lets the user guess the number. Use a `while` loop, `break` when the 
correct number is guessed, and `continue` to keep prompting the user until 
they guess correctly.
'''

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
        continue
    elif guess > secret_number:
        print("Too high! Try again.")
        continue
    else:
        print(f"Congratulations! You guessed the correct number: {secret_number}")
        break