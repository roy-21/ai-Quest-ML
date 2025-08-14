'''
27. Prime Number Checker: Write a Python program using a while loop to 
check if a given number N is prime or not.
'''


n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    i = 2
    is_prime = True
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

