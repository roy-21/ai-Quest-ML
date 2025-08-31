'''
Password Validator:
Check if a password meets the following criteria:
1. At least 8 characters long
2. Contains both uppercase and lowercase letters
3. Has at least one digit
If valid -> print "Password accepted."
Else -> continue asking until valid password entered
'''

while True:
    password = input("Enter a password: ")

    # Condition checks
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        continue
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        continue
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        continue

    print("Password accepted.")
    break