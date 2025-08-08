'''
6. Data Type Checker: Write a Python function that takes 
a variable as input and returns the data type of the 
variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).
'''
def data_type_checker(x):
    return type(x).__name__

user_input = input("Enter something: ")
try:
    value = eval(user_input)
except:
    value = user_input  

print("Data type:", data_type_checker(value))
