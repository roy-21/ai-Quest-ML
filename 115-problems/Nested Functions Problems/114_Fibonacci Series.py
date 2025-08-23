'''
Fibonacci Series using Recursion:
Write a recursive Python function called `Fibonacci` that takes an integer N as input 
and returns the Nth number in the Fibonacci series.
'''

def Fibonacci(n):
    if n < 0:
        return "Invalid input! Enter a non-negative integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# Taking input from the user
N = int(input("Enter a non-negative integer N to get the Nth Fibonacci number: "))

# Call the function and print the result
result = Fibonacci(N)
print(f"The {N}th Fibonacci number is: {result}")