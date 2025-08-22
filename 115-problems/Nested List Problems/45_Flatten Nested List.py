'''
Flatten Nested List: Write a Python program to flatten a given nested list 
and convert it into a single-dimensional list.
'''

#Function to flatten a nested list
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):   
            flat.extend(flatten_list(item))  
        else:
            flat.append(item)  
    return flat

nested_list = eval(input("Enter a nested list: "))
print("Flattened List:", flatten_list(nested_list))