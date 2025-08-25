'''
Leap Year Checker:
Write a Python function called `is_leap_year` that takes a year as input 
and returns True if it is a leap year and False otherwise. 
Test the function with different years.
'''

def is_leap_year(year):
    # A leap year is divisible by 4, not divisible by 100 unless divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
years = [2000, 2004, 1900, 2023, 2024]
for y in years:
    print(f"{y} is a leap year? {is_leap_year(y)}")