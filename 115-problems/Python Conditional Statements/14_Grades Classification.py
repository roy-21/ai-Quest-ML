'''
14. Grades Classification: Write a Python program that takes a student’s 
percentage as input and prints their corresponding grade according to the 
following criteria: – 90% or above: 
A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail
'''


result = float(input("Enter your percentage: "))

if result >= 90:
    print("Grade: A+")
elif result >= 80:
    print("Grade: A")
elif result >= 70:
    print("Grade: B")
elif result >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


