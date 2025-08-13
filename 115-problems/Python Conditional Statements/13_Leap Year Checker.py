'''
13. Leap Year Checker: Write a Python program that takes a year as input 
and determines if it is a leap year or not.
'''

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
