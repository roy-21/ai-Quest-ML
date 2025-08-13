'''
16. Time Classification: Write a Python program that takes the time in 
hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”,
“Good Evening”, or “Good Night” based on the time.
'''

hour = int(input("Enter the hour (0-23): "))

if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
elif (21 <= hour <= 23) or (0 <= hour < 5):
    print("Good Night")
else:
    print("Invalid hour. Please enter a value between 0 and 23.")