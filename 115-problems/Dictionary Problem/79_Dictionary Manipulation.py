'''
Dictionary Manipulation: Given a dictionary with student names as keys and 
their corresponding scores as values, write a Python program to add a new student 
to the dictionary and update the score of an existing student.
'''

#Sample dictionary
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

#Add a new student
new_student = input("Enter the name of the new student: ")
new_score = int(input(f"Enter the score of {new_student}: "))
students[new_student] = new_score

#Update score of an existing student
existing_student = input("Enter the name of the student to update: ")
if existing_student in students:
    updated_score = int(input(f"Enter the new score for {existing_student}: "))
    students[existing_student] = updated_score
else:
    print(f"{existing_student} not found in the dictionary.")

#Print the updated dictionary
print("Updated dictionary:", students)