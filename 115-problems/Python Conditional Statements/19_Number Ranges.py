'''
19. Number Ranges: Write a Python program that takes an integer as input 
and prints whether the number falls within the 
ranges: 0-50, 51-100, 101-150, or above 150.
'''


num = int(input("Enter a number: "))

if 0 <= num <= 50:
    print("The number falls in 0-50")
elif 51 <= num <= 100:
    print("The number falls in 51-100")
elif 101 <= num <= 150:
    print("The number falls in 101-150")
elif num > 150:
    print("The number is above 150")
else:
    print("The number is below 0")
