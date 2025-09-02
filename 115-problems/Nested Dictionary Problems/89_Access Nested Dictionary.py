'''
Access Nested Dictionary: Given a nested dictionary containing student details, 
write a Python program to access and print specific information such as a student’s name, age, and address.
'''

#Sample nested dictionary
students = {
    "S001": {
        "name": "Alice",
        "age": 21,
        "address": "New York"
    },
    "S002": {
        "name": "Bob",
        "age": 22,
        "address": "Los Angeles"
    },
    "S003": {
        "name": "Charlie",
        "age": 20,
        "address": "Chicago"
    }
}

#Take student ID from user
student_id = input("Enter the student ID (e.g., S001): ")

#Check and print details
if student_id in students:
    print("Name:", students[student_id]["name"])
    print("Age:", students[student_id]["age"])
    print("Address:", students[student_id]["address"])
else:
    print("Student ID not found!")
