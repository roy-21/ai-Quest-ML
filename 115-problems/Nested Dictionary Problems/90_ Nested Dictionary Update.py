'''
Nested Dictionary Update: Given a nested dictionary of employee details, 
write a Python program to update an employee’s salary based on their employee ID.
'''

#Sample nested dictionary of employees
employees = {
    "E001": {"name": "John", "age": 30, "salary": 50000},
    "E002": {"name": "Alice", "age": 28, "salary": 60000},
    "E003": {"name": "Bob", "age": 35, "salary": 70000}
}

#Take input from user
emp_id = input("Enter Employee ID to update salary: ")
new_salary = int(input("Enter new salary: "))

#Update salary if employee exists
if emp_id in employees:
    employees[emp_id]["salary"] = new_salary
    print(f"Salary updated for {employees[emp_id]['name']}.")
else:
    print("Employee ID not found!")

#Print updated dictionary
print("Updated Employee Details:", employees)