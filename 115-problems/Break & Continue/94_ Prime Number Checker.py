'''
Prime Number Checker:
Write a Python program that takes a number as input and determines if it is a prime number or not.
Use a for loop to check for factors. If a factor is found, break out of the loop.
'''

# Take input
num = int(input("Enter a number: "))

# Prime check
if num <= 1:
    print(f"{num} is NOT a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is NOT a prime number (divisible by {i}).")
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a PRIME number.")
