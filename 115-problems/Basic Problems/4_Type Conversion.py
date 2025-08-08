'''
4.Type Conversion: Given a list of integers, write a 
Python program to convert each element of the list to a string.
'''


def convert_string(int_list):
    return [str(i) for i in int_list]

input_list = list(map(int, input("Enter a list of interger:").split()))
string_list = convert_string(input_list)
print(string_list)