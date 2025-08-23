'''
Greeting Generator with Nested Functions and User Input:
Write a Python function called `greeting_generator` that takes a name as input 
and returns a greeting message using nested functions. The greeting message 
should be customizable.
'''

def greeting_generator(name):
    
    # Nested function to create greeting message
    def create_message():
        return f"Hello, {name}! How are you today?"
    
    return create_message()

# Taking input from the user
user_name = input("Enter your name: ")

# Call the function and print the greeting
greeting = greeting_generator(user_name)
print(greeting)